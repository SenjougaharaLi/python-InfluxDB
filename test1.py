import codecs
import os,sys
import string
import json
from influxdb import InfluxDBClient
#client = InfluxDBClient(host='10.0.0.201', port=8086, username='admin', password='admin',ssl=True, verify_ssl=True)
# create the database
#client = InfluxDBClient('10.0.0.201', 8086, 'admin', 'admin', 'INTc')

client = InfluxDBClient(host='192.168.109.224', port=8086, username='', password='',ssl=True, verify_ssl=True)
# create the database
client = InfluxDBClient('192.168.109.224', 8086, '', '', 'INT_test') #


client.create_database('INT_test')
f = codecs.open(r"/home/lty/send_64B_1000000pps_node_7_mapInfo_0x3fff_sample_N_1_print_200ms_normal.txt", mode='r', encoding='utf-8')
line = f.readline()
while line:
    a = line.split()
    if len(a)==13:
        json_body = [
            {
            "measurement": "INT",
            "tags": {
                'DEVICE_ID': (a[3])
                },

            "fields": {
                'NODE_INT_INFO':int(a[0]),
                'ufid':int(a[1]),
                'switch_id': int(a[3]),
                'in_port':int(a[4]),
                'out_port':int(a[5]),
                'ingress_time':int(a[6]),
                'hop_latency':int(a[7]),
                'bandwidth':float(a[8]),
                'n_packets':int(a[9]),
                'n_bytes':int(a[10]),
                'quene_len':int(a[11]),
                'fwd_acts':int(a[12])
            }
        }
    ]
        client.write_points(json_body) # data input
    line = f.readline()
f.close()
"""
result = client.query('select * from INT;')
print("Result: {0}".format(result))
"""
