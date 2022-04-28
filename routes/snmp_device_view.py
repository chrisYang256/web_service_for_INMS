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
            data="http://dev1.whyit.co.kr:8082/grafana/d/CXqJyow7z/ghyang-snmp-test-20220424?orgId=1&amp;kiosk=arcus&amp;theme=light&amp;from=now-1d&amp;to=now&amp;base_path=/grafana&amp;refresh=30s&amp;&amp;var-base_interval=auto&amp;ar-device_ip={device_ip}">
        </object>
    """
    return render_template("select_grafana.html", grafana_dashboard=grafana_dashboard)

@snmp_device_view.route("list_view")
def select_device_list():
    return render_template("select_device_list.html", server_time=server_time)

@snmp_device_view.route("detail_view/<device_id>")
def select_device_detail(device_id):
    return render_template("select_device_detail.html", device_id=device_id, server_time=server_time)

@snmp_device_view.route("add_view")
def add_device():
    return render_template("add_device.html", server_time=server_time)

@snmp_device_view.route("update_view/<device_id>")
def update_device(device_id):
    return render_template("update_device.html", device_id=device_id, server_time=server_time)