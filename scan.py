# Port scan function
import MySQLdb
import nmap

#def portScan():
nm = nmap.PortScanner()
nm.scan('146.64.204.48-108')

db = MySQLdb.connect("localhost", "root", "", "detect")

cursor = db.cursor()
IP_addre = ''
Ports = ''
Stat = ''
count = ''
St = ''
count = 0
Ports = ''

for host in nm.all_hosts():
    print ('-------------------------------')
    print ('Host : %s (%s)' % (host, nm[host].hostname()))
    IP_addre = host
    print ('State : %s' % nm[host].state())
    Stat = nm[host].state()

    for proto in nm[host].all_protocols():
        print ('-------- Open ports --------------')
        print ('Protocol : %s' % proto)

        for port in nm[host][proto]:

            Ports = Ports + ' ' + str(port)
            count = count + 1
            print  Ports
            print "TOTAL NO OF PORTS:", count

        if count <= 2:
            St = "LOW"
        elif count > 2 & count < 4:
            St = "HIGH"

            print St
        elif count > 4:
            St = "HIGH"
            print St

        sqli = "INSERT INTO count (IP_Address,OpenPorts,Vulnerability) VALUES ('%s','%s','%s')" % (IP_addre, count, St)

        try:
            cursor.execute(sqli)
            # Commit your changes in the database
            db.commit()

        except:
            db.rollback()


    sql = "INSERT INTO port (IP_Address, Status,ports,total) VALUES ( '%s', '%s', '%s' , '%s')" % (IP_addre, Stat, Ports, count)

    try:
        cursor.execute(sql)
        # Commit your changes in the database
        db.commit()

    except:
        db.rollback()

db.close()