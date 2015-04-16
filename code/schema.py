import json
from entities.noticeData import NoticeData

print(json.dumps(NoticeData.get_schema(), indent=True))
