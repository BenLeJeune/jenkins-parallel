from argparse import ArgumentParser

parser = ArgumentParser(
    description='This program executes once per project, as determined by the start stage.',
)

parser.add_argument('project_name')
args = parser.parse_args()

print(f'Python file executed, target project: {args.project_name}')