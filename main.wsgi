#!/usr/bin/python3
import sys
sys.path.insert(0,"/var/www/bountyapp/")

from main import app as application
application.secret_key = 'Add your secret key'

