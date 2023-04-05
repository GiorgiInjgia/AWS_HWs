import argparse
import re

parser = argparse.ArgumentParser()
parser.add_argument("text")
args = parser.parse_args()

arg1 = args.text

result = []
for s in re.findall(r'-?\d+\.?\d*', arg1):
    result.append(float(s))

floatList = [result[0]]
oddList = [result[1]]
eventList = [result[2]]

print(floatList)
print(oddList)
print(eventList)


#
# s = [float(s) for s in re.findall(r'-?\d+\.?\d*', arg1)]
# floatList = [s[0]]
# oddList = [s[1]]
# eventList = [s[2]]
#
# print(floatList)
# print(oddList)
# print(eventList)