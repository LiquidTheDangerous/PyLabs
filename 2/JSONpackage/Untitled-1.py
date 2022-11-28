import json
from pprint import pprint
a = {"other": [1, 2, 3], "name": "Andrey"}
a = json.dumps(a)
# a = json.loads(a)
pprint(a,indent=4)