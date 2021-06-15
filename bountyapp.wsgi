#!/usr/bin/python3
import sys
import os
from main import app as application


sys.path.insert(0,"/var/www/bountyapp/")
application.secret_key = os.urandom(50)

activate_this = './env/bin/activate.py'
with open(activate_this) as file_:
    exec(file_.read(), dict(__file__=activate_this))
