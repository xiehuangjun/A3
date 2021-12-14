sudo yum update -y
sudo yum install git -y
sudo yum install mysql-devel gcc python-pip python-devel -y
sudo pip3 install PyMySQL
cd ~/A3/API/create_table
sudo python3 create_table.py
sudo pip3 install Flask
sudo pip3 install -U flask-cors
sudo pip3 install flask-api
cd ~/A3/API
sudo python3 api.py
