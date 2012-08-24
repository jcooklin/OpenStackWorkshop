#Add security rules to the security group created
#nova secgroup-add-rule <securitygroupname> tcp 22 22 0.0.0.0/0
#nova secgroup-add-rule <securitygroupname> icmp -1 -1 0.0.0.0/0
echo "Please enter the security group name that you created earlier"
read secgroupname
nova secgroup-add-rule $secgroupname tcp 22 22 0.0.0.0/0
nova secgroup-add-rule $secgroupname icmp -1 -1 0.0.0.0/0

