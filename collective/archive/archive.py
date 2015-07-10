#!/usr/bin/python
# -*- coding: utf-8 -*-

#
# Zope dependencies
#
from zope import schema
from zope.interface import invariant, Invalid, Interface, implements
from zope.interface import alsoProvides
from zope.schema.vocabulary import SimpleVocabulary
from zope.schema.fieldproperty import FieldProperty
from zope.component import getMultiAdapter

#
# Plone dependencies
#
from plone.directives import dexterity, form
from plone.app.textfield import RichText
from plone.namedfile.interfaces import IImageScaleTraversable
from plone.supermodel import model
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile

#
# z3c.forms dependencies
#
from z3c.form import group, field
from z3c.form.form import extends
from z3c.form.browser.textlines import TextLinesFieldWidget

#
# DataGridFields dependencies
#
from collective.z3cform.datagridfield import DataGridFieldFactory, DictRow
from collective.z3cform.datagridfield.blockdatagridfield import BlockDataGridFieldFactory
from z3c.relationfield.schema import RelationChoice
from z3c.relationfield.schema import RelationList
#from plone.formwidget.contenttree import ObjPathSourceBinder
from .utils.source import ObjPathSourceBinder

#
# plone.app.widgets dependencies
#
from plone.app.widgets.dx import DatetimeFieldWidget

# # # # # # # # # # # # # # # 
# Dexterity imports         # 
# # # # # # # # # # # # # # # 
from five import grok
from collective import dexteritytextindexer
from plone.dexterity.browser.view import DefaultView
from plone.dexterity.content import Container
from plone.dexterity.browser import add, edit

# # # # # # # # # # # # # # # # # #
# !Archive specific imports!      #
# # # # # # # # # # # # # # # # # #
from collective.archive import MessageFactory as _
from .utils.vocabularies import *
from .utils.interfaces import *
from .utils.views import *

# # # # # # # # # # # # #
# # # # # # # # # # # # #
# # Archive schema    # #
# # # # # # # # # # # # #
# # # # # # # # # # # # #

