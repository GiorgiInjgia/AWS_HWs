from methods import *
import argparse

parser = argparse.ArgumentParser(
    description="CLI program that helps with uploading files on S3 buckets.",
    usage='''
    How to upload file:
    short:
        python week4_hw1.py -up -bn <bucket_name> -fn <file_path> 
    long:
       python main.py --upload_file --bucket_name <bucket_name> --file_name <file_path>

    How to list buckets:
    short:
        python main.py -lb
    long:
        python main.py --list_buckets

    ''',
    prog='week4_hw1.py',
    epilog='hw1')

parser.add_argument("-bn",
                    "--bucket_name",
                    type=str,
                    help="Pass bucket name.",
                    default=None)

parser.add_argument("-fn",
                    "--file_name",
                    type=str,
                    help="Pass file name.",
                    default=None)

parser.add_argument("-kfn",
                    "--keep_file_name",
                    help="Flag to keep original file name.",
                    choices=["False", "True"],
                    type=str,
                    nargs="?",
                    const="True",
                    default="False")

parser.add_argument("-lb",
                    "--list_buckets",
                    help="Flag to list bucket",
                    choices=["False", "True"],
                    type=str,
                    nargs="?",
                    const="True",
                    default="False")

parser.add_argument("-uf",
                    "--upload_file",
                    help="Flag to upload file",
                    choices=["False", "True"],
                    type=str,
                    nargs="?",
                    const="True",
                    default="False")


s3_client = init_client()
args = parser.parse_args()

if s3_client:
    if args.bucket_name and args.file_name and args.upload_file:
        file_url = upload_local_file(s3_client, args.bucket_name, args.file_name, args.keep_file_name)
        print(file_url)
    if args.list_buckets == "True":
        list_buckets(s3_client)

