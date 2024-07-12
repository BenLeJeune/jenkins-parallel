"""
This is a script that will be executed once per project, as determined by projects.csv.
In the actual pipeline, this will fetch the data for each project, and save it to a temporary csv.
"""
from argparse import ArgumentParser
from random import random
import pandas as pd
import time

parser = ArgumentParser(
    description='This program executes once per project, as determined by the start stage.',
)
parser.add_argument('project_name')
args = parser.parse_args()

time_to_wait = random()
time.sleep(time_to_wait)

print(f'Python file executed after ${time_to_wait}s, target project: {args.project_name}')

last_word = args.project_name.split(' ')[-1]

df = pd.DataFrame([{
    "project": args.project_name,
    "identifier": last_word,
    "sleep_time": time_to_wait
}])

df.to_csv(f'./tmp/{args.project_name}.csv')