from jsl import Document, DocumentField, StringField
from .publicHearing import PublicHearing
from .procurementNotice import ProcurementNotice


class Schemas (Document):
    class Options(object):
        title = 'remaining to be standardized'
        description = 'Standardized objects included in the system.'
        definition_id = 'Objects'

    propertyDisposition = StringField(description='Referenced object to be added')
    courtNotice = StringField(description='Referenced object to be added')
    ruleDetails = StringField(description='Referenced object to be added')
    contracting = StringField(description='Referenced object to be added based on http://ocds.open-contracting.org/standard/r/1__0__RC/en/standard/intro/')


    #Additional objects can be added to this list based on need.




