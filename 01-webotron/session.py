import boto3
#connect using awscli config/dev profile
session = boto3.Session(profile_name="dev")

#switch to s3 area
s3 = session.resource("s3")



"""
# create new buckett
new_Bucket = s3.create_bucket(Bucket='ttgen-lab01-aws-autoamtion', CreateBucketConfiguration={
        'LocationConstraint': 'us-east-2'
    })
"""
for bucket in s3.buckets.all():
    print (bucket.name)

# delete_Bucket = s3.delete_bucket(Bucket='ttgen-lab01-aws-autoamtion')
