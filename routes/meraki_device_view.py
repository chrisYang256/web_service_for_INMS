from flask import render_template
from .     import meraki_device_view

import datetime


server_time = '{}'.format(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))

@meraki_device_view.route("grafana_view/<device_serial>")
def select_grafana(device_serial):
    grafana_dashboard = f"""
        <object 
            type="text/html" 
            class="dashboard" 
            data="http://dev1.whyit.co.kr:3000/d/L-JOZulnz/ghyang-inms-meraki?orgId=1&amp;kiosk=arcus&amp;theme=light&amp;from=now-1d&amp;to=now&amp;var-client_serial={device_serial}&amp;var-base_interval=10m&amp;base_path=/grafana">
        </object>
    """
    return render_template("select_grafana.html", grafana_dashboard=grafana_dashboard)

@meraki_device_view.route("list_view")
def select_device_list():
    return render_template("select_meraki_device_list.html", server_time=server_time)

@meraki_device_view.route("detail_view/<device_serial>")
def select_device_detail(device_serial):
    return render_template("select_meraki_device_detail.html", device_serial=device_serial, server_time=server_time)

# @meraki_device_view.route("add_view")
# def add_device():
#     return render_template("add_meraki_device.html", server_time=server_time)

# @meraki_device_view.route("update_view/<device_serial>")
# def update_device(device_serial):
#     return render_template("update_meraki_device.html", device_serial=device_serial, server_time=server_time)