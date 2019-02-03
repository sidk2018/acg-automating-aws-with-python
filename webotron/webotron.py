import boto3
import click
# import sys
session = boto3.Session(profile_name="dev")
s3 = session.resource("s3")


@click.group()
def cli():
    "Webotron deployswebsite to AWS"
    pass

@cli.command("list-buckets")
def list_buckets():
    "List all s3 buckets"
    for bucket in s3.buckets.all():
        print(bucket.name)

@cli.command("list-bucket-objects")
#enter bucket_name argument
@click.argument("bucket")
def list_bucket_objects(bucket):
    "List objects in an s3 bucket"
    #for obj in bucket.objects.all():
    #bucket= s3.bucket("bucketname")
    for obj in s3.Bucket(bucket).objects.all():
        print(obj)


if __name__ == "__main__":
    cli()

