#!/bin/bash
source /home/perevertysh/factory/fta/pettyenv/bin/activate
exec gunicorn  -c "/home/perevertysh/factory/fta/pettyhome/gunicorn-config.py" pettyhome.wsgi