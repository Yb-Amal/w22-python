from awscode import listInstances,stopInstances

dev_filter = {'Name': 'tag:env', 'Values': ['dev']}

instances = listInstances(dev_filter)

stopInstances(instances)
