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


class FinvoiceReceiverInfoSub(supermod.FinvoiceReceiverInfo):
    def __init__(self, Version=None, MessageDetails=None, SellerPartyDetails=None, SellerOrganisationUnitNumber=None, InvoiceSenderInformationDetails=None, SellerAccountDetails=None, SellerInvoiceDetails=None, ReceiverInfoTimeStamp=None, BuyerPartyDetails=None, InvoiceRecipientDetails=None, ProposedDueDate=None, ProposedInvoicePeriod=None, BuyerServiceCode=None, ConversionDetails=None):
        super(FinvoiceReceiverInfoSub, self).__init__(Version, MessageDetails, SellerPartyDetails, SellerOrganisationUnitNumber, InvoiceSenderInformationDetails, SellerAccountDetails, SellerInvoiceDetails, ReceiverInfoTimeStamp, BuyerPartyDetails, InvoiceRecipientDetails, ProposedDueDate, ProposedInvoicePeriod, BuyerServiceCode, ConversionDetails, )
supermod.FinvoiceReceiverInfo.subclass = FinvoiceReceiverInfoSub
# end class FinvoiceReceiverInfoSub


class BuyerPartyDetailsTypeSub(supermod.BuyerPartyDetailsType):
    def __init__(self, BuyerPartyIdentifier=None, BuyerOrganisationName=None, BuyerPostalAddressDetails=None):
        super(BuyerPartyDetailsTypeSub, self).__init__(BuyerPartyIdentifier, BuyerOrganisationName, BuyerPostalAddressDetails, )
supermod.BuyerPartyDetailsType.subclass = BuyerPartyDetailsTypeSub
# end class BuyerPartyDetailsTypeSub


class BuyerPostalAddressDetailsTypeSub(supermod.BuyerPostalAddressDetailsType):
    def __init__(self, BuyerStreetName=None, BuyerTownName=None, BuyerPostCodeIdentifier=None, CountryCode=None, CountryName=None, BuyerPostOfficeBoxIdentifier=None):
        super(BuyerPostalAddressDetailsTypeSub, self).__init__(BuyerStreetName, BuyerTownName, BuyerPostCodeIdentifier, CountryCode, CountryName, BuyerPostOfficeBoxIdentifier, )
supermod.BuyerPostalAddressDetailsType.subclass = BuyerPostalAddressDetailsTypeSub
# end class BuyerPostalAddressDetailsTypeSub


class ConversionDetailsTypeSub(supermod.ConversionDetailsType):
    def __init__(self, ConversionID=None):
        super(ConversionDetailsTypeSub, self).__init__(ConversionID, )
supermod.ConversionDetailsType.subclass = ConversionDetailsTypeSub
# end class ConversionDetailsTypeSub


class InvoiceRecipientDetailsTypeSub(supermod.InvoiceRecipientDetailsType):
    def __init__(self, InvoiceRecipientAddress=None, InvoiceRecipientIntermediatorAddress=None, SellerInvoiceIdentifier=None, EpiRemittanceIdentifier=None, InvoiceRecipientLanguageCode=None):
        super(InvoiceRecipientDetailsTypeSub, self).__init__(InvoiceRecipientAddress, InvoiceRecipientIntermediatorAddress, SellerInvoiceIdentifier, EpiRemittanceIdentifier, InvoiceRecipientLanguageCode, )
supermod.InvoiceRecipientDetailsType.subclass = InvoiceRecipientDetailsTypeSub
# end class InvoiceRecipientDetailsTypeSub


class InvoiceSenderInformationDetailsTypeSub(supermod.InvoiceSenderInformationDetailsType):
    def __init__(self, SellerWebaddressNameText=None, SellerWebaddressText=None, InvoiceSenderAddress=None, InvoiceSenderIntermediatorAddress=None):
        super(InvoiceSenderInformationDetailsTypeSub, self).__init__(SellerWebaddressNameText, SellerWebaddressText, InvoiceSenderAddress, InvoiceSenderIntermediatorAddress, )
supermod.InvoiceSenderInformationDetailsType.subclass = InvoiceSenderInformationDetailsTypeSub
# end class InvoiceSenderInformationDetailsTypeSub


class MessageDetailsTypeSub(supermod.MessageDetailsType):
    def __init__(self, MessageTypeCode=None, MessageTypeText=None, MessageActionCode=None, MessageActionCodeIdentifier=None, MessageDate=None, SenderInfoIdentifier=None):
        super(MessageDetailsTypeSub, self).__init__(MessageTypeCode, MessageTypeText, MessageActionCode, MessageActionCodeIdentifier, MessageDate, SenderInfoIdentifier, )
supermod.MessageDetailsType.subclass = MessageDetailsTypeSub
# end class MessageDetailsTypeSub


