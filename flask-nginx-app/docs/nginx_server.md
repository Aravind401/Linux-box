# nginx server configuration 
# replace into default path /etc/nginx/sites-enabled/default

server {
    listen 443 ssl http2 default_server;
    listen [::]:443 ssl http2 default_server;

    server_name linux-box;

    ssl_certificate     /home/xor/linux-box/Linux-box/nginx/cert/linux-box.com+2.pem;
    ssl_certificate_key /home/xor/linux-box/Linux-box/nginx/cert/linux-box.com+2-key.pem;

    ssl_protocols TLSv1.2 TLSv1.3;
    ssl_ciphers HIGH:!aNULL:!MD5;
    ssl_prefer_server_ciphers off;

    # ---------------- Flask App ----------------
    location / {
        proxy_pass http://127.0.0.1:8000;
        proxy_http_version 1.1;

        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;

        proxy_redirect off;
    }

    # ---------------- Static Files ----------------
    location /static/ {
        # path need to change here
        alias /home/xor/flask-nginx-app/static/;
        expires 30d;
        access_log off;
    }
}

