#!/usr/bin/env python
# -*- mode: pymode; coding: latin1; -*-

import sys
import re

#
# You must include the following class definition at the top of
#   your method specification file.
#
class MethodSpec(object):
    def __init__(self, name='', source='', class_names='',
            class_names_compiled=None):
        """MethodSpec -- A specification of a method.
        Member variables:
            name -- The method name
            source -- The source code for the method.  Must be
                indented to fit in a class definition.
            class_names -- A regular expression that must match the
                class names in which the method is to be inserted.
            class_names_compiled -- The compiled class names.
                generateDS.py will do this compile for you.
        """
        self.name = name
        self.source = source
        if class_names is None:
            self.class_names = ('.*', )
        else:
            self.class_names = class_names
        if class_names_compiled is None:
            self.class_names_compiled = re.compile(self.class_names)
        else:
            self.class_names_compiled = class_names_compiled
    def get_name(self):
        return self.name
    def set_name(self, name):
        self.name = name
    def get_source(self):
        return self.source
    def set_source(self, source):
        self.source = source
    def get_class_names(self):
        return self.class_names
    def set_class_names(self, class_names):
        self.class_names = class_names
        self.class_names_compiled = re.compile(class_names)
    def get_class_names_compiled(self):
        return self.class_names_compiled
    def set_class_names_compiled(self, class_names_compiled):
        self.class_names_compiled = class_names_compiled
    def match_name(self, class_name):
        """Match against the name of the class currently being generated.
        If this method returns True, the method will be inserted in
          the generated class.
        """
        if self.class_names_compiled.search(class_name):
            return True
        else:
            return False
    def get_interpolated_source(self, values_dict):
        """Get the method source code, interpolating values from values_dict
        into it.  The source returned by this method is inserted into
        the generated class.
        """
        source = self.source % values_dict
        return source
    def show(self):
        print 'specification:'
        print '    name: %s' % (self.name, )
        print self.source
        print '    class_names: %s' % (self.class_names, )
        print '    names pat  : %s' % (self.class_names_compiled.pattern, )


#
# Provide one or more method specification such as the following.
# Notes:
# - Each generated class contains a class variable _member_data_items.
#   This variable contains a list of instances of class _MemberSpec.
#   See the definition of class _MemberSpec near the top of the
#   generated superclass file and also section "User Methods" in
#   the documentation, as well as the examples below.

#
# Replace the following method specifications with your own.

method10 = MethodSpec(name='validate_valueOf_',
    source='''\
    def validate_valueOf_(self, value):
        if ( isinstance( value, basestring ) and value.__len__() <= 35 ):
            pass
        else:
            raise_value_error( value, 'Expected less than 35 characters' )
        return value
''',
    class_names=r'^SellerAccountIDType|SellerAccountIDType2$',
    )

method20 = MethodSpec(name='build',
    source='''\
    def build(self, node):
        already_processed = set()
        self.buildAttributes(node, node.attrib, already_processed)
        self.valueOf_ = get_all_text_(node)
        self.validate_valueOf_(self.valueOf_)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_)
        return self
''',
    class_names=r'^SellerAccountIDType|SellerAccountIDType2$',
    )

method30 = MethodSpec(name='validate_IdentificationSchemeName',
    source='''\
    def validate_IdentificationSchemeName(self, value):
        if ( value == "IBAN" ):
            pass
        else:
            raise_value_error( value, 'Expected "IBAN"' )
        return value
''',
    class_names=r'^SellerAccountIDType|SellerAccountIDType2$',
    )

method40 = MethodSpec(name='buildAttributes',
    source='''\
    def buildAttributes(self, node, attrs, already_processed):
        value = find_attr_value_('IdentificationSchemeName', node)
        if value is not None and 'IdentificationSchemeName' not in already_processed:
            already_processed.add('IdentificationSchemeName')
            self.IdentificationSchemeName = value
            self.validate_IdentificationSchemeName(self.IdentificationSchemeName)
        value = find_attr_value_('xsi:type', node)
        if value is not None and 'xsi:type' not in already_processed:
            already_processed.add('xsi:type')
            self.extensiontype_ = value
''',
    class_names=r'^SellerAccountIDType|SellerAccountIDType2$',
    )

method50 = MethodSpec(name='validate_valueOf_',
    source='''\
    def validate_valueOf_(self, value):
        if ( isinstance( value, basestring ) and 8 <= value.__len__() <= 11 ):
            pass
        else:
            raise_value_error( value, 'Expected value between 8..11 characters' )
        return value
''',
    class_names=r'^SellerBicType|SellerBicType2$',
    )

