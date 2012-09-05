#launch an instance of the virtual machine
#To launch a server, you choose an image you want to match up to a size and use a flavor that you prefer,
# if  you want to start small with about 2 GB of memory you'd choose the m1.small flavor
#nova boot --flavor=<flavorId> --image=<imageId> <instance name>
echo "Please enter flavorId"
read flavorid
echo "Please enter imageid"
read imageid
echo "Please enter a  instance name starting with your idsid ex:idsidinstance"
read instancename 

echo "Please enter key pair name "
read keypair

nova boot --flavor=$flavorid --image=$imageid --key_name $keypair  $instancename


