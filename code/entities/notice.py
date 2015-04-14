from jsl import Document, ArrayField, DocumentField
from .skeleton import Skeleton
from .noticeitem import NoticeItem


class Notice(Document):
    class Options(object):
        title = 'Notice'
        description = 'Notice type'
        definition_id = 'notices'

    doc = DocumentField(Skeleton, as_ref=True)
    items = ArrayField(NoticeItem)