method60 = MethodSpec(name='build',
    source='''\
    def build(self, node):
        already_processed = set()
        self.buildAttributes(node, node.attrib, already_processed)
        self.valueOf_ = get_all_text_(node)
        self.validate_valueOf_(self.valueOf_)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_)
        return self
''',
    class_names=r'^SellerBicType|SellerBicType2$',
    )

method70 = MethodSpec(name='validate_IdentificationSchemeName',
    source='''\
    def validate_IdentificationSchemeName(self, value):
        if ( value == "BIC" ):
            pass
        else:
            raise_value_error( value, 'Expected "BIC"' )
        return value
''',
    class_names=r'^SellerBicType|SellerBicType2$',
    )

method80 = MethodSpec(name='buildAttributes',
    source='''\
    def buildAttributes(self, node, attrs, already_processed):
        value = find_attr_value_('IdentificationSchemeName', node)
        if value is not None and 'IdentificationSchemeName' not in already_processed:
            already_processed.add('IdentificationSchemeName')
            self.IdentificationSchemeName = value
            self.validate_IdentificationSchemeName(self.IdentificationSchemeName)
        value = find_attr_value_('xsi:type', node)
        if value is not None and 'xsi:type' not in already_processed:
            already_processed.add('xsi:type')
            self.extensiontype_ = value
''',
    class_names=r'^SellerBicType|SellerBicType2$',
    )

method90 = MethodSpec(name='validate_SellerInstructionFreeTextType',
    source='''\
    def validate_SellerInstructionFreeTextType(self, value):
        if ( value.__len__() <= 3 ):
            pass
        else:
            raise_value_error( value.__len__(), 'Expected maximum of 3 elements' )
        return value
''',
    class_names=r'^SellerInvoiceDetailsType$',
    )

method91 = MethodSpec(name='validate_SellerInvoiceTypeDetailsType',
    source='''\
    def validate_SellerInvoiceTypeDetailsType(self, value):
        if ( value.__len__() <= 3 ):
            pass
        else:
            raise_value_error( value.__len__(), 'Expected maximum of 3 elements' )
        return value
''',
    class_names=r'^SellerInvoiceDetailsType$',
    )

method100 = MethodSpec(name='buildChildren',
    source='''\
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        if nodeName_ == 'SellerDirectDebitIdentifier':
            SellerDirectDebitIdentifier_ = child_.text
            SellerDirectDebitIdentifier_ = self.gds_validate_string(SellerDirectDebitIdentifier_, node, 'SellerDirectDebitIdentifier')
            self.SellerDirectDebitIdentifier = SellerDirectDebitIdentifier_
            self.validate_genericStringType0_35(self.SellerDirectDebitIdentifier)    # validate type genericStringType0_35
        elif nodeName_ == 'PaymentInstructionIdentifier':
            PaymentInstructionIdentifier_ = child_.text
            PaymentInstructionIdentifier_ = self.gds_validate_string(PaymentInstructionIdentifier_, node, 'PaymentInstructionIdentifier')
            self.PaymentInstructionIdentifier = PaymentInstructionIdentifier_
            self.validate_genericStringType1_35(self.PaymentInstructionIdentifier)    # validate type genericStringType1_35
        elif nodeName_ == 'SellerInstructionFreeText':
            obj_ = SellerInstructionFreeTextType.factory()
            obj_.build(child_)
            self.SellerInstructionFreeText.append(obj_)
            self.validate_SellerInstructionFreeTextType(self.SellerInstructionFreeText)
            obj_.original_tagname_ = 'SellerInstructionFreeText'
        elif nodeName_ == 'SellerInvoiceTypeDetails':
            obj_ = SellerInvoiceTypeDetailsType.factory()
            obj_.build(child_)
            self.SellerInvoiceTypeDetails.append(obj_)
            self.validate_SellerInvoiceTypeDetailsType(self.SellerInvoiceTypeDetails)
            obj_.original_tagname_ = 'SellerInvoiceTypeDetails'
        elif nodeName_ == 'SellerServiceCode':
            SellerServiceCode_ = child_.text
            SellerServiceCode_ = self.gds_validate_string(SellerServiceCode_, node, 'SellerServiceCode')
            self.SellerServiceCode = SellerServiceCode_
            self.validate_SellerServiceCodeType(self.SellerServiceCode)    # validate type SellerServiceCodeType
''',
    class_names=r'^SellerInvoiceDetailsType$',
    )

