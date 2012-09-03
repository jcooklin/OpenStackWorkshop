#!/usr/bin/env python
import boto

conn = boto.connect_ec2()
user_data = open('../user_data/user_data')
reservation = conn.run_instances(image_id="ami-967edcff",key_name="mykeys2",instance_type="t1.micro",security_groups=["my default"])
