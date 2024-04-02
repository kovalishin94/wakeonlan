# -*- coding: utf-8 -*-

import django
import os
import sys

sys.path.append(os.path.join(os.path.abspath(os.path.dirname(__file__)), '..'))
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'wakeup_backend.settings')
django.setup()

from core.models import Computer

from scapy.layers.l2 import getmacbyip

all_computers = Computer.objects.all()

for computer in all_computers:
    try:
        mac = getmacbyip(computer.ip_address)
    except:
         continue
    if mac == None:
        continue

    for i in mac:
            mac = mac.replace(':', '-')

    if mac == computer.mac_address:
        continue


    computer.mac_address = mac
    computer.save()