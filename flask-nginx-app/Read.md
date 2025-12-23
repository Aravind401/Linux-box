Install Required Packages (Ubuntu)

sudo apt update

sudo apt install -y python3 python3-pip python3-venv nginx


sample code

flask-user-app/
│
├── app.py
├── templates/
│   ├── login.html
│   ├── home.html
│   ├── edit.html
│
└── static/
    └── style.css 


1.  Create Python Project

mkdir flask-nginx-app
cd flask-nginx-app

2.  Create virtual environment

python3 -m venv venv
source venv/bin/activate


3.  Install Flask & Gunicorn

pip install flask gunicorn

Test Flask App (Without Nginx)

python app.py

http://127.0.0.1:5000

4.  Run Flask with Gunicorn

gunicorn --bind 127.0.0.1:8000 app:app & 

5.  Configure nginx:
sudo nano /etc/nginx/sites-available/flaskapp

server {
    listen 80;
    server_name localhost;

    location / {
        proxy_pass http://127.0.0.1:8000;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
    }
}



Enable site


sudo ln -s /etc/nginx/sites-available/flaskapp /etc/nginx/sites-enabled/
sudo nginx -t
sudo systemctl restart nginx


http://localhost

6. MySQL Database Setup


pip install flask flask-mysqldb gunicorn

sudo mysql
ALTER USER 'root'@'localhost' IDENTIFIED WITH mysql_native_password BY 'NewPass@123';
FLUSH PRIVILEGES;
EXIT;


CREATE DATABASE userdb;
USE userdb;

CREATE TABLE login_users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(50) UNIQUE,
    password VARCHAR(255)
);

CREATE TABLE users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(50),
    dob DATE,
    email VARCHAR(100),
    phone VARCHAR(15)
);



INSERT INTO login_users (username, password)
VALUES ('admin', 'admin123');

