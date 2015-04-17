from jsl import Document, DocumentField, OneOfField
from .attributeList import Attributes
from .skeleton import Skeleton
from .publicHearing import PublicHearing
from .procurementNotice import ProcurementNotice
from .schemaList		import Schemas


class NoticeData(Document):
    class Options(object):
        title = 'Notice Data Standard (City Record)'
        description = 'A standard optimized for structured and ' \
                      'standardized pubclishing of notice data.'
        definition_id = 'NoticeData'

    skeleton = DocumentField(Skeleton)
    objects = OneOfField([ProcurementNotice, PublicHearing, Schemas])
    attributes = DocumentField(Attributes)

