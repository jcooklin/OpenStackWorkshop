#Add security rules to the security group created
#nova secgroup-add-rule <securitygroupname> tcp 22 22 0.0.0.0/0
#nova secgroup-add-rule <securitygroupname> icmp -1 -1 0.0.0.0/0
nova secgroup-add-rule workshopsecgroup tcp 22 22 0.0.0.0/0
nova secgroup-add-rule workshopsecgroup icmp -1 -1 0.0.0.0/0


