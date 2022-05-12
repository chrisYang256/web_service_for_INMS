from flask import Blueprint

snmp_device_api    = Blueprint("snmp_device_api", __name__, url_prefix="/snmp_device/api/")
snmp_device_view   = Blueprint("snmp_device_view", __name__, url_prefix="/snmp_device/")
meraki_device_api  = Blueprint("meraki_device_api", __name__, url_prefix="/meraki_device/api/")
meraki_device_view = Blueprint("meraki_device_view", __name__, url_prefix="/meraki_device/")

from .snmp_device_api  import *
from .snmp_device_view import *
from .meraki_device_api import *
from .meraki_device_view import *