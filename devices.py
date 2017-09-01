from socket import *
from uuid import getnode as get_mac
import socket
import MySQLdb

db = MySQLdb.connect("localhost", "root", "", "detect")
cursor = db.cursor()
#Device details function
def device_details():
    print('running~')

    network = '146.64.204.'

    def is_up(addr):
        s = socket(AF_INET, SOCK_STREAM)
        s.settimeout(0.01)
        if not s.connect_ex((addr)):
            s.close()
            return 1
        else:
            s.close()


    for ip in xrange(48, 108):
        addr = network + str(ip)
        mac = (get_mac())
        theVal = ''
        theNam = addr
        theStat = (getfqdn(addr))
        cursor = db.cursor()


        if (getfqdn(addr) == addr):
            print 'Ip Address'  + '\t' + '' + '\t' + '' + '\t' + 'Pc Name' '\t' + '' + '\t' + 'Status'
            print (addr)  + '\t' + '' + '\t'+ '' + '\t'+ (getfqdn(addr))+ '\t' + ('Off')

            try:
                # Execute the SQL command
                cursor.execute('UPDATE details SET Status = "Offline" WHERE IP_Address = "%s"' % (addr))
                db.commit()
            except:
                db.rollback()

        else:
            print 'Ip Address'  + '\t' + '' + '\t' + '' + '\t' + 'Pc Name' '\t' + '' + '\t' + 'Status'
            print (addr)  + '\t' + '' + '\t'+ '' + '\t'+ (getfqdn(addr)) + '\t' + ('On')

            try:
                # Execute the SQL command
                cursor.execute('UPDATE details SET Status = "Online" WHERE IP_Address = "%s"' % (addr))
                db.commit()
            except:
                # Rollback in case there is any error
                db.rollback()


        try:
                # Execute the SQL command
            cursor.execute('UPDATE details SET PC_Name = "%s" WHERE IP_Address = "%s"' % (getfqdn(addr),addr))
            db.commit()
        except:
                # Rollback in case there is any error
            db.rollback()
