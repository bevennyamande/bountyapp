#!/usr/bin/python3
import sys
sys.path.insert(0,"/var/www/html/facial-recognition-reggy/")

from main import app as application
application.secret_key = 'Add your secret key'

