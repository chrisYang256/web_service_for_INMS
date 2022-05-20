import sys

from flask import request

from db_connect import db
from .          import meraki_device_api
from routes     import meraki_device_query


@meraki_device_api.route("list", methods=["GET"])
def select_meraki_device_list():
    db.connect()

    offset = request.args.get("offset", default=1, type=int)
    limit  = (
        request.args.get("limit", type=int)
        if request.args.get("limit")
        else sys.maxsize
    )
    skip = int(limit * (offset - 1))

    meraki_device_list = meraki_device_query.select_meraki_device_list(limit, skip)

    if meraki_device_list is None:
        db.close()
        return { "message": "현재 입력된 장비가 없습니다.", "status": 200 }

    db.close()
    return { "meraki_device_list": meraki_device_list, "status": 201 }

@meraki_device_api.route("get/<device_serial>", methods=["GET"])
def select_meraki_device_get(device_serial: str):
    db.connect()

    meraki_device = meraki_device_query.select_meraki_device_get(device_serial)

    return { "meraki_device": meraki_device, "status": 201 }