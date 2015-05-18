from jsl import Document, StringField, IntField


class SectionName(Document):
    class Options(object):
        title = 'SectionName'
        description = 'The name of the section under which the notice appears in the City Record.\n For DCAS, see pproc_Sections for possible values'
        definition_id = 'SectionName'

    id = IntField(description='The reference ID of the CR section ')
    name = StringField(description='sampleValue: Court Notices \nmappedField: proc_Sections \naction: 1 \ncomment: incl')	