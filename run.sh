#!/bin/bash
sudo yum update -y
sudo yum install git -y
sudo cd /home/ec2-user/
sudo git clone https://github.com/xiehuangjun/A3.git
sudo cd /home/ec2-user/A3/API/
sudo yum install mysql-devel gcc python-pip python-devel -y
sudo pip3 install PyMySQL
sudo pip3 install Flask
sudo pip3 install -U flask-cors
sudo pip3 install flask-api
