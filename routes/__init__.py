from flask import Blueprint

snmp_device_api  = Blueprint("snmp_device_api", __name__, url_prefix="/snmp_device/api/")
snmp_device_view = Blueprint("snmp_device_view", __name__, url_prefix="/snmp_device/")

from .snmp_device_api  import *
from .snmp_device_view import *