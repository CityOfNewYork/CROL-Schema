import json
from entities.notice import Notice

print(json.dumps(Notice.get_schema(), indent=True))
