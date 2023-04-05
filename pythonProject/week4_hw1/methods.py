import magic
from hashlib import md5
from datetime import datetime
import boto3
from botocore.exceptions import ClientError
import logging

from os import getenv
from dotenv import load_dotenv

load_dotenv()

def init_client():
    try:
        client = boto3.client("s3",
                              aws_access_key_id = getenv("aws_access_key_id"),
                              aws_secret_access_key = getenv("aws_secret_access_key"),
                              aws_session_token = getenv("aws_session_token"),
                              region_name = getenv("aws_region_name"))
        client.list_buckets()
        return client
    except ClientError as e:
        logging.error(e)
    except:
        logging.error(("Unexpected error"))



def generate_file_name(file_name) -> str:
    file_extension = file_name.split('.')[-1]
    return f'up_{md5(str(datetime.now()).encode("utf-8")).hexdigest()}.{file_extension}'


def upload_local_file(aws_s3_client, bucket_name, filename, keep_file_name=False):
    mime = magic.Magic(mime=True)
    content_type = mime.from_file(filename)
    print(content_type)
    file_name = filename.split('/')[-1] if keep_file_name else generate_file_name(filename.split('/')[-1])
    print(file_name)
    try:
        aws_s3_client.upload_file(filename, bucket_name, file_name, ExtraArgs={'ContentType': content_type})

        return f"https://{bucket_name}.s3.{getenv('aws_region_name')}.amazonaws.com/{file_name}"

    except ClientError as e:
        logging.error(e)
    except Exception as ex:
        logging.error(ex)

    return False

def list_buckets(aws_s3_client):
    try:
        buckets = aws_s3_client.list_buckets()
        if buckets:
            for bucket in buckets['Buckets']:
                print(f"    {bucket['Name']}")

    except ClientError as e:
        logging.error(e)