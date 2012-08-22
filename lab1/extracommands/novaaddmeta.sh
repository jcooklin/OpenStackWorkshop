#To launch the image again, but add more information to the server when we  boot
#This will help in identifying the server among the other machines in the cloud.
# Use the -meta option with a key=value pair, where you can make up the string for both the key and the value.
# For example, you could add a description and also the creator of the server as shown below. 
nova boot testserver --meta description='Use for testing purposes' --meta creator=Nisha
