from jsl import StringField, IntField
from .skeleton import Skeleton


class Procurement(Skeleton):
    '''Example to show how to inherit/extend an entity.
    This class will generate this schema: https://crow-schema.herokuapp.com/#procurement.json
    '''

    class Options(object):
        title = 'Procurement'
        definition_id = 'procurement'
        description = 'Procurement definition, as defined by...'

    pin = StringField(description='pin needed to identify this contract')
    money = IntField(description='cost associated with this agreement/contract')

