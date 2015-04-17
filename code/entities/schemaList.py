from jsl import Document, DocumentField, StringField
from .publicHearing import PublicHearing
from .procurementNotice import ProcurementNotice


class Schemas (Document):
    class Options(object):
        title = 'Standardized Schemas'
        description = 'Each schema can be queried a. separatly in its whole as a full schema or b. together with a skeleton as a notice as a notice'
        definition_id = 'Objects'

    publicHearing = DocumentField(PublicHearing, as_ref=True)
    procurementNotice = DocumentField(ProcurementNotice, as_ref=True)
    contracting = StringField(description='Referenced object to be added based on http://ocds.open-contracting.org/standard/r/1__0__RC/en/standard/intro/')
    propertyDisposition = StringField(description='Referenced object to be added')
    courtNotice = StringField(description='Referenced object to be added')
    ruleDetails = StringField(description='Referenced object to be added')

    #Additional objects can be added to this list based on need.




