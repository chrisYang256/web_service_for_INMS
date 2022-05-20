from flask import render_template
from .     import snmp_device_view

import datetime


server_time = '{}'.format(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))

@snmp_device_view.route("list_view")
def select_device_list():
    return render_template("select_snmp_device_list.html", server_time=server_time)

@snmp_device_view.route("detail_view/<device_id>")
def select_device_detail(device_id):
    return render_template("select_snmp_device_detail.html", device_id=device_id, server_time=server_time)

@snmp_device_view.route("add_view")
def add_device():
    return render_template("add_snmp_device.html", server_time=server_time)

@snmp_device_view.route("update_view/<device_id>")
def update_device(device_id):
    return render_template("update_snmp_device.html", device_id=device_id, server_time=server_time)