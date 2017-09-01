
from xml.dom import minidom
import MySQLdb
from django.shortcuts import render
from django.views.generic import TemplateView
from createjson import createJson
from time import sleep
from ScanNetwork import scanNet
from portsScanner import portScan
from devices import device_details

db = MySQLdb.connect("localhost", "root", "", "detect")
cursor = db.cursor()


#Home page tamplate
scanNet()
device_details()
createJson()
sleep(0.1)
portScan()

class home(TemplateView):
    def get(self, request, **kwargs):
        return render(request, 'index.html',)

#device details template
def devices(request):
    cursor = db.cursor()
    sql = " select * from details"
    cursor.execute(sql)
    results = cursor.fetchall()
    return render(request, "devices.html", {"results": results})

#searching PC details function
def index_search(request):
    adress=request.POST.get('search','')

    cursor = db.cursor()

    cursor.execute("select * FROM details where IP_Address='" + adress + "'")

    results=cursor.fetchall()
    cursor.close()


    return render(request, "index.html", {"results":results})

#add organization PCs function
def add_pc(request):

    adress = request.POST.get('add', '')
    cursor = db.cursor()

    mac=''

    xmldoc = minidom.parse('NmapResults.xml')
    itemlist = xmldoc.getElementsByTagName('address')

    for device in itemlist:

            if device.getAttribute('addrtype') == "mac":
                MAC_Address = device.attributes['addr'].value
            elif device.getAttribute('addrtype') == "ipv4":
                IP_Address = device.attributes['addr'].value
                if IP_Address == adress:
                    print MAC_Address
                    mac= MAC_Address


    sql = "INSERT INTO local_pc(no, ip, mac) VALUES ( '%s', '%s', '%s' )" % ('', adress, mac)

    try:
        # Execute the SQL command
        cursor.execute(sql)
        db.commit()
    except:
        db.rollback()

    createJson()
    sleep(0.1)
    return render(request, "index.html", )

#check for vulnerability template
def Vul(request):
    cursor = db.cursor()
    sql = " select * from port "
    cursor.execute(sql)
    results = cursor.fetchall()
    return render(request, "View Ports.html", {"results": results})


#views open ports template
def ViewP(request):
    db = MySQLdb.connect("localhost", "root", "", "detect")
    cursor = db.cursor()
    sql = " select * from count "
    cursor.execute(sql)
    results = cursor.fetchall()
    db.close()
    return render(request, "Vulnerability.html", {"results": results})



