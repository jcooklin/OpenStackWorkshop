#Command to create security group
#nova secgroup-create <security groupname> <description>
echo "Please enter a security group name starting with your idsid"
read secgroupname
nova secgroup-create $secgroupname  "securitygroup for workshop"

