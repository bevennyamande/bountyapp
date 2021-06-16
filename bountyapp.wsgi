#!/usr/bin/python3
import sys
import logging
import os

logging.basicConfig(stream=sys.stderr)
sys.path.insert(0,"/var/www/bountyapp/")

from bountyapp import app as application
application.secret_key = os.urandom(30)
