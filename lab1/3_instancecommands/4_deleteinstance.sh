#Delete the instance of Virtual machine created
#nova delete <instance name>
echo "Please enter the instance that you created earlier"
read instancename
nova delete $instancename


