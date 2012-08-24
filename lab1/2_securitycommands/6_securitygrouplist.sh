#Command to check the rules added to the security group
#nova secgroup-list-rules <securitygroupname>
echo "Please enter the secgroup name that you created"
read secgroupname
nova secgroup-list-rules $secgroupname
