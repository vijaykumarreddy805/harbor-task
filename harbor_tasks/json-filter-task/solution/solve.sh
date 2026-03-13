#!/bin/bash
python3 -c "
import json

with open('/app/input.json', 'r') as f:
    users = json.load(f)

adults = [u['name'] for u in users if u['age'] >= 18]

with open('/app/output.txt', 'w') as f:
    f.write('\n'.join(adults) + '\n')
"
