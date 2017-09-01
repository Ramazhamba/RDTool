# Create your views here.
import subprocess
from xml.dom import minidom
import MySQLdb


def scanNet():
    subprocess.call("nmap -oA NmapResults  146.64.204.48-108")

    db = MySQLdb.connect("localhost", "root", "", "detect")
    cursor = db.cursor()

    IP_Address = ''
    MAC_Address = ''

    xmldoc = minidom.parse('NmapResults.xml')
    itemlist = xmldoc.getElementsByTagName('address')

    for device in itemlist:
        if device.getAttribute('addrtype') == "ipv4":
            IP_Address = device.attributes['addr'].value
            print(device.attributes['addr'].value)

            sql = "INSERT INTO details(IP_Address, MAC_Address, PC_Name, Status) VALUES ( '%s', '%s', '%s', '%s' )" % (
                IP_Address, '', '', '')

            try:
                # Execute the SQL command
                cursor.execute(sql)
                # Commit your changes in the database
                db.commit()
            except:
                # Rollback in case there is any error
                db.rollback()

        elif device.getAttribute('addrtype') == "mac":
            MAC_Address = device.attributes['addr'].value
            print(device.attributes['addr'].value)

            sql = 'UPDATE details SET MAC_Address = "%s" WHERE IP_Address = "%s"' % ( MAC_Address,IP_Address)

            try:
                # Execute the SQL command
                cursor.execute(sql)
                # Commit your changes in the database
                db.commit()
            except:
                # Rollback in case there is any error
                db.rollback()