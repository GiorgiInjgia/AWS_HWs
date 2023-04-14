
import magic
import boto3
from os import getenv
from dotenv import load_dotenv
from botocore.exceptions import ClientError
import json
from random import randint
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


def read_random_quote():
    filename = "quetes.json"
    with open(filename, 'r') as qt:
        quotes_lst = json.load(qt)

    rint = randint (0,len(quotes_lst))
    print("author: \n", quotes_lst[rint]["author"])
    print("quote: \n", quotes_lst[rint]["text"])



def read_quote(author):
    filename = "quetes.json"
    quotes = list()
    with open(filename, 'r') as qt:
        quotes_lst = json.load(qt)


    for quote in quotes_lst:
        if quote["author"] == author:
            print("quotes: ")
            print(quote["text"])
            quotes.append(quote["text"])

    return {author: quotes}


def upload_static_web_files(aws_s3_client, bucket_name, quote):

    aws_s3_client.put_object(Bucket=bucket_name,
                             Key="quotes.json",
                             Body=json.dumps(quote),
                             # ExtraArgs={'ContentType': "json"}
                             )

    return f"http://{bucket_name}.s3.us-west-2.amazonaws.com/quotes.json"


def bucket_exists(aws_s3_client, bucket_name) -> bool:
    try:
        response = aws_s3_client.head_bucket(Bucket=bucket_name)
        status_code = response["ResponseMetadata"]["HTTPStatusCode"]
        if status_code == 200:
            return True
    except ClientError as e:
        print(e)
        return False


