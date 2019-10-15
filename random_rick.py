from glob import glob
import random
import os

extensions = (".mkv", ".avi", ".mp4", ".mkv")
ricks = []

# list all directory files
for ext in extensions:
    ricks.extend(glob(f'.\\ricks\\*{ext}'))

# get a random item from list
rick_selected = random.choice(ricks)

# execute file by command line
print(f'Playing  {rick_selected}')
os.system(f'"{rick_selected}"')
