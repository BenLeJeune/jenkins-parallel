"""
This is the start script - this runs before the parallel process.
This will obtain all the projects, and put them in a list somewhere
"""

import pandas as pd

df = pd.DataFrame(["Project A", "Project B", "Project C"], columns=["Project"])
df.to_csv('projects.csv', index=False)

print("Project list obtained!")