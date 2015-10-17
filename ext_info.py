import sys
from pathlib import Path
from collections import defaultdict


def create_suffix():
    return {'counter': 0,
            'size': 0}


suffixes = defaultdict(create_suffix)
try:
    folder = Path(sys.argv[1])
except IndexError:
    print("""usage: ext_info.py path
       displays number of files and total size of files per extension in the specified path.""")
    exit()


for file in folder.iterdir():
    if file.is_file():
        suffix = file.suffix[1:] or '.'
        suffixes[suffix]['counter'] += 1
        suffixes[suffix]['size'] += file.stat().st_size

for name, info in sorted(suffixes.items()):
    print('{} {counter} {size}'.format(name, **info))
