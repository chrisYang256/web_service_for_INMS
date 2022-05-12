from flask import render_template
from .     import snmp_device_view

import datetime


server_time = '{}'.format(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))

@snmp_device_view.route("grafana_view/<device_ip>")
def select_grafana(device_ip):
    grafana_dashboard = f"""
        <object 
            type="text/html" 
            class="dashboard" 
            data="http://dev1.whyit.co.kr:3000/d/AQWi8rQnk/ghyang-inms?orgId=1&amp;kiosk=arcus&amp;theme=light&amp;from=now-1d&amp;to=now&amp;var-device_ip={device_ip}&amp;var-base_interval=10m&amp;base_path=/grafana">
        </object>
    """
    return render_template("select_grafana.html", grafana_dashboard=grafana_dashboard)

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