method110 = MethodSpec(name='validate_valueOf_',
    source='''\
    def validate_valueOf_(self, value):
        if ( isinstance( value, basestring ) and 1 <= value.__len__() <= 420 ):
            pass
        else:
            raise_value_error( value, 'Expected value between 1..420 characters' )
        return value
''',
    class_names=r'^SellerInstructionFreeTextType$',
    )

method120 = MethodSpec(name='build',
    source='''\
    def build(self, node):
        already_processed = set()
        self.buildAttributes(node, node.attrib, already_processed)
        self.valueOf_ = get_all_text_(node)
        self.validate_valueOf_(self.valueOf_)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_)
        return self
''',
    class_names=r'^SellerInstructionFreeTextType$',
    )

method130 = MethodSpec(name='validate_valueOf_',
    source='''\
    def validate_valueOf_(self, value):
        if ( isinstance( value, basestring ) and value.__len__() <= 35 ):
            pass
        else:
            raise_value_error( value, 'Expected value less than 35 characters' )
        return value
''',
    class_names=r'^SellerInvoiceTypeTextType$',
    )

method140 = MethodSpec(name='build',
    source='''\
    def build(self, node):
        already_processed = set()
        self.buildAttributes(node, node.attrib, already_processed)
        self.valueOf_ = get_all_text_(node)
        self.validate_valueOf_(self.valueOf_)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_)
        return self
''',
    class_names=r'^SellerInvoiceTypeTextType$',
    )

method150 = MethodSpec(name='validate_valueOf_',
    source='''\
    def validate_valueOf_(self, value):
        if ( isinstance( value, basestring ) and 4 <= value.__len__() <= 70 ):
            pass
        else:
            raise_value_error( value, 'Expected value between 4..70 characters' )
        return value
''',
    class_names=r'^SellerInvoiceIdentifierTextType3$',
    )

method160 = MethodSpec(name='build',
    source='''\
    def build(self, node):
        already_processed = set()
        self.buildAttributes(node, node.attrib, already_processed)
        self.valueOf_ = get_all_text_(node)
        self.validate_valueOf_(self.valueOf_)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_)
        return self
''',
    class_names=r'^SellerInvoiceIdentifierTextType3$',
    )

method170 = MethodSpec(name='validate_valueOf_',
    source='''\
    def validate_SellerInvoiceIdentifierTextType3(self, value):
        if ( value.__len__() <= 2 ):
            pass
        else:
            raise_value_error( value, 'Expected maximum of 2 elements' )
        return value
''',
    class_names=r'^SellerInvoiceTypeDetailsType$',
    )

method180 = MethodSpec(name='buildChildren',
    source='''\
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        if nodeName_ == 'SellerInvoiceTypeText':
            obj_ = SellerInvoiceTypeTextType.factory()
            obj_.build(child_)
            self.SellerInvoiceTypeText = obj_
            obj_.original_tagname_ = 'SellerInvoiceTypeText'
        elif nodeName_ == 'SellerInvoiceIdentifierText':
            obj_ = SellerInvoiceIdentifierTextType3.factory()
            obj_.build(child_)
            self.SellerInvoiceIdentifierText.append(obj_)
            self.validate_SellerInvoiceIdentifierTextType3(self.SellerInvoiceIdentifierText);
            obj_.original_tagname_ = 'SellerInvoiceIdentifierText'
''',
    class_names=r'^SellerInvoiceTypeDetailsType$',
    )

method190 = MethodSpec(name='validate_valueOf_',
    source='''\
    def validate_valueOf_(self, value):
        import datetime
        if ( datetime.datetime.strptime( value, '%%Y%%m%%d\' ).strftime( '%%Y%%m%%d\' ) == value ):
            pass
        else:
            raise_value_error( value, 'Time format does not match' )
        return value
''',
    class_names=r'^date$',
    )

method200 = MethodSpec(name='build',
    source='''\
    def build(self, node):
        already_processed = set()
        self.buildAttributes(node, node.attrib, already_processed)
        self.valueOf_ = get_all_text_(node)
        self.validate_valueOf_(self.valueOf_)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_)
        return self
''',
    class_names=r'^date$',
    )

method210 = MethodSpec(name='validate_Format',
    source='''\
    def validate_Format(self, value):
        if ( value == "CCYYMMDD" ):
            pass
        else:
            raise_value_error( value, 'Expected "CCYYMMDD"' )
        return value
''',
    class_names=r'^date$',
    )

method220 = MethodSpec(name='buildAttributes',
    source='''\
    def buildAttributes(self, node, attrs, already_processed):
        value = find_attr_value_('Format', node)
        if value is not None and 'Format' not in already_processed:
            already_processed.add('Format')
            self.Format = value
            self.validate_Format(self.Format)
''',
    class_names=r'^date$',
    )

