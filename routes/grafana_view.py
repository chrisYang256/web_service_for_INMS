from flask import render_template
from .     import grafana_view


@grafana_view.route("main_view")
def select_grafana_main():
    grafana_dashboard = f"""
        <object 
            type="text/html" 
            class="dashboard" 
            data="http://dev1.whyit.co.kr:3000/d/N9Cf9pu7k/ghyang-integrated-inms?orgId=1&amp;kiosk=arcus&amp;theme=light&amp;from=now-1d&amp;to=now&amp;base_path=/grafana">
        </object>
    """
    return render_template("select_grafana.html", grafana_dashboard=grafana_dashboard)

@grafana_view.route("meraki_view/<device_serial>")
def select_grafana_meraki(device_serial):
    grafana_dashboard = f"""
        <object 
            type="text/html" 
            class="dashboard" 
            data="http://dev1.whyit.co.kr:3000/d/L-JOZulnz/ghyang-inms-meraki?orgId=1&amp;kiosk=arcus&amp;theme=light&amp;from=now-1d&amp;to=now&amp;var-client_serial={device_serial}&amp;var-base_interval=10m&amp;base_path=/grafana">
        </object>
    """
    return render_template("select_grafana.html", grafana_dashboard=grafana_dashboard)

@grafana_view.route("snmp_view/<device_ip>")
def select_grafana_snmp(device_ip):
    grafana_dashboard = f"""
        <object 
            type="text/html" 
            class="dashboard" 
            data="http://dev1.whyit.co.kr:3000/d/AQWi8rQnk/ghyang-inms?orgId=1&amp;kiosk=arcus&amp;theme=light&amp;from=now-1d&amp;to=now&amp;var-device_ip={device_ip}&amp;var-base_interval=10m&amp;base_path=/grafana">
        </object>
    """
    return render_template("select_grafana.html", grafana_dashboard=grafana_dashboard)