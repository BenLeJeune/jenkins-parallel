"""
This is the start script - this runs before the parallel process.
This will obtain all the projects, and put them in a list somewhere
"""
import pandas as pd
import os

df = pd.DataFrame(["Project A", "Project B", "Project C"], columns=["Project"])
df.to_csv('projects.csv', index=False, header=False)

print("Project list obtained!")

try:
    os.mkdir('tmp')
except Exception as e:
    print(f"An error occurred while creating the /tmp/ directory: {e}")


print(f"Username: {os.getenv('USERNAME')}")
print(f"Password: {os.getenv('PASSWORD')}")