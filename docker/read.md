# (Optional – avoid sudo every time)
    sudo usermod -aG docker $USER
    newgrp docker

# Create folders
    mkdir -p ~/nginx-lb/app1 ~/nginx-lb/app2

    App1 config:
        vi ~/nginx-lb/app1/index.html

        <h1>Hello from APP 1 (Port 8081)</h1>

    App2 config

        nano ~/nginx-lb/app2/index.html

        <h1>Hello from APP 2 (Port 8082)</h1>

# Step 3: Run Multiple Docker Containers
    App1 container

docker run -d \
  --name app1 \
  -p 8081:80 \
  -v ~/nginx-lb/app1:/usr/share/nginx/html \
  nginx

App2 container

docker run -d \
  --name app2 \
  -p 8082:80 \
  -v ~/nginx-lb/app2:/usr/share/nginx/html \
  nginx


Test:

http://localhost:8081

http://localhost:8082


Step 4: Install NGINX on Host (Load Balancer)
sudo apt install nginx -y

🔹 Step 5: Configure NGINX Load Balancer

Create config:

sudo nano /etc/nginx/conf.d/docker-lb.conf

✅ NGINX Load Balancer Config
upstream docker_backend {
    server 127.0.0.1:8081;
    server 127.0.0.1:8082;
}

server {
    listen 8080;

    location / {
        proxy_pass http://docker_backend;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
    }
}

🔹 Step 6: Restart & Test NGINX
sudo nginx -t
sudo systemctl restart nginx


Open:

http://localhost:8080


🔁 Refresh page → response alternates between APP1 & APP2 🎉


# remove all images in your machine
 docker system prune -a

