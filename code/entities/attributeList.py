from jsl import Document, ArrayField, DocumentField, StringField


class Attributes(Document):
    class Options(object):
        title = 'Data Standard Attributes'
        description = 'Attributes provide more structure to each notice. If nothing else is specified, multiple attributes can be added to each notice.'
        definition_id = 'Attributes'

    noticeItem = StringField(description='Referenced attribute to be added')
    refOrganization = StringField(description='Referenced attribute to be added')
    refAddress = StringField(description='Referenced attribute to be added')
    refMeeting = StringField(description='Referenced attribute to be added')

    #Additional attributes can be added to this list based on need.

