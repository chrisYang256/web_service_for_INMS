import pymysql, datetime

from db_connect import cursor


def select_meraki_device_list(limit, skip):
    meraki_device_list = """
        select *
        from meraki_devices
        order by cdate DESC
        limit %s offset %s
    """
    cursor.execute(meraki_device_list, (limit, skip))
    meraki_device_list = cursor.fetchall()

    return meraki_device_list

def select_meraki_device_get(device_serial):
    meraki_device = """
        select *
        from meraki_devices
        where serial=%s
    """
    cursor.execute(meraki_device, (device_serial))
    meraki_device = cursor.fetchone()

    return meraki_device