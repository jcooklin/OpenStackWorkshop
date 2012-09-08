#!/usr/bin/env python
import boto

conn = boto.connect_ec2()
user_data = open('../user_data/user_data')
reservation = conn.run_instances(image_id="ami-967edcff"
        ,instance_type="m1.large"
        ,key_name="mykeys2"
        ,user_data=user_data.read()
        ,security_groups=["my default"])
