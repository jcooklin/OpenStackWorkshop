======================
OpenStack Workshop '12
======================

Summary
=======

This repo contains everything required to facilitate an introduction to OpenStack workshop.  Within the activities directory are two labs that introduce the user to the nova CLI and the API through the python-novaclient.  The setup directory contains the scripts and automation for deploying devstack_ instances into AWS.  Finally the ittlcsite contains a simple Django app is used to register devstack instances and logins as servers are deployed so the logins can later be allocated to the lab participants.

Lab 1 - Managing Openstack through nova CLI (Command Line Interface) and using Dashboard 
========================================================================================

Managing Openstack through nova CLI (Command Line Interface) and using Dashboard 

- Users will be introduced to nova CLI.  
- Using various nova commands users will check services, launch instances, create security keypairs and login into the instance created

Lab 2 - Programming OpenStack, Its the API 
==========================================

- Users will be introduced to the API through the python-novaclient module.  
- Similar to what was done in Lab 1, users will be able to use the python novaclient to list available images, flavors and to launch and destroy their instance.

Deploying Devstack
------------------

We deploy devstack on a Ubuntu Cloud Imagei (12.04).  The image contains CloudInit_ a facility to bootstrap automation and customizations which we leveraged to add/install manage users, devstack, ssh, GateOne (html5 ssh client) and integrate with our server/login registration app.  

Scripts to provision EC2 instances: ./setup/bin/create_*_devstack_instance.py

CloudInit
~~~~~~~~~

CloudInit_ handles early initialization of a cloud instance.  Some of the things it can configure include locale, hostname, generating and managing ssh keys, setting up ephemeral mount points, installing apps, etc.  We choose to use a Mime Multi Part archive so that we could separate the automation into multiple scripts.  We have a script for creating users, installing devstack and installing GateOne_.

Create multipart user_data:
write-mime-multipart setup/user_data/10_create_users setup/user_data/20_install_devstack setup/user_data/30_install_gateone setup/user_data/40_install_misc > setup/user_data/user_data

The resulting setup/user_data/user_data file is referenced by the boto run_instance call in the create scripts located in setup/bin.

Mapping available server/logins to users - Registration App
-----------------------------------------------------------

The directory ittlcsite contains a Django web app app for handling server and login registration.  The app provides REST service endpoints for registering servers/logins and allocating users to available logins.  The app depends on sqllite and can easily be hosted on an micro ec2 instance.   

.. _CloudInit: https://help.ubuntu.com/community/CloudInit
.. _devstack: http://devstack.org/
.. _GateOne: https://github.com/liftoff/GateOne
