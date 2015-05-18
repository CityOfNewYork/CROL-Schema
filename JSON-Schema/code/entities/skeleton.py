from jsl import Document, StringField, IntField, DateTimeField
from jsl import DocumentField
from .noticeType import NoticeType
from .sectionName import SectionName
from .organization import Organization

class Skeleton(Document):
    class Options(object):
        title = 'NoticeSkeleton'
        definition_id = 'NoticeSkeleton'
        description = 'The notice skeleton constitutes the base response for each notice. It includes normalized and standardized fields that are common to all notices.'

    noticeTitle = StringField(description='sampleValue: Public Hearing on Bikelanes \nmappedField: ShortTitle \naction: 0 \ncomment:')
    noticeType = DocumentField(NoticeType, as_ref=True)
    sectionName = DocumentField(SectionName, as_ref=True)
    noticeDescription = StringField(description='sampleValue: Hello world of engaged New Yorkers! \nmappedField: AdditionalDescription \naction: 0 \ncomment:')
    publishingOrganization = DocumentField(Organization, as_ref=True)
    noticeStartDate = DateTimeField(description='sampleValue: An ISO 8601 formatted date-time field. \nmappedField: StartDate \naction: 0 \ncomment:')
    noticeEndDate = DateTimeField(description='sampleValue: An ISO 8601 formatted date-time field. \nmappedField: EndDate \naction: 0 \ncomment:')
    otherInfo = StringField(description='sampleValue: The services cannot be timely procured through competitive sealed... \nmappedField: PrintOut \naction: 0 \ncomment:IN ')
    printOut = StringField(description='sampleValue: "CITRIX XENAPP ENTERPRISE SOFTWARE..." \nmappedField: PrintOut \naction: 0 \ncomment: IP')
    createdAt = DateTimeField(description='sampleValue: An ISO 8601 formatted date-time field. \nmappedField: ? \naction: 0 \ncomment: IP This needs to be located. ')
    lastUpdatedAt = DateTimeField(description='sampleValue: An ISO 8601 formatted date-time field. \nmappedField: ? \naction: 0 \ncomment: Needs to be computed?')
