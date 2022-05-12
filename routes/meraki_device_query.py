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

# def create_meraki_device(ip, port, name, descr):
#     meraki_device_data = """
#         insert into 
#         meraki_devices(ip, port, name, descr)
#         values(%s, %s, %s, %s)
#     """
#     cursor.execute(meraki_device_data, (ip, port, name, descr))

# def update_meraki_device(ip, port, name, descr, device_device_serial):
#     now_date = datetime.datetime.now()

#     meraki_device_data = """
#         update meraki_devices
#         set ip=%s, port=%s, name=%s, descr=%s, udate=%s
#         where device_serial=%s
#     """
#     cursor.execute(meraki_device_data, (ip, port, name, descr, now_date, device_device_serial))

# def delete_meraki_device(device_device_serial):
#     target_meraki_device = """
#         delete from meraki_devices
#         where device_serial=%s
#     """
#     cursor.execute(target_meraki_device, (device_device_serial))