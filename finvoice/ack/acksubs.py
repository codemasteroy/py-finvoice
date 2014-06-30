#!/usr/bin/env python

###
# Copyright 2014 Code Master Oy (http://www.codemaster.fi/)
#
# This file is part of py-finvoice.
#
# py-finvoice is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
# 
# py-finvoice is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with py-finvoice. If not, see <http://www.gnu.org/licenses/>.
##

import sys

import finvoice as supermod

etree_ = None
Verbose_import_ = False
(
    XMLParser_import_none, XMLParser_import_lxml,
    XMLParser_import_elementtree
) = range(3)
XMLParser_import_library = None
try:
    # lxml
    from lxml import etree as etree_
    XMLParser_import_library = XMLParser_import_lxml
    if Verbose_import_:
        print("running with lxml.etree")
except ImportError:
    try:
        # cElementTree from Python 2.5+
        import xml.etree.cElementTree as etree_
        XMLParser_import_library = XMLParser_import_elementtree
        if Verbose_import_:
            print("running with cElementTree on Python 2.5+")
    except ImportError:
        try:
            # ElementTree from Python 2.5+
            import xml.etree.ElementTree as etree_
            XMLParser_import_library = XMLParser_import_elementtree
            if Verbose_import_:
                print("running with ElementTree on Python 2.5+")
        except ImportError:
            try:
                # normal cElementTree install
                import cElementTree as etree_
                XMLParser_import_library = XMLParser_import_elementtree
                if Verbose_import_:
                    print("running with cElementTree")
            except ImportError:
                try:
                    # normal ElementTree install
                    import elementtree.ElementTree as etree_
                    XMLParser_import_library = XMLParser_import_elementtree
                    if Verbose_import_:
                        print("running with ElementTree")
                except ImportError:
                    raise ImportError(
                        "Failed to import ElementTree from any known place")


def parsexml_(*args, **kwargs):
    if (XMLParser_import_library == XMLParser_import_lxml and
            'parser' not in kwargs):
        # Use the lxml ElementTree compatible parser so that, e.g.,
        #   we ignore comments.
        kwargs['parser'] = etree_.ETCompatXMLParser()
    doc = etree_.parse(*args, **kwargs)
    return doc

#
# Globals
#

ExternalEncoding = 'ascii'

#
# Data representation classes
#


class FinvoiceackSub(supermod.Finvoiceack):
    def __init__(self, Version=None, Acknowledgement=None, RefToCounterpartMessage=None, MessageTransmissionDetails=None, Error=None):
        super(FinvoiceackSub, self).__init__(Version, Acknowledgement, RefToCounterpartMessage, MessageTransmissionDetails, Error, )
supermod.Finvoiceack.subclass = FinvoiceackSub
# end class FinvoiceackSub


class MessageDataSub(supermod.MessageData):
    def __init__(self, MessageId=None, Timestamp=None):
        super(MessageDataSub, self).__init__(MessageId, Timestamp, )
supermod.MessageData.subclass = MessageDataSub
# end class MessageDataSub


class ReasonSub(supermod.Reason):
    def __init__(self, Code=None, Text=None):
        super(ReasonSub, self).__init__(Code, Text, )
supermod.Reason.subclass = ReasonSub
# end class ReasonSub


class MessageTransmissionDetailsTypeSub(supermod.MessageTransmissionDetailsType):
    def __init__(self, MessageSenderDetails=None, MessageReceiverDetails=None, MessageDetails=None):
        super(MessageTransmissionDetailsTypeSub, self).__init__(MessageSenderDetails, MessageReceiverDetails, MessageDetails, )
supermod.MessageTransmissionDetailsType.subclass = MessageTransmissionDetailsTypeSub
# end class MessageTransmissionDetailsTypeSub


class ErrorTypeSub(supermod.ErrorType):
    def __init__(self, Code=None, Text=None, Severity=None, Location=None):
        super(ErrorTypeSub, self).__init__(Code, Text, Severity, Location, )
supermod.ErrorType.subclass = ErrorTypeSub
# end class ErrorTypeSub


class ToSub(supermod.To):
    def __init__(self, PartyId=None, Role=None):
        super(ToSub, self).__init__(PartyId, Role, )
supermod.To.subclass = ToSub
# end class ToSub


class FromSub(supermod.From):
    def __init__(self, PartyId=None, Role=None):
        super(FromSub, self).__init__(PartyId, Role, )
supermod.From.subclass = FromSub
# end class FromSub


class AcknowledgementTypeSub(supermod.AcknowledgementType):
    def __init__(self, From=None, To=None, MessageData=None, Reason=None):
        super(AcknowledgementTypeSub, self).__init__(From, To, MessageData, Reason, )
supermod.AcknowledgementType.subclass = AcknowledgementTypeSub
# end class AcknowledgementTypeSub


