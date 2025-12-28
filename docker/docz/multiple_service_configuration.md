Step 1: Run Multiple Applications (Docker)

App1 (2 containers)
docker run -d --name app1-1 -p 8081:80 nginx
docker run -d --name app1-2 -p 8082:80 nginx

App2 (2 containers)
docker run -d --name app2-1 -p 8091:80 nginx
docker run -d --name app2-2 -p 8092:80 nginx

🔹 Step 2: NGINX Configuration

Create config:

sudo nano /etc/nginx/conf.d/multi-app.conf

✅ Multi-Application Load Balancer
# APP 1
upstream app1_backend {
    server 127.0.0.1:8081;
    server 127.0.0.1:8082;
}

# APP 2
upstream app2_backend {
    server 127.0.0.1:8091;
    server 127.0.0.1:8092;
}

server {
    listen 8080;

    location /app1/ {
        proxy_pass http://app1_backend/;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
    }

    location /app2/ {
        proxy_pass http://app2_backend/;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
    }
}

🔹 Step 3: Restart & Test
sudo nginx -t
sudo systemctl restart nginx

Test
curl localhost:8080/app1
curl localhost:8080/app2


✔ Each app routes correctly
✔ Each app has its own load balancing
