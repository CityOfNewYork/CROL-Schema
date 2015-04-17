from jsl import Document, StringField, IntField, NumberField
from .organization import Organization


class Address(Document):
    class Options(object):
        title = 'Address'
        description = 'Address field defined by CROW. To standardize toward http://schema.org/Place'
        definition_id = 'address'

    complete    = StringField(description='sampleValue: Spector Hall 22 Reade Street New York NY \nmappedField: \naction:1 \ncomment:')
    name        = StringField(description='sampleValue: Spector Hall \nmappedField:  \naction: 1 \ncomment: ')
    address1    = StringField(description='sampleValue: 22 Reade Street \nmappedField:  \naction: 1 \ncomment:')
    address2    = StringField(description='sampleValue: \nmappedField:  \naction: 1 \ncomment:')
    city        = StringField(description='sampleValue: New York \nmappedField:  \naction: 1 \ncomment:')
    state       = StringField(description='sampleValue: New York \nmappedField:  \naction: 1 \ncomment:')
    zip         = NumberField(description='sampleValue: 10001 \nmappedField:  \naction: 1 \ncomment:')
    lat         = NumberField(description='sampleValue: 40.751320 \nmappedField:  \naction: 3 \ncomment:')
    long        = NumberField(description='sampleValue: -74.006172 \nmappedField:  \naction: 3 \ncomment:')
    latLong     = StringField(description='sampleValue: 40.751320, -74.006172 \nmappedField:  \naction: 3 \ncomment:')
