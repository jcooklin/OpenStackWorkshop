# coding: utf-8
 
# create a Nova client object

ip = 'http://' + raw_input("Enter your ip: " )
url = ip + ':5000/v2.0'

user = raw_input("Enter Username: ") 

pwd = raw_input("Enter Password: ")

tenant = raw_input("Enter Tenant name: ")

from novaclient.v1_1 import client
nc = client.Client(user, pwd, tenant ,url, service_type="compute")

print"List keypairs available in the cloud are:"
print(nc.keypairs.list())
 

