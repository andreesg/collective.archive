#!/usr/bin/python
# -*- coding: utf-8 -*-

from zope import schema
from zope.interface import Interface
from collective.archive import MessageFactory as _
from ..utils.vocabularies import _createPriorityVocabulary, _createInsuranceTypeVocabulary
from zope.schema.vocabulary import SimpleTerm, SimpleVocabulary

priority_vocabulary = SimpleVocabulary(list(_createPriorityVocabulary()))
insurance_type_vocabulary = SimpleVocabulary(list(_createInsuranceTypeVocabulary()))

class ListField(schema.List):
    """We need to have a unique class for the field list so that we
    can apply a custom adapter."""
    pass

# # # # # # # # # # # # #
# Widget interface      #
# # # # # # # # # # # # #

class IFormWidget(Interface):
    pass


# # # # # # # # # # # # # #
# DataGrid interfaces     # 
# # # # # # # # # # # # # #

## Archive details

class IClass(Interface):
    term = schema.TextLine(title=_(u'Class'), required=False)

class IEditorialForm(Interface):
    term = schema.TextLine(title=_(u"Editorial form"), required=False)

class IDevelopmentPhase(Interface):
    term = schema.TextLine(title=_(u"Development phase"), required=False)

class ISender(Interface):
    term = schema.TextLine(title=_(u"Sender"), required=False)

class IDateExact(Interface):
    term = schema.TextLine(title=_(u"Date (exact)"), required=False)

class IContent(Interface):
    term = schema.TextLine(title=_(u"Content"), required=False)

class IKeyword(Interface):
    term = schema.TextLine(title=_(u"Keyword"), required=False)

class INotes(Interface):
    term = schema.TextLine(title=_(u"Notes"), required=False)

## Linked Objects
class ILinkedObjects(Interface):
    objectNumber = schema.TextLine(title=_(u'Object number'), required=False)
    creator = schema.TextLine(title=_(u'Creator'), required=False)
    objectName = schema.TextLine(title=_(u'Object name'), required=False)
    title = schema.TextLine(title=_(u'Title'), required=False)



