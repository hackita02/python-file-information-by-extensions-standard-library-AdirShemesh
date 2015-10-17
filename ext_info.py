import sys
from pathlib import Path
from collections import defaultdict


def create_suffix():
    return {'counter': 0,
            'size': 0}


suffixes = defaultdict(create_suffix)
for p in Path(sys.argv[1]).iterdir():
    if p.is_file():
        suffixes[p.suffix or '.']['counter'] += 1
        suffixes[p.suffix or '.']['size'] += p.stat().st_size

for name, info in sorted(suffixes.items()):
    print('{} {counter} {size}'.format(name, **info))
