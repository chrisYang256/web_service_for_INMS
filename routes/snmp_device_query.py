import pymysql, datetime

from db_connect import cursor


def select_snmp_device_list(limit, skip):
    snmp_device_list = """
        select *
        from snmp_devices
        order by cdate DESC
        limit %s offset %s
    """
    cursor.execute(snmp_device_list, (limit, skip))
    snmp_device_list = cursor.fetchall()

    return snmp_device_list

def select_snmp_device_get(device_id):
    snmp_device = """
        select *
        from snmp_devices
        where id=%s
    """
    cursor.execute(snmp_device, (device_id))
    snmp_device = cursor.fetchone()

    return snmp_device

def create_snmp_device(ip, port, name, descr):
    snmp_device_data = """
        insert into 
        snmp_devices(ip, port, name, descr)
        values(%s, %s, %s, %s)
    """
    cursor.execute(snmp_device_data, (ip, port, name, descr))

def update_snmp_device(ip, port, name, descr, device_id):
    now_date = datetime.datetime.now()

    snmp_device_data = """
        update snmp_devices
        set ip=%s, port=%s, name=%s, descr=%s, udate=%s
        where id=%s
    """
    cursor.execute(snmp_device_data, (ip, port, name, descr, now_date, device_id))

def delete_snmp_device(device_id):
    target_snmp_device = """
        delete from snmp_devices
        where id=%s
    """
    cursor.execute(target_snmp_device, (device_id))