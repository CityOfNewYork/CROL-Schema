from jsl import Document, StringField, IntField


class NoticeType(Document):
    class Options(object):
        title = 'NoticeType'
        description = 'The type of notices available.\n For DCAS, see proc_Type_of_Notice for possible values'
        definition_id = 'noticeType'

    id = IntField(description='The reference ID of the notice type ')
    name = StringField(description='sampleValue: Public Hearing \nmappedField: Descr [proc_Type_of_Notice.csv] \naction: 1 \ncomment: incl')