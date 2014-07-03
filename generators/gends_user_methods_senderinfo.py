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

method1 = MethodSpec(name='validate_valueOf_',
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

method2 = MethodSpec(name='build',
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

method3 = MethodSpec(name='validate_IdentificationSchemeName',
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

method4 = MethodSpec(name='buildAttributes',
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

method5 = MethodSpec(name='validate_valueOf_',
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

method6 = MethodSpec(name='build',
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

method7 = MethodSpec(name='validate_IdentificationSchemeName',
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

method8 = MethodSpec(name='buildAttributes',
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

method9 = MethodSpec(name='validate_SellerInstructionFreeTextType',
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

method10 = MethodSpec(name='buildChildren',
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
            obj_.original_tagname_ = 'SellerInvoiceTypeDetails'
        elif nodeName_ == 'SellerServiceCode':
            SellerServiceCode_ = child_.text
            SellerServiceCode_ = self.gds_validate_string(SellerServiceCode_, node, 'SellerServiceCode')
            self.SellerServiceCode = SellerServiceCode_
            self.validate_SellerServiceCodeType(self.SellerServiceCode)    # validate type SellerServiceCodeType
''',
    class_names=r'^SellerInvoiceDetailsType$',
    )

method11 = MethodSpec(name='validate_valueOf_',
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

method12 = MethodSpec(name='build',
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

method13 = MethodSpec(name='validate_valueOf_',
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

method14 = MethodSpec(name='build',
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

method13 = MethodSpec(name='validate_valueOf_',
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

method14 = MethodSpec(name='build',
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

method15 = MethodSpec(name='validate_valueOf_',
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

method16 = MethodSpec(name='buildChildren',
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

method17 = MethodSpec(name='validate_valueOf_',
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

method18 = MethodSpec(name='build',
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

method19 = MethodSpec(name='validate_Format',
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

method20 = MethodSpec(name='buildAttributes',
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
#
# Provide a list of your method specifications.
#   This list of specifications must be named METHOD_SPECS.
#
METHOD_SPECS = (
    method1,
    method2,
    method3,
    method4,
    method5,
    method6,
    method7,
    method8,
    method9,
    method10,
    method11,
    method12,
    method13,
    method14,
    method15,
    method16,
    method17,
    method18,
    method19,
    method20,
    )


def test():
    for spec in METHOD_SPECS:
        spec.show()

def main():
    test()


if __name__ == '__main__':
    main()


