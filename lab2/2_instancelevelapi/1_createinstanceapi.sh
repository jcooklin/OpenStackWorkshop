#Launch an instance of the Virtual machine using nova client API
#nc.serververs.create(“InstanceName”, nc.images.list()[0], nc.flavors.list()[0])

nc.serververs.create("workshopinstance2", nc.images.list()[0], nc.flavors.list()[0])