class SellerAccountDetailsTypeSub(supermod.SellerAccountDetailsType):
    def __init__(self, SellerAccountID=None, SellerBic=None):
        super(SellerAccountDetailsTypeSub, self).__init__(SellerAccountID, SellerBic, )
supermod.SellerAccountDetailsType.subclass = SellerAccountDetailsTypeSub
# end class SellerAccountDetailsTypeSub


class SellerAccountIDTypeSub(supermod.SellerAccountIDType):
    def __init__(self, IdentificationSchemeName=None, valueOf_=None, extensiontype_=None):
        super(SellerAccountIDTypeSub, self).__init__(IdentificationSchemeName, valueOf_, extensiontype_, )
supermod.SellerAccountIDType.subclass = SellerAccountIDTypeSub
# end class SellerAccountIDTypeSub


class SellerBicTypeSub(supermod.SellerBicType):
    def __init__(self, IdentificationSchemeName=None, valueOf_=None, extensiontype_=None):
        super(SellerBicTypeSub, self).__init__(IdentificationSchemeName, valueOf_, extensiontype_, )
supermod.SellerBicType.subclass = SellerBicTypeSub
# end class SellerBicTypeSub


class SellerInvoiceDetailsTypeSub(supermod.SellerInvoiceDetailsType):
    def __init__(self, SellerDirectDebitIdentifier=None, PaymentInstructionIdentifier=None, SellerInstructionFreeText=None, SellerInvoiceTypeDetails=None):
        super(SellerInvoiceDetailsTypeSub, self).__init__(SellerDirectDebitIdentifier, PaymentInstructionIdentifier, SellerInstructionFreeText, SellerInvoiceTypeDetails, )
supermod.SellerInvoiceDetailsType.subclass = SellerInvoiceDetailsTypeSub
# end class SellerInvoiceDetailsTypeSub


class SellerPartyDetailsTypeSub(supermod.SellerPartyDetailsType):
    def __init__(self, SellerPartyIdentifier=None, SellerOrganisationNames=None, SellerOrganisationBankName=None, SellerPostalAddressDetails=None):
        super(SellerPartyDetailsTypeSub, self).__init__(SellerPartyIdentifier, SellerOrganisationNames, SellerOrganisationBankName, SellerPostalAddressDetails, )
supermod.SellerPartyDetailsType.subclass = SellerPartyDetailsTypeSub
# end class SellerPartyDetailsTypeSub


class SellerOrganisationNamesTypeSub(supermod.SellerOrganisationNamesType):
    def __init__(self, LanguageCode=None, SellerOrganisationName=None):
        super(SellerOrganisationNamesTypeSub, self).__init__(LanguageCode, SellerOrganisationName, )
supermod.SellerOrganisationNamesType.subclass = SellerOrganisationNamesTypeSub
# end class SellerOrganisationNamesTypeSub


class SellerPostalAddressDetailsTypeSub(supermod.SellerPostalAddressDetailsType):
    def __init__(self, SellerStreetName=None, SellerTownName=None, SellerPostCodeIdentifier=None, CountryCode=None, CountryName=None, SellerPostOfficeBoxIdentifier=None):
        super(SellerPostalAddressDetailsTypeSub, self).__init__(SellerStreetName, SellerTownName, SellerPostCodeIdentifier, CountryCode, CountryName, SellerPostOfficeBoxIdentifier, )
supermod.SellerPostalAddressDetailsType.subclass = SellerPostalAddressDetailsTypeSub
# end class SellerPostalAddressDetailsTypeSub


class dateSub(supermod.date):
    def __init__(self, Format=None, valueOf_=None):
        super(dateSub, self).__init__(Format, valueOf_, )
supermod.date.subclass = dateSub
# end class dateSub


class TextLanguageOptionalSub(supermod.TextLanguageOptional):
    def __init__(self, LanguageCode=None, valueOf_=None, extensiontype_=None):
        super(TextLanguageOptionalSub, self).__init__(LanguageCode, valueOf_, extensiontype_, )
supermod.TextLanguageOptional.subclass = TextLanguageOptionalSub
# end class TextLanguageOptionalSub


class TextLanguageRequiredSub(supermod.TextLanguageRequired):
    def __init__(self, LanguageCode=None, valueOf_=None, extensiontype_=None):
        super(TextLanguageRequiredSub, self).__init__(LanguageCode, valueOf_, extensiontype_, )
supermod.TextLanguageRequired.subclass = TextLanguageRequiredSub
# end class TextLanguageRequiredSub


class SellerInvoiceIdentifierTypeSub(supermod.SellerInvoiceIdentifierType):
    def __init__(self, SellerInvoiceIdentifierType=None, valueOf_=None):
        super(SellerInvoiceIdentifierTypeSub, self).__init__(SellerInvoiceIdentifierType, valueOf_, )