method230 = MethodSpec(name='validate_SellerOrganisationNamesType',
    source='''\
    def validate_SellerOrganisationNamesType(self, value):
        if ( value.__len__() <= 3 ):
            pass
        else:
            raise_value_error( value.__len__(), 'Expected maximum of 3 elements' )
        return value
''',
    class_names=r'^SellerPartyDetailsType$',
    )

method231 = MethodSpec(name='validate_SellerOrganisationBankName',
    source='''\
    def validate_SellerOrganisationBankName(self, value):
        if ( value.__len__() <= 2 ):
            pass
        else:
            raise_value_error( value.__len__(), 'Expected maximum of 3 elements' )
        return value
''',
    class_names=r'^SellerPartyDetailsType$',
    )

method240 = MethodSpec(name='buildChildren',
    source='''\
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        if nodeName_ == 'SellerPartyIdentifier':
            SellerPartyIdentifier_ = child_.text
            SellerPartyIdentifier_ = self.gds_validate_string(SellerPartyIdentifier_, node, 'SellerPartyIdentifier')
            self.SellerPartyIdentifier = SellerPartyIdentifier_
            self.validate_genericStringType1_48(self.SellerPartyIdentifier)    # validate type genericStringType1_48
        elif nodeName_ == 'SellerOrganisationNames':
            obj_ = SellerOrganisationNamesType.factory()
            obj_.build(child_)
            self.SellerOrganisationNames.append(obj_)
            self.validate_SellerOrganisationNamesType(self.SellerOrganisationNames)
            obj_.original_tagname_ = 'SellerOrganisationNames'
        elif nodeName_ == 'SellerOrganisationBankName':
            SellerOrganisationBankName_ = child_.text
            SellerOrganisationBankName_ = self.gds_validate_string(SellerOrganisationBankName_, node, 'SellerOrganisationBankName')
            self.SellerOrganisationBankName.append(SellerOrganisationBankName_)
            self.validate_genericStringType1_35(self.SellerOrganisationBankName)    # validate type genericStringType1_35
            self.validate_SellerOrganisationBankName(self.SellerOrganisationBankName)
        elif nodeName_ == 'SellerPostalAddressDetails':
            obj_ = SellerPostalAddressDetailsType.factory()
            obj_.build(child_)
            self.SellerPostalAddressDetails = obj_
            obj_.original_tagname_ = 'SellerPostalAddressDetails'
        elif nodeName_ == 'IndustryCode':
            IndustryCode_ = child_.text
            IndustryCode_ = self.gds_validate_string(IndustryCode_, node, 'IndustryCode')
            self.IndustryCode = IndustryCode_
            self.validate_genericStringType0_6(self.IndustryCode)    # validate type genericStringType0_6
''',
    class_names=r'^SellerPartyDetailsType$',
    )

method250 = MethodSpec(name='validate_SellerOrganisationName',
    source='''\
    def validate_SellerOrganisationName(self, value):
        if ( value.__len__() <= 2 ):
            pass
        else:
            raise_value_error( value.__len__(), 'Expected maximum of 2 elements' )
        return value
''',
    class_names=r'^SellerOrganisationNamesType$',
    )

method260 = MethodSpec(name='buildChildren',
    source='''\
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        if nodeName_ == 'SellerOrganisationName':
            SellerOrganisationName_ = child_.text
            SellerOrganisationName_ = self.gds_validate_string(SellerOrganisationName_, node, 'SellerOrganisationName')
            self.SellerOrganisationName.append(SellerOrganisationName_)
            self.validate_genericStringType2_70(self.SellerOrganisationName)    # validate type genericStringType2_70
            self.validate_SellerOrganisationName(self.SellerOrganisationName)
''',
    class_names=r'^SellerOrganisationNamesType$',
    )

#
# Provide a list of your method specifications.
#   This list of specifications must be named METHOD_SPECS.
#
METHOD_SPECS = (
    method10,
    method20,
    method30,
    method40,
    method50,
    method60,
    method70,
    method80,
    method90,
    method91,
    method100,
    method110,
    method120,
    method130,
    method140,
    method150,
    method160,
    method170,
    method180,
    method190,
    method200,
    method210,
    method220,
    method230,
    method231,
    method240,
    method250,
    method260,
    )


def test():
    for spec in METHOD_SPECS:
        spec.show()

def main():
    test()


if __name__ == '__main__':
    main()


