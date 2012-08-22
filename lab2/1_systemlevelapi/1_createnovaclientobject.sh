#Create a Nova client object
#nc = client.Client(“Username",“Password",“TenantName","http://<nova server IP>:5000/v2.0",service_type="compute")

python
from novaclient.v1_1 import client
nc = client.Client("workshop","workshop","TenantName","http://<nova server IP>:5000/v2.0",service_type="compute")
 

