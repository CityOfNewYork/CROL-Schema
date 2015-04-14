from jsl import Document, StringField, IntField
from jsl import DocumentField

from .organization import Organization

class Skeleton(Document):

    class Options(object):
        title = 'NoticeBase'
        definition_id = 'basenotice'
        description = '''The schema is still a working draft, but the
 completion of it is fairly simple if we can make sure that we are on the same
 page with DCAS as to what we are trying to do.
'''

    requestId = StringField(required=True)
    typeOfNotice = IntField(required=True)
    noticeTypeName = StringField(required=True)
    sectionName = StringField()
    shortTitle = StringField()
    noticeDescription = StringField()
    otherInfo = StringField()
    printOut = StringField()
    organization = DocumentField(Organization, as_ref=True)
