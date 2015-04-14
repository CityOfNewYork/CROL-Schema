from jsl import Document, StringField, IntField


class Organization(Document):
    class Options(object):
        title = 'Organization'
        description = 'A DCAS Organization.\nSee: http://talk.beta.nyc'
        definition_id = 'org'

    agencyCode = IntField(description='An agency code as defined by DCAS')
    agencyName = StringField()
    agency = StringField()
    agencyDivisionId = IntField()
    parent = IntField()
    name = StringField()
    agencyDivision = StringField()
