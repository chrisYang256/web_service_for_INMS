import sys

from flask import request

from db_connect import db
from .          import snmp_device_api
from routes     import snmp_device_query


@snmp_device_api.route("list", methods=["GET"])
def select_snmp_device_list():
    db.connect()

    offset = request.args.get("offset", default=1, type=int)
    limit = (
        request.args.get("limit", type=int)
        if request.args.get("limit")
        else sys.maxsize
    )
    skip = int(limit * (offset - 1))

    snmp_device_list = snmp_device_query.select_snmp_device_list(limit, skip)

    if snmp_device_list is None:
        db.close()
        return { "message": "현재 입력된 장비가 없습니다.", "status": 200 }

    db.close()
    return { "snmp_device_list": snmp_device_list, "status": 201 }

@snmp_device_api.route("get/<device_id>", methods=["GET"])
def select_snmp_device_get(device_id: int):
    db.connect()

    snmp_device = snmp_device_query.select_snmp_device_get(device_id)

    return { "snmp_device": snmp_device, "status": 201 }

@snmp_device_api.route("add", methods=["POST"])
def create_snmp_device():
    db.connect()

    ip    = request.form["ip"]
    name  = request.form["name"]
    descr = request.form["descr"]

    snmp_device_query.create_snmp_device(ip, name, descr)

    db.commit()
    db.close()

    return { "message": "success", "Status": 201 }

@snmp_device_api.route("update/<device_id>", methods=["PUT"])
def update_snmp_device(device_id: int):
    db.connect()

    ip    = request.form["ip"]
    name  = request.form["name"]
    descr = request.form["descr"]

    snmp_device_query.update_snmp_device(ip, name, descr, device_id)

    db.commit()
    db.close()

    return { "message": "success", "Status": 201 }

@snmp_device_api.route("delete/<device_id>", methods=["DELETE"])
def delete_snmp_device(device_id: int):
    db.connect()

    snmp_device_query.delete_snmp_device(device_id)

    db.commit()
    db.close()

    return { "message": "success", "Status": 201 }