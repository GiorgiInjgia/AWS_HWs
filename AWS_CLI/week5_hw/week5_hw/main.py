from os import getenv
import logging
from botocore.exceptions import ClientError
from methods import *
import argparse

parser = argparse.ArgumentParser(
    description="CLI program that helps with S3 buckets.",
    prog='main.py',
    epilog='DEMO APP - 2 FOR BTU_AWS'
)

parser.add_argument("-fp",
                    "--file_path",
                    type=str,
                    help="list bucket object",
                    nargs="?",
                    default=None)

parser.add_argument("-bn",
                    "--bucket_name",
                    type=str,
                    help="list bucket object",
                    nargs="?",
                    default=None)

parser.add_argument("-hw",
                    "--host_website",
                    help="flag to assign read bucket policy.",
                    choices=["False", "True"],
                    type=str,
                    nargs="?",
                    const="True",
                    default="False")
parser.add_argument("-lb",
                    "--list_bucket",
                    help="flag to assign read bucket policy.",
                    choices=["False", "True"],
                    type=str,
                    nargs="?",
                    const="True",
                    default="False")

args = parser.parse_args()
s3_client = init_client()

if args.list_bucket:
    bucket = list_buckets(s3_client)
    for i in bucket["Buckets"]:
        print(i["Name"])

if args.bucket_name:
    if args.bucket_name and args.host_website == "True" and args.file_path:
        policy = set_bucket_website_policy(s3_client, args.bucket_name, True)
        if policy:
            url = static_web_page_file(s3_client, args.bucket_name, args.file_path)
            print(url)

