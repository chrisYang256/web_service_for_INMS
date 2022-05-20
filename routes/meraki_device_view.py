from flask import render_template
from .     import meraki_device_view

import datetime


server_time = '{}'.format(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))

@meraki_device_view.route("list_view")
def select_device_list():
    return render_template("select_meraki_device_list.html", server_time=server_time)

@meraki_device_view.route("detail_view/<device_serial>")
def select_device_detail(device_serial):
    return render_template("select_meraki_device_detail.html", device_serial=device_serial, server_time=server_time)