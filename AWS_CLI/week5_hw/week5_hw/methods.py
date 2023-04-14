from pathlib import Path
import pylibmagic
import magic
import boto3
from os import getenv
from dotenv import load_dotenv
from botocore.exceptions import ClientError

load_dotenv()


def init_client():
    client = boto3.client(
        "s3",
        aws_access_key_id=getenv("aws_access_key_id"),
        aws_secret_access_key=getenv("aws_secret_access_key"),
        aws_session_token=getenv("aws_session_token"),
        region_name=getenv("aws_region_name")
    )
    client.list_buckets()

    return client


def list_buckets(aws_s3_client) -> list:
  return aws_s3_client.list_buckets()


def set_bucket_website_policy(aws_s3_client, bucket_name, switch):
    website_configuration = {
        # 'ErrorDocument': {'Key': 'error.html'},
        "IndexDocument": {"Suffix": "index.html"},
    }

    response = None

    if switch:
        response = aws_s3_client.put_bucket_website(
            Bucket=bucket_name,
            WebsiteConfiguration=website_configuration)
    else:
        response = aws_s3_client.delete_bucket_website(Bucket=bucket_name)

    status_code = response["ResponseMetadata"]["HTTPStatusCode"]
    if status_code == 200:
        return True
    return False


def static_web_page_file(aws_s3_client, bucket_name, filename):
    if not bucket_exists(aws_s3_client, bucket_name):
        raise ValueError("Bucket does not exists")
    root = Path(f'{filename}').expanduser().resolve()

    def __handle_directory(file_folder):
        if file_folder.is_file():
            raise ValueError("Bucket does not exists")

        for each_path in file_folder.iterdir():
            if each_path.is_dir():
                __handle_directory(each_path)
            if each_path.is_file():
                __upload_static_web_files(aws_s3_client, bucket_name, each_path, str(each_path.relative_to(root)))

    __handle_directory(root)

    # public URL
    return "http://{0}.s3-website-{1}.amazonaws.com".format(
        bucket_name,
        getenv("aws_s3_region_name", "us-west-2")
    )


def __upload_static_web_files(aws_s3_client, bucket_name, file_path, filename):
    uploaded = {}

    mime_type = magic.from_file(file_path, mime=True)

    allowed_types = {
        ".html": "text/html",
        ".css": "text/plain"
    }

    content_type = mime_type if mime_type in allowed_types.values() else None

    if ".css" == file_path.suffix:
        content_type = "text/css"

    if content_type:
        aws_s3_client.upload_file(
            file_path,
            bucket_name,
            filename,
            ExtraArgs={'ContentType': content_type}
        )
        uploaded[file_path] = filename
        print(content_type, mime_type)


def bucket_exists(aws_s3_client, bucket_name) -> bool:
    try:
        response = aws_s3_client.head_bucket(Bucket=bucket_name)
        status_code = response["ResponseMetadata"]["HTTPStatusCode"]
        if status_code == 200:
            return True
    except ClientError as e:
        print(e)
        return False
