from jsl import Document, StringField, IntField, NumberField, DateTimeField, DocumentField
from .organization import Organization
from .address      import Address


class Meeting(Document):
    class Options(object):
        title = 'Meeting'
        description = 'Standardized as defined by the Popolo Project\nSee: http://www.popoloproject.com/specs/event.html'
        definition_id = 'Meeting'


    name            = StringField(description='sampleValue: City Bike Hearing \nmappedField: \naction:1 \ncomment:')
    description     = StringField(description='sampleValue: Spector Hall 22 Reade Street New York NY \nmappedField: \naction:1 \ncomment:')
    startTime       = DateTimeField(description='sampleValue: An ISO 8601 formatted date-time field. \nmappedField: \naction: \ncomment:')
    endTime         = DateTimeField(description='sampleValue: An ISO 8601 formatted date-time field. \nmappedField: \naction: \ncomment:')
    location        = DocumentField(Address, as_ref=True)
    #status         =
    identifier      = IntField(description='323 \nmappedField: \naction:3 \ncomment:')
    classification  = IntField(description='323 \nmappedField: \naction:3 \ncomment: Need to create a classification topic table')
    organization    = DocumentField(Organization, as_ref=True)
    #attendee       =
    #parent event   =