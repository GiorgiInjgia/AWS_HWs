
from methods import *
import argparse

parser = argparse.ArgumentParser(
    description="CLI program ",
    prog='main.py',
    epilog='wh5_2. work with quotes'
)

parser.add_argument("-it",
                    "--inspite",
                    type=str,
                    help="enterh author",
                    nargs="?",
                    default=None)

parser.add_argument("-bn",
                    "--bucket_name",
                    type=str,
                    help="list bucket object",
                    nargs="?",
                    default=None)

parser.add_argument("-i",
                    "--inspire",
                    help="flag to call random quotes.",
                    choices=["False", "True"],
                    type=str,
                    nargs="?",
                    const="True",
                    default="False")

parser.add_argument("-sv",
                    "--save",
                    help="flag to save quote on aws.",
                    choices=["False", "True"],
                    type=str,
                    nargs="?",
                    const="True",
                    default="False")

args = parser.parse_args()
s3_client = init_client()

if args.inspire == "True":
    read_random_quote()

elif args.inspite and args.bucket_name and args.save == "True":
    qt = read_quote(args.inspite)
    uploaded_file = upload_static_web_files(s3_client, args.bucket_name, qt)
    print(uploaded_file)

elif args.inspite:
    read_quote(args.inspite)
