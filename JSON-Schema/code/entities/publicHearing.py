from jsl import DocumentField
from .meeting import Meeting
from .skeleton import Skeleton


class PublicHearing(Skeleton):
    class Options(object):
        title = 'PublicHearing'
        definition_id = 'PublicHearing'
        description = 'PublicHearing, a sub-schema, is used for ' \
                      'publishing notices for public meetings and hearings'

    meeting = DocumentField(Meeting, as_ref=True)
