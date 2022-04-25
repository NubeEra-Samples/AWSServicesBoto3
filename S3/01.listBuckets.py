import boto3
AWS_REGION="us-west-2"

client=boto3.client("s3",region_name=AWS_REGION)

response=client.list_buckets()

for b in response["Buckets"]:
    print(b['Name'])