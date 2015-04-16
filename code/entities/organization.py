from jsl import Document, StringField, IntField


class Organization(Document):
    class Options(object):
        title = 'Organization'
        description = 'Standardized as defined by the Popolo Project\nSee: http://www.popoloproject.com/specs/organization.html'
        definition_id = 'org'


    name                = StringField(description='sampleValue: Department of Transportation \nmappedField: If publishingOrganization:AgencyName, if ref:AdditionalDescription \naction: 0/1 \ncomment: ')
    #alternate name
    #former name
    identifier          = StringField(description='sampleValue: 675 \nmappedField: If publishingOrganization:AgencyCode/AgencyDivision, if ref:AdditionalDescription \naction: 0/1 \ncomment: ')
    classification      = StringField(description='sampleValue: Agency \nmappedField: \naction: 3 \ncomment: ')
    parentOrganization  = StringField(description='sampleValue: Department of Transportation \nmappedField: AgencyName, if ref:AdditionalDescription \naction: 0 and 1 \ncomment:')
    #geographic area    
    #one-line description
    #description
    #date of founding
    #date of dissolution
    #image
    #contact detail      
    #external links