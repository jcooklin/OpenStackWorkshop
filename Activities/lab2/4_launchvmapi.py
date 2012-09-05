# coding: utf-8
 
# ---------------ACTIVITY1- create a Nova client object

ip = 'http://' + raw_input("Enter your ip: " )
url = ip + ':5000/v2.0'

user = raw_input("Enter Username: ") 

pwd = raw_input("Enter Password: ")

tenant = raw_input("Enter Tenant name: ")

from novaclient.v1_1 import client
nc = client.Client(user, pwd, tenant ,url, service_type="compute")


# ---------------ACTIVITY2 -Launch an instance

instancename = raw_input("Please enter instance name: ")
print"Launching instance in cloud:"
 
#nc.serververs.create(“InstanceName”, nc.images.list()[0], nc.flavors.list()[0])
nc.servers.create(instancename, nc.images.list()[0], nc.flavors.list()[0])


# ---------------ACTIVITY3 -List instances in the cloud
print"List of instances in the cloud"
print(nc.servers.list())


#----------------ACTIVITY4444 - Terminate an instance
#Terminate the instance API 
#nc.servers.list()[0].delete
