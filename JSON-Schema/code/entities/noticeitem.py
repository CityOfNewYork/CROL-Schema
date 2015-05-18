from jsl import Document, StringField, IntField, ArrayField, DocumentField
from .organization import Organization


class NoticeItem(Document):
    class Options(object):
        title = 'Notice Item'
        description = ''
        definition_id = 'noticeitem'

    id = IntField(description='')
    description = StringField(description='')
    itemObject = StringField()
    itemAction = StringField()
    adminContext = StringField()
    documentContext = StringField()
    refOrg = ArrayField(DocumentField(Organization, as_ref=True))
