from jsl import Document, DocumentField, OneOfField
from .attributeList import Attributes
from .skeleton import Skeleton
from .publicHearing import PublicHearing
from .procurementNotice import ProcurementNotice


class NoticeData(Document):
    class Options(object):
        title = 'Notice Data Standard (City Record)'
        description = 'A standard optimized for structured and ' \
                      'standardized pubclishing of notice data.'
        definition_id = 'NoticeData'

    doc = OneOfField([Skeleton, ProcurementNotice, PublicHearing])
    attributes = DocumentField(Attributes)
