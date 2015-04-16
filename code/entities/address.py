from jsl import Document, StringField, IntField


class Address(Document):
    class Options(object):
        title = 'Address'
        description = 'A DCAS Organization.\nSee: http://talk.beta.nyc\n'
        definition_id = 'address'

    agencyCode = IntField(description='An address code as defined by DCAS')
    agencyName = StringField()
    agency = StringField()
    agencyDivisionId = IntField()
    parent = IntField()
    name = StringField()
    agencyDivision = StringField()