class IArchive(form.Schema):

    text = RichText(
        title=_(u"Body"),
        required=False
    )

    priref = schema.TextLine(
        title=_(u'priref'),
        required=False
    )
    dexteritytextindexer.searchable('priref')

    # # # # # # # # # # #
    # Archive details   #
    # # # # # # # # # # #
    model.fieldset('archive_details', label=_(u'Archive details'), 
        fields=['archiveDetails_archiveDetails_archiveNumber','archiveDetails_archiveDetails_preliminaryNumber',
                'archiveDetails_archiveDetails_photoNumber', 'archiveDetails_archiveDetails_class', 
                'archiveDetails_archiveDetails_editorialForm', 'archiveDetails_archiveDetails_physicalForm',
                'archiveDetails_archiveDetails_developmentPhase', 'archiveDetails_archiveDetails_sender',
                'archiveDetails_archiveDetails_receiver', 'archiveDetails_archiveDetails_dateExact',
                'archiveDetails_archiveDetails_dateFree', 'archiveDetails_archiveDetails_content',
                'archiveDetails_archiveDetails_keyword', 'archiveDetails_archiveDetails_notes']
    )

    archiveDetails_archiveDetails_archiveNumber = schema.TextLine(
        title=_(u'Archive number'),
        required=False
    )
    dexteritytextindexer.searchable('archiveDetails_archiveDetails_archiveNumber')

    archiveDetails_archiveDetails_preliminaryNumber = schema.TextLine(
        title=_(u'Preliminary number'),
        required=False
    )
    dexteritytextindexer.searchable('archiveDetails_archiveDetails_preliminaryNumber')

    archiveDetails_archiveDetails_photoNumber = schema.TextLine(
        title=_(u'Photo number'),
        required=False
    )
    dexteritytextindexer.searchable('archiveDetails_archiveDetails_photoNumber')


    archiveDetails_archiveDetails_class = ListField(title=_(u'Class'),
        value_type=DictRow(title=_(u'Class'), schema=IClass),
        required=False)
    form.widget(archiveDetails_archiveDetails_class=BlockDataGridFieldFactory)
    dexteritytextindexer.searchable('archiveDetails_archiveDetails_class')

    archiveDetails_archiveDetails_editorialForm = ListField(title=_(u'Editorial form'),
        value_type=DictRow(title=_(u'Editorial form'), schema=IEditorialForm),
        required=False)
    form.widget(archiveDetails_archiveDetails_editorialForm=BlockDataGridFieldFactory)
    dexteritytextindexer.searchable('archiveDetails_archiveDetails_editorialForm')

    archiveDetails_archiveDetails_physicalForm = schema.TextLine(
        title=_(u'Physical form'),
        required=False
    )
    dexteritytextindexer.searchable('archiveDetails_archiveDetails_physicalForm')

    archiveDetails_archiveDetails_developmentPhase = ListField(title=_(u'Development phase'),
        value_type=DictRow(title=_(u'Development phase'), schema=IDevelopmentPhase),
        required=False)
    form.widget(archiveDetails_archiveDetails_developmentPhase=BlockDataGridFieldFactory)
    dexteritytextindexer.searchable('archiveDetails_archiveDetails_developmentPhase')

    archiveDetails_archiveDetails_sender = ListField(title=_(u'Sender'),
        value_type=DictRow(title=_(u'Sender'), schema=ISender),
        required=False)
    form.widget(archiveDetails_archiveDetails_sender=BlockDataGridFieldFactory)
    dexteritytextindexer.searchable('archiveDetails_archiveDetails_sender')

    archiveDetails_archiveDetails_receiver = schema.TextLine(
        title=_(u'Receiver'),
        required=False
    )
    dexteritytextindexer.searchable('archiveDetails_archiveDetails_receiver')

    archiveDetails_archiveDetails_dateExact = ListField(title=_(u'Date (exact)'),
        value_type=DictRow(title=_(u'Date (exact)'), schema=IDateExact),
        required=False)
    form.widget(archiveDetails_archiveDetails_dateExact=BlockDataGridFieldFactory)
    dexteritytextindexer.searchable('archiveDetails_archiveDetails_dateExact')

    archiveDetails_archiveDetails_dateFree = schema.TextLine(
        title=_(u'Date (free)'),
        required=False
    )
    dexteritytextindexer.searchable('archiveDetails_archiveDetails_dateFree')

    archiveDetails_archiveDetails_content = ListField(title=_(u'Content'),
        value_type=DictRow(title=_(u'Content'), schema=IContent),
        required=False)
    form.widget(archiveDetails_archiveDetails_content=BlockDataGridFieldFactory)
    dexteritytextindexer.searchable('archiveDetails_archiveDetails_content')
    
    archiveDetails_archiveDetails_keyword = ListField(title=_(u'Keyword'),
        value_type=DictRow(title=_(u'Keyword'), schema=IKeyword),
        required=False)
    form.widget(archiveDetails_archiveDetails_keyword=BlockDataGridFieldFactory)
    dexteritytextindexer.searchable('archiveDetails_archiveDetails_keyword')

    archiveDetails_archiveDetails_notes = ListField(title=_(u'Notes'),
        value_type=DictRow(title=_(u'Notes'), schema=INotes),
        required=False)
    form.widget(archiveDetails_archiveDetails_notes=BlockDataGridFieldFactory)
    dexteritytextindexer.searchable('archiveDetails_archiveDetails_notes')
    

    # # # # # # # # # # #
    # Linked objects    #
    # # # # # # # # # # #
    model.fieldset('linked_objects', label=_(u'Linked Objects'), 
        fields=['linkedObjects_linkedObjects', 'linkedObjects_relatedObjects']
    )

    linkedObjects_relatedObjects = RelationList(
        title=_(u'Linked Objects'),
        default=[],
        value_type=RelationChoice(
            title=u"Related",
            source=ObjPathSourceBinder()
        ),
        required=False
    )

    linkedObjects_linkedObjects = ListField(title=_(u'Linked Objects'),
        value_type=DictRow(title=_(u'Linked Objects'), schema=ILinkedObjects),
        required=False)
    form.widget(linkedObjects_linkedObjects=DataGridFieldFactory)
    dexteritytextindexer.searchable('linkedObjects_linkedObjects')


# # # # # # # # # # # # # #
# Archive declaration     #
# # # # # # # # # # # # # #

class Archive(Container):
    grok.implements(IArchive)
    pass

# # # # # # # # # # # # # # # # 
# Archive add/edit views      # 
# # # # # # # # # # # # # # # #

class AddForm(add.DefaultAddForm):
    template = ViewPageTemplateFile('archive_templates/add.pt')
    def update(self):
        super(AddForm, self).update()
        for group in self.groups:
            for widget in group.widgets.values():
                alsoProvides(widget, IFormWidget)

class AddView(add.DefaultAddView):
    form = AddForm
    

class EditForm(edit.DefaultEditForm):
    template = ViewPageTemplateFile('archive_templates/edit.pt')
    
    def update(self):
        super(EditForm, self).update()
        for group in self.groups:
            for widget in group.widgets.values():
                alsoProvides(widget, IFormWidget)

