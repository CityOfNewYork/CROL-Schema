from jsl import Document, StringField, IntField, DateTimeField
from jsl import DocumentField
from .meeting import Meeting


class PublicHearing(Document):
    class Options(object):
        title = 'PublicHearing'
        definition_id = 'PublicHearing'
        description = 'PublicHearing, a sub-schema, is used for publishing notices for public meetings and hearings'

    meeting = DocumentField (Meeting)