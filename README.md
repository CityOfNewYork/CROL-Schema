# City Record Online Workgroup (CROW) - Schema

This is the main repository containing efforts pertaining to the schema development of CROW. For parsing libraries, see https://github.com/CityOfNewYork/CROL-Parsing. 

Disclaimer. In case of conflicting document versions, please refer to documents mentioned in GitHub as the latest version.


##Goal 

Create a  notice data standard that is optimized for public consumption.


##Deliverables
* JSON Schema to validate against

* Sample JSON-LD for different types of notices and attributes

* Hosted JSON-LD context framework (e.g. @types + @ids)

* ‘Read the Docs’-Documentation


##Schema Requirements

* ‘standardized’: it brings established data standards (e.g. schema.org, open-contracting) into a new and single consistent whole
* ‘structured’: it breaks down the content of notices to maximize the possible use cases and services (e.g. notifications) for the public 
* ‘transferrable’:  it is flexible enough to address different local contexts’ specific needs
* ‘designed for public consumption”: it is optimized for public access and usablity



#Proposed Structure


####JSON-LD
Each notice is stored as a JSON-LD document. Fully JSON based and compatible, JSON-LD is a lightweight Linked Data format. It is easy for humans to read and write, and provides a way to help JSON data interoperate at Web-scale. It is adopted by Google, Yahoo, Yandex, and Microsoft, and will provide the data with an off-the shelf integration to existing web apps as well as mapping by the major search engines of the city record data. Hence, The key project goals of “structuring” and “standardizing” will be achieved by adapting JSON-LD and established object structures from sources like schema.org and thepopoloproject.com.


####JSON Schema

We use JSON Schema to describe the data format in a clear, human- and machine-readable documentation. It provides complete structural validation, useful for automated testing as well as validating client-submitted data


###Schema Structure
The current proposed schema (in JSON-LD ) is built up by
(a) notice skeleton (fields that are shared by all notice types), 
(b) attributes (recursive and standardized objects such places, events, documents, organizations), and
(c) sub-configurations (the set of notice-type specific fields, belonging, for instance, to all solicitations, or court notices). 
Skeleton




####Skeleton

Section              Link                          | Status                   |   Impl. Phase 
--------------|------------------------------------|--------------------------|--------------------
Skeleton      | [Sample](http://bit.ly/1ESeoeI)    |       Draft              |   1




####Attributes

Attributes              Link                       | Status                   |   Impl. Phase 
--------------|------------------------------------|--------------------------|--------------------
Place         | [Sample](http://bit.ly/1ESeoeI)    |        Draft             |   1
Event         | [Sample](http://bit.ly/1ESeoeI)    |        Draft             |   1
Document      | [Sample](http://bit.ly/1ESeoeI)    |        Draft             |   1
Organization  | [Sample](http://bit.ly/1ESeoeI)    |        Draft             |   1
Person        | [Sample](http://bit.ly/1ESeoeI)    |        Draft             |   1
Agenda Items  | [Sample](http://bit.ly/1ESeoeI)    |        Draft             |   2
Links/Urls    | [Sample](http://bit.ly/1ESeoeI)    |        Draft             |   1


NB. There are also a set of "system specific" objects such as (section, sub section) that needs to be mapped out. See [Sample](http://bit.ly/1ESeoeI) 



####Configurations


Configurations              Link                               | Status                              |   Impl. Phase 
--------------------------|------------------------------------|-------------------------------------|--------------------
Public Hearing            | [Sample](http://bit.ly/1ESeoeI)    |          Draft                      |   1
Procurement               |  Not yet available                 |          Not finalized              |   1
Property Displostion      |  Not yet available                 |          Not finalized              |   2
Court notices             |  Not yet available                 |          Not finalized              |   2
Rule Details              |  Not yet available                 |          Not finalized              |   2
Personell Announcements   |  Not yet available                 |          Not finalized              |   2
Other identified types    |  Not yet available                 |          Not finalized              |   2


#To Do's

[See Milestones]

