from jsl import Document, ArrayField, DocumentField, StringField
from .organization import Organization
from .address import Address
from .meeting import Meeting




class Attributes(Document):
    class Options(object):
        title = 'Attributes'
        description = 'Provide more structure for each notice'
        definition_id = 'Attributes'

    noticeItem = StringField(description='Breaks down agendas into multiple items. Standardization in progress')
    refOrganization = ArrayField(DocumentField(Organization))
    refAddress = ArrayField(DocumentField(Address))
    refMeeting = ArrayField(DocumentField(Meeting))

    #Additional attributes can be added to this list based on need.
