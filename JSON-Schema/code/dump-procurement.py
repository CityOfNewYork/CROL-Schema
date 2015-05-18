from entities import Procurement
import json

print(json.dumps(Procurement.get_schema(), indent=True))
