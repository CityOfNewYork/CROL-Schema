from jsl import Document, ArrayField, DocumentField, StringField
from .organization import Organization
from .address import Address
from .meeting import Meeting




class Attributes(Document):
    class Options(object):
        title = 'Data Standard Attributes'
        description = 'Attributes provide more structure to each notice. If nothing else is specified, multiple attributes can be added to each notice.'
        definition_id = 'Attributes'

    noticeItem = StringField(description='Referenced attribute to be added')
    refOrganization = DocumentField(Organization)
    refAddress = DocumentField(Address)
    refMeeting = DocumentField(Meeting)

    #Additional attributes can be added to this list based on need.