class MessageSenderDetailsTypeSub(supermod.MessageSenderDetailsType):
    def __init__(self, FromIdentifier=None, FromIntermediator=None):
        super(MessageSenderDetailsTypeSub, self).__init__(FromIdentifier, FromIntermediator, )
supermod.MessageSenderDetailsType.subclass = MessageSenderDetailsTypeSub
# end class MessageSenderDetailsTypeSub


class MessageReceiverDetailsTypeSub(supermod.MessageReceiverDetailsType):
    def __init__(self, ToIdentifier=None, ToIntermediator=None):
        super(MessageReceiverDetailsTypeSub, self).__init__(ToIdentifier, ToIntermediator, )
supermod.MessageReceiverDetailsType.subclass = MessageReceiverDetailsTypeSub
# end class MessageReceiverDetailsTypeSub


class MessageDetailsTypeSub(supermod.MessageDetailsType):
    def __init__(self, MessageIdentifier=None, MessageTimeStamp=None, RefToMessageIdentifier=None):
        super(MessageDetailsTypeSub, self).__init__(MessageIdentifier, MessageTimeStamp, RefToMessageIdentifier, )
supermod.MessageDetailsType.subclass = MessageDetailsTypeSub
# end class MessageDetailsTypeSub


def get_root_tag(node):
    tag = supermod.Tag_pattern_.match(node.tag).groups()[-1]
    rootClass = None
    rootClass = supermod.GDSClassesMapping.get(tag)
    if rootClass is None and hasattr(supermod, tag):
        rootClass = getattr(supermod, tag)
    return tag, rootClass


def parse(inFilename, silence=False):
    doc = parsexml_(inFilename)
    rootNode = doc.getroot()
    rootTag, rootClass = get_root_tag(rootNode)
    if rootClass is None:
        rootTag = 'Finvoiceack'
        rootClass = supermod.Finvoiceack
    rootObj = rootClass.factory()
    rootObj.build(rootNode)
    # Enable Python to collect the space used by the DOM.
    doc = None
    if not silence:
        sys.stdout.write('<?xml version="1.0" ?>\n')
        rootObj.export(
            sys.stdout, 0, name_=rootTag,
            namespacedef_='',
            pretty_print=True)
    return rootObj


def parseEtree(inFilename, silence=False):
    doc = parsexml_(inFilename)
    rootNode = doc.getroot()
    rootTag, rootClass = get_root_tag(rootNode)
    if rootClass is None:
        rootTag = 'Finvoiceack'
        rootClass = supermod.Finvoiceack
    rootObj = rootClass.factory()
    rootObj.build(rootNode)
    # Enable Python to collect the space used by the DOM.
    doc = None
    mapping = {}
    rootElement = rootObj.to_etree(None, name_=rootTag, mapping_=mapping)
    reverse_mapping = rootObj.gds_reverse_node_mapping(mapping)
    if not silence:
        content = etree_.tostring(
            rootElement, pretty_print=True,
            xml_declaration=True, encoding="utf-8")
        sys.stdout.write(content)
        sys.stdout.write('\n')
    return rootObj, rootElement, mapping, reverse_mapping


def parseString(inString, silence=False):
    from StringIO import StringIO
    doc = parsexml_(StringIO(inString))
    rootNode = doc.getroot()
    rootTag, rootClass = get_root_tag(rootNode)
    if rootClass is None:
        rootTag = 'Finvoiceack'
        rootClass = supermod.Finvoiceack
    rootObj = rootClass.factory()
    rootObj.build(rootNode)
    # Enable Python to collect the space used by the DOM.
    doc = None
    if not silence:
        sys.stdout.write('<?xml version="1.0" ?>\n')
        rootObj.export(
            sys.stdout, 0, name_=rootTag,
            namespacedef_='')
    return rootObj


def parseLiteral(inFilename, silence=False):
    doc = parsexml_(inFilename)
    rootNode = doc.getroot()
    rootTag, rootClass = get_root_tag(rootNode)
    if rootClass is None:
        rootTag = 'Finvoiceack'
        rootClass = supermod.Finvoiceack
    rootObj = rootClass.factory()
    rootObj.build(rootNode)
    # Enable Python to collect the space used by the DOM.
    doc = None
    if not silence:
        sys.stdout.write('#from ??? import *\n\n')
        sys.stdout.write('import ??? as model_\n\n')
        sys.stdout.write('rootObj = model_.rootClass(\n')
        rootObj.exportLiteral(sys.stdout, 0, name_=rootTag)
        sys.stdout.write(')\n')
    return rootObj


USAGE_TEXT = """
Usage: python ???.py <infilename>
"""


def usage():
    print USAGE_TEXT
    sys.exit(1)


def main():
    args = sys.argv[1:]
    if len(args) != 1:
        usage()
    infilename = args[0]
    parse(infilename)


if __name__ == '__main__':
    #import pdb; pdb.set_trace()
    main()
