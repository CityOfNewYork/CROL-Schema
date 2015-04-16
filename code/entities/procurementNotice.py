from jsl import Document, StringField, IntField, DateTimeField
from jsl import DocumentField
from .meeting import Meeting
from. organization import Organization


class ProcurementNotice(Document):
    class Options(object):
        title = 'ProcurementNotice'
        definition_id = 'ProcurementNotice'
        description = 'ProcurementNotice, a sub-schema, is used for publishing notices for procurement notices from the Mayors Office of Contract Services (will depreciate and merge into open-contracting.org framework)'


requestingOrganization					= DocumentField(Organization, as_ref=True)
vendor									= DocumentField(Organization, as_ref=True)
descriptionOfServices					= StringField(description='sampleValue:  \nmappedField: AdditionalDescription \naction: 0 \ncomment:')
orginalAwardMethod						= StringField(description='sampleValue:  \nmappedField: AdditionalDescription \naction: 0 \ncomment:')
contractTypeFMS							= StringField(description='sampleValue:  \nmappedField: AdditionalDescription \naction: 0 \ncomment:')
originalContactEndDate					= DateTimeField(description='sampleValue: An ISO 8601 formatted date-time field. \nmappedField: StartDate \naction: 0 \ncomment:')
metodOfExtension						= StringField(description='sampleValue:  \nmappedField: AdditionalDescription \naction: 0 \ncomment:')
newStartDateExtension					= DateTimeField(description='sampleValue: An ISO 8601 formatted date-time field. \nmappedField: StartDate \naction: 0 \ncomment:')
newEndDateExtension						= DateTimeField(description='sampleValue: An ISO 8601 formatted date-time field. \nmappedField: StartDate \naction: 0 \ncomment:')
modificationOfServices					= StringField(description='sampleValue:  \nmappedField: AdditionalDescription \naction: 0 \ncomment:')
reasonForRenewal						= StringField(description='sampleValue:  \nmappedField: AdditionalDescription \naction: 0 \ncomment:')
personnelInSimiliarTitles				= StringField(description='sampleValue:  \nmappedField: AdditionalDescription \naction: 0 \ncomment:')
personnelInSimiliarTitlesHeadcount		= IntField(description='sampleValue:  \nmappedField: AdditionalDescription \naction: 0 \ncomment:')


