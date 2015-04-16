from jsl import Document, ArrayField, DocumentField
from .skeleton import Skeleton
from .schemaList import Schemas
from .attributeList import Attributes


class NoticeData(Document):
    class Options(object):
        title = 'Notice Data Standard (City Record)'
        description = 'A standard optimized for structured and standardized pubclishing of notice data.'
        definition_id = 'NoticeData'

    skeleton 	= DocumentField(Skeleton, as_ref=True)
    schema   	= DocumentField(Schemas, as_ref=True)
    attributes 	= DocumentField(Attributes)
