#!/bin/bash
sudo yum update -y
sudo yum install git -y
cd /home/ec2-user/
sudo git clone https://github.com/xiehuangjun/A3.git
cd /home/ec2-user/A3/API/
sudo sed -i -e 's/host_value/[Database's name]/g' -e 's/port_value/[Port]/g' -e 's/user_value/[User]/g' -e 's/password_value/[Password]/g' config.ini
sudo yum install mysql-devel gcc python-pip python-devel -y
sudo pip3 install PyMySQL
cd /home/ec2-user/A3/API/create_table
sudo python3 create_table.py
sudo pip3 install Flask
sudo pip3 install -U flask-cors
sudo pip3 install flask-api
cd /home/ec2-user/A3/API
sudo python3 api.py
