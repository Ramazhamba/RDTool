import json
import MySQLdb
import collections
import socket

def createJson():
    IP = socket.gethostbyname(socket.gethostname())

    db = MySQLdb.connect("localhost", "root", "", "detect")
    cursor = db.cursor()

    cursor.execute("""SELECT * 
        FROM details""")
    rows = cursor.fetchall()
    # result = rows
    data_array = []
    nodeID = "n"
    number = 1

    for data in rows:
        jData = collections.OrderedDict()

        if  data[3] == "Online":
            jData['color'] = "green"

        elif data[3] == "Offline" :
            jData['color'] = "gray"


        if IP == data[0]:
            jData['size'] = "4"
        elif IP != data[0]:
            jData['size'] = "2"

        jData['label'] = data[2]
        jData['id'] = data[0]
        number += 1

        data_array.append(jData)


    edges_array = []
    num = 1
    edge = "e"
    for ip in rows:
        ipData = collections.OrderedDict()
        ipData['source'] = ip[0]
        ipData['id'] = edge + str(num)
        ipData['target'] = IP
        num += 1
        edges_array.append(ipData)

    with open('C:\\Users\\MTshiololi\\Documents\\CSIR PROJECT\\Detecting\\SystemApp\\static\\SystemApp\\js\\results.json', 'wb+') as f:
        jsonData = {
            'nodes': data_array,
            'edges': edges_array
        }
        json.dump(jsonData, f, rows, indent=2)



