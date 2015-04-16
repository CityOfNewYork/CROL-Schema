from jsl import Document, ArrayField, DocumentField, StringField
from .skeleton import Skeleton


class Schemas (Document):
    class Options(object):
        title = 'Standardized Schemas'
        description = 'Each schema can be queried a. separatly in its whole as a full schema or b. together with a skeleton as a notice as a notice'
        definition_id = 'Objects'

    contracting = StringField(description='Referenced object to be added based on http://ocds.open-contracting.org/standard/r/1__0__RC/en/standard/intro/')
    publicHearing = StringField(description='Referenced object to be added')
    propertyDisposition = StringField(description='Referenced object to be added')
    courtNotice = StringField(description='Referenced object to be added')
    ruleDetails = StringField(description='Referenced object to be added')

    #Additional objects can be added to this list based on need.




