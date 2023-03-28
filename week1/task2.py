import argparse
# from pathlib import Path
import boto3
parser = argparse.ArgumentParser()

parser.add_argument("first_number")
parser.add_argument("second_number")

args = parser.parse_args()

arg1 = int(args.first_number)
arg2 = int(args.second_number)

def armstrong_detector(start, end):
    armstrong_numbers = []

    for number in range(start, end):
        pow = len(str(number))
        sum_each_element = 0

        for each_element in str(number):
            sum_each_element += int(each_element) ** pow

        if number == sum_each_element:
            armstrong_numbers.append(number)

    return armstrong_numbers


def recursive_sum(any_integer_array):
    if len(any_integer_array) == 1:
        return any_integer_array[0]
    else:
        return any_integer_array[0] + recursive_sum(any_integer_array[1:])


print(
    f"""
  numbers: {armstrong_detector(arg1, arg2)} 
  sum: {sum(armstrong_detector(arg1, arg2))} 
  recursive_sum: {recursive_sum(armstrong_detector(arg1, arg2))}"""
)