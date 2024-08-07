import boto3

ec2 = boto3.client('ec2', region_name="us-east-1")


dev_filter = {'Name': 'tag:env', 'Values': ['dev']}
qa_filter = {'Name': 'tag:env', 'Values': ['qa']}
prod_filter = {'Name': 'tag:env', 'Values': ['prod']}
stopped_instances = {'Name': 'instance-state-name', 'Values': ['stopped']}
instance_type_filter = {'Name': 'instance-type', 'Values': ['t2.micro']}


def listInstances(*args):
    try:
        response = ec2.describe_instances(Filters = [*args])
        instance_list = []
        for instance in response ['Reservations']:
            instance_id = instance['Instances'][0]['InstanceId']
            instance_list.append(instance_id)

        return instance_list
    except Exception as e:
        print(f"ERROR: {e}")


def startInstances(instance_list):
    try:
        ec2.start_instances(InstanceIds= instance_list)
    except Exception as e:
        print(f"Error: {e}")

def stopInstances(instance_list):
    try:
        ec2.stop_instances(InstanceIds= instance_list)
    except Exception as e:
        print(f"Error: {e}")















































# import boto3

# ec2 = boto3.client('ec2', region_name="us-east-1")

# response = ec2.describe_instances()
# instance_list = []
# for instance in response ['Reservations']:
#     instance_list.append(instance['Instances'][0]['InstanceId'])

    


























































































# import boto3
# ec2 = boto3.client('ec2', region_name="us-east-1")
# #_iam = boto3.client('iam')
# #_s3 = boto3.client('s3')
# dev_filter = {'Name': 'tag:env', 'Values': ['dev']}
# qa_filter = {'Name': 'tag:env', 'Values': ['qa']}
# prod_filter = {'Name': 'tag:env', 'Values': ['prod']}
# stopped_instance = {'Name': 'instance-state-name' , 'Values' : ['stopped']}
# instance_type_filter = {'Name': 'instance-type' , 'Values' : ['t2.micro']}
# response = ec2.describe_instances(Filters=[stopped_instance])
# instance_list = []
# for instance in response['Reservations']:
#     instance_id = instance['Instances'][0]['InstanceId']
#     instance_list.append(instance_id)
# print(instance_list)


# ec2.stop_instances(InstanceIds=instance_list)

# import boto3

# # Initialize a session using Amazon EC2
# ec2 = boto3.client('ec2', region_name="us-east-1")

# # Define filters
# running_instance_filter = {'Name': 'instance-state-name', 'Values': ['running']}
# instance_type_filter = {'Name': 'instance-type', 'Values': ['t2.micro']}
# env_filter = {'Name': 'tag:env', 'Values': ['dev', 'qa', 'prod']}

# # Describe instances with the specified filters
# response = ec2.describe_instances(Filters=[running_instance_filter, instance_type_filter, env_filter])

# # List to hold the instance IDs
# instance_list = []

# # Extract instance IDs from the response
# for reservation in response['Reservations']:
#     for instance in reservation['Instances']:
#         instance_id = instance['InstanceId']
#         instance_list.append(instance_id)

# # Print the instance IDs
# print("Instance IDs to be stopped:", instance_list)

# # Stop instances if there are any running
# if instance_list:
#     ec2.stop_instances(InstanceIds=instance_list)
#     print("Instances are stopping...")
