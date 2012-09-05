#Create Security keypair
#nova keypair-add  <keypair name> 
echo "Please enter a Keypair name starting with your idsid"
read keypairname
nova keypair-add $keypairname

