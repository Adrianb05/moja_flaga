
import os

os.system('sudo apt install python3-pip python3-dev python3-venv build-essential libssl-dev libffi-dev python3-setuptools')
os.system('sudo apt install nano')
os.system('sudo apt remove apache2')
os.system('sudo apt install nginx')
os.system('sudo systemctl enable nginx')
os.system('sudo systemctl start nginx')

os.system('sudo rm -r /var/www/html')