supermod.SellerInvoiceIdentifierType.subclass = SellerInvoiceIdentifierTypeSub
# end class SellerInvoiceIdentifierTypeSub


class SellerAccountIDType1Sub(supermod.SellerAccountIDType1):
    def __init__(self, IdentificationSchemeName=None, valueOf_=None):
        super(SellerAccountIDType1Sub, self).__init__(IdentificationSchemeName, valueOf_, )
supermod.SellerAccountIDType1.subclass = SellerAccountIDType1Sub
# end class SellerAccountIDType1Sub


class SellerBicType2Sub(supermod.SellerBicType2):
    def __init__(self, IdentificationSchemeName=None, valueOf_=None):
        super(SellerBicType2Sub, self).__init__(IdentificationSchemeName, valueOf_, )
supermod.SellerBicType2.subclass = SellerBicType2Sub
# end class SellerBicType2Sub


class SellerInstructionFreeTextTypeSub(supermod.SellerInstructionFreeTextType):
    def __init__(self, LanguageCode=None, valueOf_=None):
        super(SellerInstructionFreeTextTypeSub, self).__init__(LanguageCode, valueOf_, )
supermod.SellerInstructionFreeTextType.subclass = SellerInstructionFreeTextTypeSub
# end class SellerInstructionFreeTextTypeSub


class SellerInvoiceTypeDetailsTypeSub(supermod.SellerInvoiceTypeDetailsType):
    def __init__(self, SellerInvoiceTypeText=None, SellerInvoiceIdentifierText=None):
        super(SellerInvoiceTypeDetailsTypeSub, self).__init__(SellerInvoiceTypeText, SellerInvoiceIdentifierText, )
supermod.SellerInvoiceTypeDetailsType.subclass = SellerInvoiceTypeDetailsTypeSub
# end class SellerInvoiceTypeDetailsTypeSub


class SellerInvoiceTypeTextTypeSub(supermod.SellerInvoiceTypeTextType):
    def __init__(self, LanguageCode=None, valueOf_=None):
        super(SellerInvoiceTypeTextTypeSub, self).__init__(LanguageCode, valueOf_, )
supermod.SellerInvoiceTypeTextType.subclass = SellerInvoiceTypeTextTypeSub
# end class SellerInvoiceTypeTextTypeSub


class SellerInvoiceIdentifierTextTypeSub(supermod.SellerInvoiceIdentifierTextType):
    def __init__(self, LanguageCode=None, SellerInvoiceIdentifierType=None, SellerInvoiceIdentifierMinLength=1, SellerInvoiceIdentifierHyphens=False, SellerInvoiceIdentifierSpaces=False, SellerInvoiceIdentifierMaxLength=35, valueOf_=None, extensiontype_=None):
        super(SellerInvoiceIdentifierTextTypeSub, self).__init__(LanguageCode, SellerInvoiceIdentifierType, SellerInvoiceIdentifierMinLength, SellerInvoiceIdentifierHyphens, SellerInvoiceIdentifierSpaces, SellerInvoiceIdentifierMaxLength, valueOf_, extensiontype_, )
supermod.SellerInvoiceIdentifierTextType.subclass = SellerInvoiceIdentifierTextTypeSub
# end class SellerInvoiceIdentifierTextTypeSub


class SellerInvoiceIdentifierTextType3Sub(supermod.SellerInvoiceIdentifierTextType3):
    def __init__(self, LanguageCode=None, SellerInvoiceIdentifierType=None, SellerInvoiceIdentifierMinLength=1, SellerInvoiceIdentifierHyphens=False, SellerInvoiceIdentifierSpaces=False, SellerInvoiceIdentifierMaxLength=35, valueOf_=None):
        super(SellerInvoiceIdentifierTextType3Sub, self).__init__(LanguageCode, SellerInvoiceIdentifierType, SellerInvoiceIdentifierMinLength, SellerInvoiceIdentifierHyphens, SellerInvoiceIdentifierSpaces, SellerInvoiceIdentifierMaxLength, valueOf_, )
supermod.SellerInvoiceIdentifierTextType3.subclass = SellerInvoiceIdentifierTextType3Sub
# end class SellerInvoiceIdentifierTextType3Sub


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
        rootTag = 'FinvoiceReceiverInfo'
        rootClass = supermod.FinvoiceReceiverInfo
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
        rootTag = 'FinvoiceReceiverInfo'
        rootClass = supermod.FinvoiceReceiverInfo
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
        rootTag = 'FinvoiceReceiverInfo'
        rootClass = supermod.FinvoiceReceiverInfo
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
        rootTag = 'FinvoiceReceiverInfo'
        rootClass = supermod.FinvoiceReceiverInfo
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
