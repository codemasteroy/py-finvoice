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


class FinvoiceSub(supermod.Finvoice):
    def __init__(self, Version=None, MessageTransmissionDetails=None, SellerPartyDetails=None, SellerOrganisationUnitNumber=None, SellerSiteCode=None, SellerContactPersonName=None, SellerContactPersonFunction=None, SellerContactPersonDepartment=None, SellerCommunicationDetails=None, SellerInformationDetails=None, InvoiceSenderPartyDetails=None, InvoiceRecipientPartyDetails=None, InvoiceRecipientOrganisationUnitNumber=None, InvoiceRecipientSiteCode=None, InvoiceRecipientContactPersonName=None, InvoiceRecipientContactPersonFunction=None, InvoiceRecipientContactPersonDepartment=None, InvoiceRecipientLanguageCode=None, InvoiceRecipientCommunicationDetails=None, BuyerPartyDetails=None, BuyerOrganisationUnitNumber=None, BuyerSiteCode=None, BuyerContactPersonName=None, BuyerContactPersonFunction=None, BuyerContactPersonDepartment=None, BuyerCommunicationDetails=None, DeliveryPartyDetails=None, DeliveryOrganisationUnitNumber=None, DeliverySiteCode=None, DeliveryContactPersonName=None, DeliveryContactPersonFunction=None, DeliveryContactPersonDepartment=None, DeliveryCommunicationDetails=None, DeliveryDetails=None, AnyPartyDetails=None, InvoiceDetails=None, PaymentStatusDetails=None, PartialPaymentDetails=None, FactoringAgreementDetails=None, VirtualBankBarcode=None, InvoiceRow=None, SpecificationDetails=None, EpiDetails=None, InvoiceUrlNameText=None, InvoiceUrlText=None, StorageUrlText=None, LayOutIdentifier=None, InvoiceSegmentIdentifier=None, ControlStampText=None, AcceptanceStampText=None, OriginalInvoiceFormat=None, AttachmentMessageDetails=None):
        super(FinvoiceSub, self).__init__(Version, MessageTransmissionDetails, SellerPartyDetails, SellerOrganisationUnitNumber, SellerSiteCode, SellerContactPersonName, SellerContactPersonFunction, SellerContactPersonDepartment, SellerCommunicationDetails, SellerInformationDetails, InvoiceSenderPartyDetails, InvoiceRecipientPartyDetails, InvoiceRecipientOrganisationUnitNumber, InvoiceRecipientSiteCode, InvoiceRecipientContactPersonName, InvoiceRecipientContactPersonFunction, InvoiceRecipientContactPersonDepartment, InvoiceRecipientLanguageCode, InvoiceRecipientCommunicationDetails, BuyerPartyDetails, BuyerOrganisationUnitNumber, BuyerSiteCode, BuyerContactPersonName, BuyerContactPersonFunction, BuyerContactPersonDepartment, BuyerCommunicationDetails, DeliveryPartyDetails, DeliveryOrganisationUnitNumber, DeliverySiteCode, DeliveryContactPersonName, DeliveryContactPersonFunction, DeliveryContactPersonDepartment, DeliveryCommunicationDetails, DeliveryDetails, AnyPartyDetails, InvoiceDetails, PaymentStatusDetails, PartialPaymentDetails, FactoringAgreementDetails, VirtualBankBarcode, InvoiceRow, SpecificationDetails, EpiDetails, InvoiceUrlNameText, InvoiceUrlText, StorageUrlText, LayOutIdentifier, InvoiceSegmentIdentifier, ControlStampText, AcceptanceStampText, OriginalInvoiceFormat, AttachmentMessageDetails, )
supermod.Finvoice.subclass = FinvoiceSub
# end class FinvoiceSub


class MessageTransmissionDetailsTypeSub(supermod.MessageTransmissionDetailsType):
    def __init__(self, MessageSenderDetails=None, MessageReceiverDetails=None, MessageDetails=None):
        super(MessageTransmissionDetailsTypeSub, self).__init__(MessageSenderDetails, MessageReceiverDetails, MessageDetails, )
supermod.MessageTransmissionDetailsType.subclass = MessageTransmissionDetailsTypeSub
# end class MessageTransmissionDetailsTypeSub


class AnyPartyDetailsTypeSub(supermod.AnyPartyDetailsType):
    def __init__(self, AnyPartyText=None, AnyPartyIdentifier=None, AnyPartyOrganisationName=None, AnyPartyOrganisationDepartment=None, AnyPartyOrganisationTaxCode=None, AnyPartyCode=None, AnyPartyContactPersonName=None, AnyPartyContactPersonFunction=None, AnyPartyContactPersonDepartment=None, AnyPartyCommunicationDetails=None, AnyPartyPostalAddressDetails=None, AnyPartyOrganisationUnitNumber=None, AnyPartySiteCode=None):
        super(AnyPartyDetailsTypeSub, self).__init__(AnyPartyText, AnyPartyIdentifier, AnyPartyOrganisationName, AnyPartyOrganisationDepartment, AnyPartyOrganisationTaxCode, AnyPartyCode, AnyPartyContactPersonName, AnyPartyContactPersonFunction, AnyPartyContactPersonDepartment, AnyPartyCommunicationDetails, AnyPartyPostalAddressDetails, AnyPartyOrganisationUnitNumber, AnyPartySiteCode, )
supermod.AnyPartyDetailsType.subclass = AnyPartyDetailsTypeSub
# end class AnyPartyDetailsTypeSub


class FactoringAgreementDetailsTypeSub(supermod.FactoringAgreementDetailsType):
    def __init__(self, FactoringAgreementIdentifier=None, TransmissionListIdentifier=None, EndorsementClauseCode=None, FactoringTypeCode=None, FactoringFreeText=None, FactoringPartyIdentifier=None, FactoringPartyName=None, FactoringPartyPostalAddressDetails=None):
        super(FactoringAgreementDetailsTypeSub, self).__init__(FactoringAgreementIdentifier, TransmissionListIdentifier, EndorsementClauseCode, FactoringTypeCode, FactoringFreeText, FactoringPartyIdentifier, FactoringPartyName, FactoringPartyPostalAddressDetails, )
supermod.FactoringAgreementDetailsType.subclass = FactoringAgreementDetailsTypeSub
# end class FactoringAgreementDetailsTypeSub


class BuyerCommunicationDetailsTypeSub(supermod.BuyerCommunicationDetailsType):
    def __init__(self, BuyerPhoneNumberIdentifier=None, BuyerEmailaddressIdentifier=None):
        super(BuyerCommunicationDetailsTypeSub, self).__init__(BuyerPhoneNumberIdentifier, BuyerEmailaddressIdentifier, )
supermod.BuyerCommunicationDetailsType.subclass = BuyerCommunicationDetailsTypeSub
# end class BuyerCommunicationDetailsTypeSub


class BuyerPartyDetailsTypeSub(supermod.BuyerPartyDetailsType):
    def __init__(self, BuyerPartyIdentifier=None, BuyerOrganisationName=None, BuyerOrganisationDepartment=None, BuyerOrganisationTaxCode=None, BuyerCode=None, BuyerPostalAddressDetails=None):
        super(BuyerPartyDetailsTypeSub, self).__init__(BuyerPartyIdentifier, BuyerOrganisationName, BuyerOrganisationDepartment, BuyerOrganisationTaxCode, BuyerCode, BuyerPostalAddressDetails, )
supermod.BuyerPartyDetailsType.subclass = BuyerPartyDetailsTypeSub
# end class BuyerPartyDetailsTypeSub


class BuyerPostalAddressDetailsTypeSub(supermod.BuyerPostalAddressDetailsType):
    def __init__(self, BuyerStreetName=None, BuyerTownName=None, BuyerPostCodeIdentifier=None, CountryCode=None, CountryName=None, BuyerPostOfficeBoxIdentifier=None):
        super(BuyerPostalAddressDetailsTypeSub, self).__init__(BuyerStreetName, BuyerTownName, BuyerPostCodeIdentifier, CountryCode, CountryName, BuyerPostOfficeBoxIdentifier, )
supermod.BuyerPostalAddressDetailsType.subclass = BuyerPostalAddressDetailsTypeSub
# end class BuyerPostalAddressDetailsTypeSub


class DeliveryCommunicationDetailsTypeSub(supermod.DeliveryCommunicationDetailsType):
    def __init__(self, DeliveryPhoneNumberIdentifier=None, DeliveryEmailaddressIdentifier=None):
        super(DeliveryCommunicationDetailsTypeSub, self).__init__(DeliveryPhoneNumberIdentifier, DeliveryEmailaddressIdentifier, )
supermod.DeliveryCommunicationDetailsType.subclass = DeliveryCommunicationDetailsTypeSub
# end class DeliveryCommunicationDetailsTypeSub


class DeliveryDetailsTypeSub(supermod.DeliveryDetailsType):
    def __init__(self, DeliveryDate=None, DeliveryPeriodDetails=None, ShipmentPartyDetails=None, DeliveryMethodText=None, DeliveryTermsText=None, DeliveryTermsCode=None, TerminalAddressText=None, WaybillIdentifier=None, WaybillTypeCode=None, ClearanceIdentifier=None, DeliveryNoteIdentifier=None, DelivererIdentifier=None, DelivererName=None, DelivererCountryCode=None, DelivererCountryName=None, ModeOfTransportIdentifier=None, CarrierName=None, VesselName=None, LocationIdentifier=None, TransportInformationDate=None, CountryOfOrigin=None, CountryOfDestinationName=None, DestinationCountryCode=None, PlaceOfDischarge=None, FinalDestinationName=None, ManufacturerIdentifier=None, ManufacturerName=None, ManufacturerCountryCode=None, ManufacturerCountryName=None, ManufacturerOrderIdentifier=None, PackageDetails=None):
        super(DeliveryDetailsTypeSub, self).__init__(DeliveryDate, DeliveryPeriodDetails, ShipmentPartyDetails, DeliveryMethodText, DeliveryTermsText, DeliveryTermsCode, TerminalAddressText, WaybillIdentifier, WaybillTypeCode, ClearanceIdentifier, DeliveryNoteIdentifier, DelivererIdentifier, DelivererName, DelivererCountryCode, DelivererCountryName, ModeOfTransportIdentifier, CarrierName, VesselName, LocationIdentifier, TransportInformationDate, CountryOfOrigin, CountryOfDestinationName, DestinationCountryCode, PlaceOfDischarge, FinalDestinationName, ManufacturerIdentifier, ManufacturerName, ManufacturerCountryCode, ManufacturerCountryName, ManufacturerOrderIdentifier, PackageDetails, )
supermod.DeliveryDetailsType.subclass = DeliveryDetailsTypeSub
# end class DeliveryDetailsTypeSub


class DeliveryPartyDetailsTypeSub(supermod.DeliveryPartyDetailsType):
    def __init__(self, DeliveryPartyIdentifier=None, DeliveryOrganisationName=None, DeliveryOrganisationDepartment=None, DeliveryOrganisationTaxCode=None, DeliveryCode=None, DeliveryPostalAddressDetails=None):
        super(DeliveryPartyDetailsTypeSub, self).__init__(DeliveryPartyIdentifier, DeliveryOrganisationName, DeliveryOrganisationDepartment, DeliveryOrganisationTaxCode, DeliveryCode, DeliveryPostalAddressDetails, )
supermod.DeliveryPartyDetailsType.subclass = DeliveryPartyDetailsTypeSub
# end class DeliveryPartyDetailsTypeSub


class DeliveryPeriodDetailsTypeSub(supermod.DeliveryPeriodDetailsType):
    def __init__(self, StartDate=None, EndDate=None):
        super(DeliveryPeriodDetailsTypeSub, self).__init__(StartDate, EndDate, )
supermod.DeliveryPeriodDetailsType.subclass = DeliveryPeriodDetailsTypeSub
# end class DeliveryPeriodDetailsTypeSub


class DeliveryPostalAddressDetailsTypeSub(supermod.DeliveryPostalAddressDetailsType):
    def __init__(self, DeliveryStreetName=None, DeliveryTownName=None, DeliveryPostCodeIdentifier=None, CountryCode=None, CountryName=None, DeliveryPostofficeBoxIdentifier=None):
        super(DeliveryPostalAddressDetailsTypeSub, self).__init__(DeliveryStreetName, DeliveryTownName, DeliveryPostCodeIdentifier, CountryCode, CountryName, DeliveryPostofficeBoxIdentifier, )
supermod.DeliveryPostalAddressDetailsType.subclass = DeliveryPostalAddressDetailsTypeSub
# end class DeliveryPostalAddressDetailsTypeSub


class EpiAccountIDTypeSub(supermod.EpiAccountIDType):
    def __init__(self, IdentificationSchemeName=None, valueOf_=None):
        super(EpiAccountIDTypeSub, self).__init__(IdentificationSchemeName, valueOf_, )
supermod.EpiAccountIDType.subclass = EpiAccountIDTypeSub
# end class EpiAccountIDTypeSub


class EpiBfiIdentifierTypeSub(supermod.EpiBfiIdentifierType):
    def __init__(self, IdentificationSchemeName=None, valueOf_=None):
        super(EpiBfiIdentifierTypeSub, self).__init__(IdentificationSchemeName, valueOf_, )
supermod.EpiBfiIdentifierType.subclass = EpiBfiIdentifierTypeSub
# end class EpiBfiIdentifierTypeSub


class EpiDetailsTypeSub(supermod.EpiDetailsType):
    def __init__(self, EpiIdentificationDetails=None, EpiPartyDetails=None, EpiPaymentInstructionDetails=None):
        super(EpiDetailsTypeSub, self).__init__(EpiIdentificationDetails, EpiPartyDetails, EpiPaymentInstructionDetails, )
supermod.EpiDetailsType.subclass = EpiDetailsTypeSub
# end class EpiDetailsTypeSub


class EpiIdentificationDetailsTypeSub(supermod.EpiIdentificationDetailsType):
    def __init__(self, EpiDate=None, EpiReference=None, EpiUrl=None, EpiEmail=None, EpiOrderInfo=None):
        super(EpiIdentificationDetailsTypeSub, self).__init__(EpiDate, EpiReference, EpiUrl, EpiEmail, EpiOrderInfo, )
supermod.EpiIdentificationDetailsType.subclass = EpiIdentificationDetailsTypeSub
# end class EpiIdentificationDetailsTypeSub


class EpiPartyDetailsTypeSub(supermod.EpiPartyDetailsType):
    def __init__(self, EpiBfiPartyDetails=None, EpiBeneficiaryPartyDetails=None):
        super(EpiPartyDetailsTypeSub, self).__init__(EpiBfiPartyDetails, EpiBeneficiaryPartyDetails, )
supermod.EpiPartyDetailsType.subclass = EpiPartyDetailsTypeSub
# end class EpiPartyDetailsTypeSub


class EpiBfiPartyDetailsTypeSub(supermod.EpiBfiPartyDetailsType):
    def __init__(self, EpiBfiIdentifier=None, EpiBfiName=None):
        super(EpiBfiPartyDetailsTypeSub, self).__init__(EpiBfiIdentifier, EpiBfiName, )
supermod.EpiBfiPartyDetailsType.subclass = EpiBfiPartyDetailsTypeSub
# end class EpiBfiPartyDetailsTypeSub


class EpiBeneficiaryPartyDetailsTypeSub(supermod.EpiBeneficiaryPartyDetailsType):
    def __init__(self, EpiNameAddressDetails=None, EpiBei=None, EpiAccountID=None):
        super(EpiBeneficiaryPartyDetailsTypeSub, self).__init__(EpiNameAddressDetails, EpiBei, EpiAccountID, )
supermod.EpiBeneficiaryPartyDetailsType.subclass = EpiBeneficiaryPartyDetailsTypeSub
# end class EpiBeneficiaryPartyDetailsTypeSub


class EpiPaymentInstructionDetailsTypeSub(supermod.EpiPaymentInstructionDetailsType):
    def __init__(self, EpiPaymentInstructionId=None, EpiTransactionTypeCode=None, EpiInstructionCode=None, EpiRemittanceInfoIdentifier=None, EpiInstructedAmount=None, EpiCharge=None, EpiDateOptionDate=None):
        super(EpiPaymentInstructionDetailsTypeSub, self).__init__(EpiPaymentInstructionId, EpiTransactionTypeCode, EpiInstructionCode, EpiRemittanceInfoIdentifier, EpiInstructedAmount, EpiCharge, EpiDateOptionDate, )
supermod.EpiPaymentInstructionDetailsType.subclass = EpiPaymentInstructionDetailsTypeSub
# end class EpiPaymentInstructionDetailsTypeSub


class EpiChargeTypeSub(supermod.EpiChargeType):
    def __init__(self, ChargeOption=None, valueOf_=None):
        super(EpiChargeTypeSub, self).__init__(ChargeOption, valueOf_, )
supermod.EpiChargeType.subclass = EpiChargeTypeSub
# end class EpiChargeTypeSub


class EpiRemittanceInfoIdentifierTypeSub(supermod.EpiRemittanceInfoIdentifierType):
    def __init__(self, IdentificationSchemeName=None, valueOf_=None):
        super(EpiRemittanceInfoIdentifierTypeSub, self).__init__(IdentificationSchemeName, valueOf_, )
supermod.EpiRemittanceInfoIdentifierType.subclass = EpiRemittanceInfoIdentifierTypeSub
# end class EpiRemittanceInfoIdentifierTypeSub


class InvoiceDetailsTypeSub(supermod.InvoiceDetailsType):
    def __init__(self, InvoiceTypeCode=None, InvoiceTypeText=None, OriginCode=None, OriginText=None, InvoiceNumber=None, InvoiceDate=None, OriginalInvoiceNumber=None, InvoicingPeriodStartDate=None, InvoicingPeriodEndDate=None, SellerReferenceIdentifier=None, SellerReferenceIdentifierUrlText=None, BuyersSellerIdentifier=None, SellersBuyerIdentifier=None, OrderIdentifier=None, OrderIdentifierUrlText=None, OrderDate=None, OrdererName=None, SalesPersonName=None, OrderConfirmationIdentifier=None, OrderConfirmationDate=None, AgreementIdentifier=None, AgreementIdentifierUrlText=None, AgreementTypeText=None, AgreementTypeCode=None, AgreementDate=None, NotificationIdentifier=None, NotificationDate=None, RegistrationNumberIdentifier=None, ControllerIdentifier=None, ControllerName=None, ControlDate=None, BuyerReferenceIdentifier=None, ProjectReferenceIdentifier=None, DefinitionDetails=None, InvoiceTotalVatExcludedAmount=None, InvoiceTotalVatAmount=None, InvoiceTotalVatIncludedAmount=None, InvoiceTotalRoundoffAmount=None, ExchangeRate=None, OtherCurrencyAmountVatExcludedAmount=None, OtherCurrencyAmountVatIncludedAmount=None, CreditLimitAmount=None, CreditInterestPercent=None, OperationLimitAmount=None, MonthlyAmount=None, ShortProposedAccountIdentifier=None, NormalProposedAccountIdentifier=None, ProposedAccountText=None, AccountDimensionText=None, SellerAccountText=None, VatSpecificationDetails=None, InvoiceFreeText=None, InvoiceVatFreeText=None, PaymentTermsDetails=None, DiscountDetails=None):
        super(InvoiceDetailsTypeSub, self).__init__(InvoiceTypeCode, InvoiceTypeText, OriginCode, OriginText, InvoiceNumber, InvoiceDate, OriginalInvoiceNumber, InvoicingPeriodStartDate, InvoicingPeriodEndDate, SellerReferenceIdentifier, SellerReferenceIdentifierUrlText, BuyersSellerIdentifier, SellersBuyerIdentifier, OrderIdentifier, OrderIdentifierUrlText, OrderDate, OrdererName, SalesPersonName, OrderConfirmationIdentifier, OrderConfirmationDate, AgreementIdentifier, AgreementIdentifierUrlText, AgreementTypeText, AgreementTypeCode, AgreementDate, NotificationIdentifier, NotificationDate, RegistrationNumberIdentifier, ControllerIdentifier, ControllerName, ControlDate, BuyerReferenceIdentifier, ProjectReferenceIdentifier, DefinitionDetails, InvoiceTotalVatExcludedAmount, InvoiceTotalVatAmount, InvoiceTotalVatIncludedAmount, InvoiceTotalRoundoffAmount, ExchangeRate, OtherCurrencyAmountVatExcludedAmount, OtherCurrencyAmountVatIncludedAmount, CreditLimitAmount, CreditInterestPercent, OperationLimitAmount, MonthlyAmount, ShortProposedAccountIdentifier, NormalProposedAccountIdentifier, ProposedAccountText, AccountDimensionText, SellerAccountText, VatSpecificationDetails, InvoiceFreeText, InvoiceVatFreeText, PaymentTermsDetails, DiscountDetails, )
supermod.InvoiceDetailsType.subclass = InvoiceDetailsTypeSub
# end class InvoiceDetailsTypeSub


class InvoiceRecipientCommunicationDetailsTypeSub(supermod.InvoiceRecipientCommunicationDetailsType):
    def __init__(self, InvoiceRecipientPhoneNumberIdentifier=None, InvoiceRecipientEmailaddressIdentifier=None):
        super(InvoiceRecipientCommunicationDetailsTypeSub, self).__init__(InvoiceRecipientPhoneNumberIdentifier, InvoiceRecipientEmailaddressIdentifier, )
supermod.InvoiceRecipientCommunicationDetailsType.subclass = InvoiceRecipientCommunicationDetailsTypeSub
# end class InvoiceRecipientCommunicationDetailsTypeSub


class InvoiceRecipientDetailsTypeSub(supermod.InvoiceRecipientDetailsType):
    def __init__(self, InvoiceRecipientAddress=None, InvoiceRecipientIntermediatorAddress=None):
        super(InvoiceRecipientDetailsTypeSub, self).__init__(InvoiceRecipientAddress, InvoiceRecipientIntermediatorAddress, )
supermod.InvoiceRecipientDetailsType.subclass = InvoiceRecipientDetailsTypeSub
# end class InvoiceRecipientDetailsTypeSub


class InvoiceRecipientPartyDetailsTypeSub(supermod.InvoiceRecipientPartyDetailsType):
    def __init__(self, InvoiceRecipientPartyIdentifier=None, InvoiceRecipientOrganisationName=None, InvoiceRecipientDepartment=None, InvoiceRecipientOrganisationTaxCode=None, InvoiceRecipientCode=None, InvoiceRecipientPostalAddressDetails=None):
        super(InvoiceRecipientPartyDetailsTypeSub, self).__init__(InvoiceRecipientPartyIdentifier, InvoiceRecipientOrganisationName, InvoiceRecipientDepartment, InvoiceRecipientOrganisationTaxCode, InvoiceRecipientCode, InvoiceRecipientPostalAddressDetails, )
supermod.InvoiceRecipientPartyDetailsType.subclass = InvoiceRecipientPartyDetailsTypeSub
# end class InvoiceRecipientPartyDetailsTypeSub


class InvoiceRecipientPostalAddressDetailsTypeSub(supermod.InvoiceRecipientPostalAddressDetailsType):
    def __init__(self, InvoiceRecipientStreetName=None, InvoiceRecipientTownName=None, InvoiceRecipientPostCodeIdentifier=None, CountryCode=None, CountryName=None, InvoiceRecipientPostOfficeBoxIdentifier=None):
        super(InvoiceRecipientPostalAddressDetailsTypeSub, self).__init__(InvoiceRecipientStreetName, InvoiceRecipientTownName, InvoiceRecipientPostCodeIdentifier, CountryCode, CountryName, InvoiceRecipientPostOfficeBoxIdentifier, )
supermod.InvoiceRecipientPostalAddressDetailsType.subclass = InvoiceRecipientPostalAddressDetailsTypeSub
# end class InvoiceRecipientPostalAddressDetailsTypeSub


class InvoiceRowTypeSub(supermod.InvoiceRowType):
    def __init__(self, RowSubIdentifier=None, ArticleIdentifier=None, ArticleGroupIdentifier=None, ArticleName=None, ArticleInfoUrlText=None, BuyerArticleIdentifier=None, EanCode=None, RowRegistrationNumberIdentifier=None, SerialNumberIdentifier=None, RowActionCode=None, RowDefinitionDetails=None, OfferedQuantity=None, DeliveredQuantity=None, OrderedQuantity=None, ConfirmedQuantity=None, PostDeliveredQuantity=None, InvoicedQuantity=None, CreditRequestedQuantity=None, ReturnedQuantity=None, StartDate=None, EndDate=None, UnitPriceAmount=None, UnitPriceVatIncludedAmount=None, UnitPriceBaseQuantity=None, RowIdentifier=None, RowIdentifierUrlText=None, RowOrderPositionIdentifier=None, RowIdentifierDate=None, RowPositionIdentifier=None, OriginalInvoiceNumber=None, RowOrdererName=None, RowSalesPersonName=None, RowOrderConfirmationIdentifier=None, RowOrderConfirmationDate=None, RowDeliveryIdentifier=None, RowDeliveryIdentifierUrlText=None, RowDeliveryDate=None, RowQuotationIdentifier=None, RowQuotationIdentifierUrlText=None, RowAgreementIdentifier=None, RowAgreementIdentifierUrlText=None, RowRequestOfQuotationIdentifier=None, RowRequestOfQuotationIdentifierUrlText=None, RowPriceListIdentifier=None, RowPriceListIdentifierUrlText=None, RowProjectReferenceIdentifier=None, RowOverDuePaymentDetails=None, RowAnyPartyDetails=None, RowDeliveryDetails=None, RowShortProposedAccountIdentifier=None, RowNormalProposedAccountIdentifier=None, RowProposedAccountText=None, RowAccountDimensionText=None, RowSellerAccountText=None, RowFreeText=None, RowUsedQuantity=None, RowPreviousMeterReadingDate=None, RowLatestMeterReadingDate=None, RowCalculatedQuantity=None, RowAveragePriceAmount=None, RowDiscountPercent=None, RowDiscountAmount=None, RowDiscountTypeCode=None, RowDiscountTypeText=None, RowProgressiveDiscountDetails=None, RowVatRatePercent=None, RowVatCode=None, RowVatAmount=None, RowVatExcludedAmount=None, RowAmount=None, RowTransactionDetails=None, SubInvoiceRow=None):
        super(InvoiceRowTypeSub, self).__init__(RowSubIdentifier, ArticleIdentifier, ArticleGroupIdentifier, ArticleName, ArticleInfoUrlText, BuyerArticleIdentifier, EanCode, RowRegistrationNumberIdentifier, SerialNumberIdentifier, RowActionCode, RowDefinitionDetails, OfferedQuantity, DeliveredQuantity, OrderedQuantity, ConfirmedQuantity, PostDeliveredQuantity, InvoicedQuantity, CreditRequestedQuantity, ReturnedQuantity, StartDate, EndDate, UnitPriceAmount, UnitPriceVatIncludedAmount, UnitPriceBaseQuantity, RowIdentifier, RowIdentifierUrlText, RowOrderPositionIdentifier, RowIdentifierDate, RowPositionIdentifier, OriginalInvoiceNumber, RowOrdererName, RowSalesPersonName, RowOrderConfirmationIdentifier, RowOrderConfirmationDate, RowDeliveryIdentifier, RowDeliveryIdentifierUrlText, RowDeliveryDate, RowQuotationIdentifier, RowQuotationIdentifierUrlText, RowAgreementIdentifier, RowAgreementIdentifierUrlText, RowRequestOfQuotationIdentifier, RowRequestOfQuotationIdentifierUrlText, RowPriceListIdentifier, RowPriceListIdentifierUrlText, RowProjectReferenceIdentifier, RowOverDuePaymentDetails, RowAnyPartyDetails, RowDeliveryDetails, RowShortProposedAccountIdentifier, RowNormalProposedAccountIdentifier, RowProposedAccountText, RowAccountDimensionText, RowSellerAccountText, RowFreeText, RowUsedQuantity, RowPreviousMeterReadingDate, RowLatestMeterReadingDate, RowCalculatedQuantity, RowAveragePriceAmount, RowDiscountPercent, RowDiscountAmount, RowDiscountTypeCode, RowDiscountTypeText, RowProgressiveDiscountDetails, RowVatRatePercent, RowVatCode, RowVatAmount, RowVatExcludedAmount, RowAmount, RowTransactionDetails, SubInvoiceRow, )
supermod.InvoiceRowType.subclass = InvoiceRowTypeSub
# end class InvoiceRowTypeSub


class InvoiceSenderPartyDetailsTypeSub(supermod.InvoiceSenderPartyDetailsType):
    def __init__(self, InvoiceSenderPartyIdentifier=None, InvoiceSenderOrganisationName=None, InvoiceSenderOrganisationTaxCode=None, InvoiceSenderCode=None):
        super(InvoiceSenderPartyDetailsTypeSub, self).__init__(InvoiceSenderPartyIdentifier, InvoiceSenderOrganisationName, InvoiceSenderOrganisationTaxCode, InvoiceSenderCode, )
supermod.InvoiceSenderPartyDetailsType.subclass = InvoiceSenderPartyDetailsTypeSub
# end class InvoiceSenderPartyDetailsTypeSub


class InvoiceTypeCodeTypeSub(supermod.InvoiceTypeCodeType):
    def __init__(self, CodeListAgencyIdentifier=None, valueOf_=None):
        super(InvoiceTypeCodeTypeSub, self).__init__(CodeListAgencyIdentifier, valueOf_, )
supermod.InvoiceTypeCodeType.subclass = InvoiceTypeCodeTypeSub
# end class InvoiceTypeCodeTypeSub


class PartialPaymentDetailsTypeSub(supermod.PartialPaymentDetailsType):
    def __init__(self, PaidAmount=None, PaidVatExcludedAmount=None, UnPaidAmount=None, UnPaidVatExcludedAmount=None, InterestPercent=None, ProsessingCostsAmount=None, PartialPaymentVatIncludedAmount=None, PartialPaymentVatExcludedAmount=None, PartialPaymentDueDate=None, PartialPaymentReferenceIdentifier=None):
        super(PartialPaymentDetailsTypeSub, self).__init__(PaidAmount, PaidVatExcludedAmount, UnPaidAmount, UnPaidVatExcludedAmount, InterestPercent, ProsessingCostsAmount, PartialPaymentVatIncludedAmount, PartialPaymentVatExcludedAmount, PartialPaymentDueDate, PartialPaymentReferenceIdentifier, )
supermod.PartialPaymentDetailsType.subclass = PartialPaymentDetailsTypeSub
# end class PartialPaymentDetailsTypeSub


class PaymentOverDueFineDetailsTypeSub(supermod.PaymentOverDueFineDetailsType):
    def __init__(self, PaymentOverDueFineFreeText=None, PaymentOverDueFinePercent=None, PaymentOverDueFixedAmount=None):
        super(PaymentOverDueFineDetailsTypeSub, self).__init__(PaymentOverDueFineFreeText, PaymentOverDueFinePercent, PaymentOverDueFixedAmount, )
supermod.PaymentOverDueFineDetailsType.subclass = PaymentOverDueFineDetailsTypeSub
# end class PaymentOverDueFineDetailsTypeSub


class PaymentStatusDetailsTypeSub(supermod.PaymentStatusDetailsType):
    def __init__(self, PaymentStatusCode=None, PaymentMethodText=None):
        super(PaymentStatusDetailsTypeSub, self).__init__(PaymentStatusCode, PaymentMethodText, )
supermod.PaymentStatusDetailsType.subclass = PaymentStatusDetailsTypeSub
# end class PaymentStatusDetailsTypeSub


class PaymentTermsDetailsTypeSub(supermod.PaymentTermsDetailsType):
    def __init__(self, PaymentTermsFreeText=None, InvoiceDueDate=None, CashDiscountDate=None, CashDiscountBaseAmount=None, CashDiscountPercent=None, CashDiscountAmount=None, CashDiscountExcludingVatAmount=None, CashDiscountVatDetails=None, ReducedInvoiceVatIncludedAmount=None, PaymentOverDueFineDetails=None):
        super(PaymentTermsDetailsTypeSub, self).__init__(PaymentTermsFreeText, InvoiceDueDate, CashDiscountDate, CashDiscountBaseAmount, CashDiscountPercent, CashDiscountAmount, CashDiscountExcludingVatAmount, CashDiscountVatDetails, ReducedInvoiceVatIncludedAmount, PaymentOverDueFineDetails, )
supermod.PaymentTermsDetailsType.subclass = PaymentTermsDetailsTypeSub
# end class PaymentTermsDetailsTypeSub


class RowDeliveryDetailsTypeSub(supermod.RowDeliveryDetailsType):
    def __init__(self, RowTerminalAddressText=None, RowWaybillIdentifier=None, RowWaybillTypeCode=None, RowClearanceIdentifier=None, RowDeliveryNoteIdentifier=None, RowDelivererIdentifier=None, RowDelivererName=None, RowDelivererCountryCode=None, RowDelivererCountryName=None, RowModeOfTransportIdentifier=None, RowCarrierName=None, RowVesselName=None, RowLocationIdentifier=None, RowTransportInformationDate=None, RowCountryOfOrigin=None, RowCountryOfDestinationName=None, RowDestinationCountryCode=None, RowPlaceOfDischarge=None, RowFinalDestinationName=None, RowCustomsInfo=None, RowManufacturerArticleIdentifier=None, RowManufacturerIdentifier=None, RowManufacturerName=None, RowManufacturerCountryCode=None, RowManufacturerCountryName=None, RowManufacturerOrderIdentifier=None, RowPackageDetails=None):
        super(RowDeliveryDetailsTypeSub, self).__init__(RowTerminalAddressText, RowWaybillIdentifier, RowWaybillTypeCode, RowClearanceIdentifier, RowDeliveryNoteIdentifier, RowDelivererIdentifier, RowDelivererName, RowDelivererCountryCode, RowDelivererCountryName, RowModeOfTransportIdentifier, RowCarrierName, RowVesselName, RowLocationIdentifier, RowTransportInformationDate, RowCountryOfOrigin, RowCountryOfDestinationName, RowDestinationCountryCode, RowPlaceOfDischarge, RowFinalDestinationName, RowCustomsInfo, RowManufacturerArticleIdentifier, RowManufacturerIdentifier, RowManufacturerName, RowManufacturerCountryCode, RowManufacturerCountryName, RowManufacturerOrderIdentifier, RowPackageDetails, )
supermod.RowDeliveryDetailsType.subclass = RowDeliveryDetailsTypeSub
# end class RowDeliveryDetailsTypeSub


class SellerAccountDetailsTypeSub(supermod.SellerAccountDetailsType):
    def __init__(self, SellerAccountID=None, SellerBic=None):
        super(SellerAccountDetailsTypeSub, self).__init__(SellerAccountID, SellerBic, )
supermod.SellerAccountDetailsType.subclass = SellerAccountDetailsTypeSub
# end class SellerAccountDetailsTypeSub


class SellerAccountIDTypeSub(supermod.SellerAccountIDType):
    def __init__(self, IdentificationSchemeName=None, valueOf_=None):
        super(SellerAccountIDTypeSub, self).__init__(IdentificationSchemeName, valueOf_, )
supermod.SellerAccountIDType.subclass = SellerAccountIDTypeSub
# end class SellerAccountIDTypeSub


class SellerBicTypeSub(supermod.SellerBicType):
    def __init__(self, IdentificationSchemeName=None, valueOf_=None):
        super(SellerBicTypeSub, self).__init__(IdentificationSchemeName, valueOf_, )
supermod.SellerBicType.subclass = SellerBicTypeSub
# end class SellerBicTypeSub


class SellerCommunicationDetailsTypeSub(supermod.SellerCommunicationDetailsType):
    def __init__(self, SellerPhoneNumberIdentifier=None, SellerEmailaddressIdentifier=None):
        super(SellerCommunicationDetailsTypeSub, self).__init__(SellerPhoneNumberIdentifier, SellerEmailaddressIdentifier, )
supermod.SellerCommunicationDetailsType.subclass = SellerCommunicationDetailsTypeSub
# end class SellerCommunicationDetailsTypeSub


class SellerInformationDetailsTypeSub(supermod.SellerInformationDetailsType):
    def __init__(self, SellerOfficialPostalAddressDetails=None, SellerHomeTownName=None, SellerVatRegistrationText=None, SellerVatRegistrationDate=None, SellerTaxRegistrationText=None, SellerPhoneNumber=None, SellerFaxNumber=None, SellerCommonEmailaddressIdentifier=None, SellerWebaddressIdentifier=None, SellerFreeText=None, SellerAccountDetails=None, InvoiceRecipientDetails=None):
        super(SellerInformationDetailsTypeSub, self).__init__(SellerOfficialPostalAddressDetails, SellerHomeTownName, SellerVatRegistrationText, SellerVatRegistrationDate, SellerTaxRegistrationText, SellerPhoneNumber, SellerFaxNumber, SellerCommonEmailaddressIdentifier, SellerWebaddressIdentifier, SellerFreeText, SellerAccountDetails, InvoiceRecipientDetails, )
supermod.SellerInformationDetailsType.subclass = SellerInformationDetailsTypeSub
# end class SellerInformationDetailsTypeSub


class SellerPartyDetailsTypeSub(supermod.SellerPartyDetailsType):
    def __init__(self, SellerPartyIdentifier=None, SellerPartyIdentifierUrlText=None, SellerOrganisationName=None, SellerOrganisationDepartment=None, SellerOrganisationTaxCode=None, SellerOrganisationTaxCodeUrlText=None, SellerCode=None, SellerPostalAddressDetails=None):
        super(SellerPartyDetailsTypeSub, self).__init__(SellerPartyIdentifier, SellerPartyIdentifierUrlText, SellerOrganisationName, SellerOrganisationDepartment, SellerOrganisationTaxCode, SellerOrganisationTaxCodeUrlText, SellerCode, SellerPostalAddressDetails, )
supermod.SellerPartyDetailsType.subclass = SellerPartyDetailsTypeSub
# end class SellerPartyDetailsTypeSub


class SellerPostalAddressDetailsTypeSub(supermod.SellerPostalAddressDetailsType):
    def __init__(self, SellerStreetName=None, SellerTownName=None, SellerPostCodeIdentifier=None, CountryCode=None, CountryName=None, SellerPostOfficeBoxIdentifier=None):
        super(SellerPostalAddressDetailsTypeSub, self).__init__(SellerStreetName, SellerTownName, SellerPostCodeIdentifier, CountryCode, CountryName, SellerPostOfficeBoxIdentifier, )
supermod.SellerPostalAddressDetailsType.subclass = SellerPostalAddressDetailsTypeSub
# end class SellerPostalAddressDetailsTypeSub


class AnyPartyCommunicationDetailsTypeSub(supermod.AnyPartyCommunicationDetailsType):
    def __init__(self, AnyPartyPhoneNumberIdentifier=None, AnyPartyEmailAddressIdentifier=None):
        super(AnyPartyCommunicationDetailsTypeSub, self).__init__(AnyPartyPhoneNumberIdentifier, AnyPartyEmailAddressIdentifier, )
supermod.AnyPartyCommunicationDetailsType.subclass = AnyPartyCommunicationDetailsTypeSub
# end class AnyPartyCommunicationDetailsTypeSub


class SpecificationDetailsTypeSub(supermod.SpecificationDetailsType):
    def __init__(self, SpecificationFreeText=None, ExternalSpecificationDetails=None):
        super(SpecificationDetailsTypeSub, self).__init__(SpecificationFreeText, ExternalSpecificationDetails, )
supermod.SpecificationDetailsType.subclass = SpecificationDetailsTypeSub
# end class SpecificationDetailsTypeSub


class ExternalSpecificationDetailsTypeSub(supermod.ExternalSpecificationDetailsType):
    def __init__(self, anytypeobjs_=None):
        super(ExternalSpecificationDetailsTypeSub, self).__init__(anytypeobjs_, )
supermod.ExternalSpecificationDetailsType.subclass = ExternalSpecificationDetailsTypeSub
# end class ExternalSpecificationDetailsTypeSub


class SubInvoiceRowTypeSub(supermod.SubInvoiceRowType):
    def __init__(self, SubIdentifier=None, SubRowPositionIdentifier=None, SubArticleIdentifier=None, SubArticleGroupIdentifier=None, SubArticleName=None, SubArticleInfoUrlText=None, SubBuyerArticleIdentifier=None, SubEanCode=None, SubRowRegistrationNumberIdentifier=None, SubSerialNumberIdentifier=None, SubRowActionCode=None, SubRowDefinitionDetails=None, SubOfferedQuantity=None, SubDeliveredQuantity=None, SubOrderedQuantity=None, SubConfirmedQuantity=None, SubPostDeliveredQuantity=None, SubInvoicedQuantity=None, SubCreditRequestedQuantity=None, SubReturnedQuantity=None, SubStartDate=None, SubEndDate=None, SubUnitPriceAmount=None, SubUnitPriceVatIncludedAmount=None, SubUnitPriceBaseQuantity=None, SubRowIdentifier=None, SubRowIdentifierUrlText=None, SubRowIdentifierDate=None, SubRowOrdererName=None, SubRowSalesPersonName=None, SubRowOrderConfirmationIdentifier=None, SubRowOrderConfirmationDate=None, SubOriginalInvoiceNumber=None, SubRowDeliveryIdentifier=None, SubRowDeliveryIdentifierUrlText=None, SubRowDeliveryDate=None, SubRowQuotationIdentifier=None, SubRowQuotationIdentifierUrlText=None, SubRowAgreementIdentifier=None, SubRowAgreementIdentifierUrlText=None, SubRowRequestOfQuotationIdentifier=None, SubRowRequestOfQuotationIdentifierUrlText=None, SubRowPriceListIdentifier=None, SubRowPriceListIdentifierUrlText=None, SubRowProjectReferenceIdentifier=None, SubRowOverDuePaymentDetails=None, SubRowAnyPartyDetails=None, SubRowDeliveryDetails=None, SubRowShortProposedAccountIdentifier=None, SubRowNormalProposedAccountIdentifier=None, SubRowProposedAccountText=None, SubRowAccountDimensionText=None, SubRowSellerAccountText=None, SubRowFreeText=None, SubRowUsedQuantity=None, SubRowPreviousMeterReadingDate=None, SubRowLatestMeterReadingDate=None, SubRowCalculatedQuantity=None, SubRowAveragePriceAmount=None, SubRowDiscountPercent=None, SubRowDiscountAmount=None, SubRowDiscountTypeCode=None, SubRowDiscountTypeText=None, SubRowProgressiveDiscountDetails=None, SubRowVatRatePercent=None, SubRowVatCode=None, SubRowVatAmount=None, SubRowVatExcludedAmount=None, SubRowAmount=None, SubRowTransactionDetails=None):
        super(SubInvoiceRowTypeSub, self).__init__(SubIdentifier, SubRowPositionIdentifier, SubArticleIdentifier, SubArticleGroupIdentifier, SubArticleName, SubArticleInfoUrlText, SubBuyerArticleIdentifier, SubEanCode, SubRowRegistrationNumberIdentifier, SubSerialNumberIdentifier, SubRowActionCode, SubRowDefinitionDetails, SubOfferedQuantity, SubDeliveredQuantity, SubOrderedQuantity, SubConfirmedQuantity, SubPostDeliveredQuantity, SubInvoicedQuantity, SubCreditRequestedQuantity, SubReturnedQuantity, SubStartDate, SubEndDate, SubUnitPriceAmount, SubUnitPriceVatIncludedAmount, SubUnitPriceBaseQuantity, SubRowIdentifier, SubRowIdentifierUrlText, SubRowIdentifierDate, SubRowOrdererName, SubRowSalesPersonName, SubRowOrderConfirmationIdentifier, SubRowOrderConfirmationDate, SubOriginalInvoiceNumber, SubRowDeliveryIdentifier, SubRowDeliveryIdentifierUrlText, SubRowDeliveryDate, SubRowQuotationIdentifier, SubRowQuotationIdentifierUrlText, SubRowAgreementIdentifier, SubRowAgreementIdentifierUrlText, SubRowRequestOfQuotationIdentifier, SubRowRequestOfQuotationIdentifierUrlText, SubRowPriceListIdentifier, SubRowPriceListIdentifierUrlText, SubRowProjectReferenceIdentifier, SubRowOverDuePaymentDetails, SubRowAnyPartyDetails, SubRowDeliveryDetails, SubRowShortProposedAccountIdentifier, SubRowNormalProposedAccountIdentifier, SubRowProposedAccountText, SubRowAccountDimensionText, SubRowSellerAccountText, SubRowFreeText, SubRowUsedQuantity, SubRowPreviousMeterReadingDate, SubRowLatestMeterReadingDate, SubRowCalculatedQuantity, SubRowAveragePriceAmount, SubRowDiscountPercent, SubRowDiscountAmount, SubRowDiscountTypeCode, SubRowDiscountTypeText, SubRowProgressiveDiscountDetails, SubRowVatRatePercent, SubRowVatCode, SubRowVatAmount, SubRowVatExcludedAmount, SubRowAmount, SubRowTransactionDetails, )
supermod.SubInvoiceRowType.subclass = SubInvoiceRowTypeSub
# end class SubInvoiceRowTypeSub


class SubRowDeliveryDetailsTypeSub(supermod.SubRowDeliveryDetailsType):
    def __init__(self, SubRowTerminalAddressText=None, SubRowWaybillIdentifier=None, SubRowWaybillTypeCode=None, SubRowClearanceIdentifier=None, SubRowDeliveryNoteIdentifier=None, SubRowDelivererIdentifier=None, SubRowDelivererName=None, SubRowDelivererCountryCode=None, SubRowDelivererCountryName=None, SubRowPlaceOfDischarge=None, SubRowFinalDestinationName=None, SubRowCustomsInfo=None, SubRowManufacturerArticleIdentifier=None, SubRowManufacturerIdentifier=None, SubRowManufacturerName=None, SubRowManufacturerCountryCode=None, SubRowManufacturerCountryName=None, SubRowManufacturerOrderIdentifier=None, SubRowPackageDetails=None):
        super(SubRowDeliveryDetailsTypeSub, self).__init__(SubRowTerminalAddressText, SubRowWaybillIdentifier, SubRowWaybillTypeCode, SubRowClearanceIdentifier, SubRowDeliveryNoteIdentifier, SubRowDelivererIdentifier, SubRowDelivererName, SubRowDelivererCountryCode, SubRowDelivererCountryName, SubRowPlaceOfDischarge, SubRowFinalDestinationName, SubRowCustomsInfo, SubRowManufacturerArticleIdentifier, SubRowManufacturerIdentifier, SubRowManufacturerName, SubRowManufacturerCountryCode, SubRowManufacturerCountryName, SubRowManufacturerOrderIdentifier, SubRowPackageDetails, )
supermod.SubRowDeliveryDetailsType.subclass = SubRowDeliveryDetailsTypeSub
# end class SubRowDeliveryDetailsTypeSub


class VatSpecificationDetailsTypeSub(supermod.VatSpecificationDetailsType):
    def __init__(self, VatBaseAmount=None, VatRatePercent=None, VatCode=None, VatRateAmount=None, VatFreeText=None):
        super(VatSpecificationDetailsTypeSub, self).__init__(VatBaseAmount, VatRatePercent, VatCode, VatRateAmount, VatFreeText, )
supermod.VatSpecificationDetailsType.subclass = VatSpecificationDetailsTypeSub
# end class VatSpecificationDetailsTypeSub


class PartyIdentifierTypeSub(supermod.PartyIdentifierType):
    def __init__(self, IdentifierType=None, valueOf_=None):
        super(PartyIdentifierTypeSub, self).__init__(IdentifierType, valueOf_, )
supermod.PartyIdentifierType.subclass = PartyIdentifierTypeSub
# end class PartyIdentifierTypeSub


class DiscountDetailsTypeSub(supermod.DiscountDetailsType):
    def __init__(self, FreeText=None, Percent=None, Amount=None):
        super(DiscountDetailsTypeSub, self).__init__(FreeText, Percent, Amount, )
supermod.DiscountDetailsType.subclass = DiscountDetailsTypeSub
# end class DiscountDetailsTypeSub


class CustomsInfoTypeSub(supermod.CustomsInfoType):
    def __init__(self, CNCode=None, CNName=None, CNOriginCountryCode=None, CNOriginCountryName=None):
        super(CustomsInfoTypeSub, self).__init__(CNCode, CNName, CNOriginCountryCode, CNOriginCountryName, )
supermod.CustomsInfoType.subclass = CustomsInfoTypeSub
# end class CustomsInfoTypeSub


class TransactionDetailsTypeSub(supermod.TransactionDetailsType):
    def __init__(self, OtherCurrencyAmount=None, ExchangeRate=None, ExchangeDate=None):
        super(TransactionDetailsTypeSub, self).__init__(OtherCurrencyAmount, ExchangeRate, ExchangeDate, )
supermod.TransactionDetailsType.subclass = TransactionDetailsTypeSub
# end class TransactionDetailsTypeSub


class AttachmentMessageDetailsTypeSub(supermod.AttachmentMessageDetailsType):
    def __init__(self, AttachmentMessageIdentifier=None):
        super(AttachmentMessageDetailsTypeSub, self).__init__(AttachmentMessageIdentifier, )
supermod.AttachmentMessageDetailsType.subclass = AttachmentMessageDetailsTypeSub
# end class AttachmentMessageDetailsTypeSub


class QuantityTypeSub(supermod.QuantityType):
    def __init__(self, QuantityUnitCode=None, valueOf_=None, extensiontype_=None):
        super(QuantityTypeSub, self).__init__(QuantityUnitCode, valueOf_, extensiontype_, )
supermod.QuantityType.subclass = QuantityTypeSub
# end class QuantityTypeSub


class QuantityType0_14Sub(supermod.QuantityType0_14):
    def __init__(self, QuantityUnitCode=None, valueOf_=None):
        super(QuantityType0_14Sub, self).__init__(QuantityUnitCode, valueOf_, )
supermod.QuantityType0_14.subclass = QuantityType0_14Sub
# end class QuantityType0_14Sub


class QuantityType0_70Sub(supermod.QuantityType0_70):
    def __init__(self, QuantityUnitCode=None, valueOf_=None):
        super(QuantityType0_70Sub, self).__init__(QuantityUnitCode, valueOf_, )
supermod.QuantityType0_70.subclass = QuantityType0_70Sub
# end class QuantityType0_70Sub


class AnyPartyTextTypeSub(supermod.AnyPartyTextType):
    def __init__(self, AnyPartyCode=None, valueOf_=None, extensiontype_=None):
        super(AnyPartyTextTypeSub, self).__init__(AnyPartyCode, valueOf_, extensiontype_, )
supermod.AnyPartyTextType.subclass = AnyPartyTextTypeSub
# end class AnyPartyTextTypeSub


class anypartytexttype0_35Sub(supermod.anypartytexttype0_35):
    def __init__(self, AnyPartyCode=None, valueOf_=None):
        super(anypartytexttype0_35Sub, self).__init__(AnyPartyCode, valueOf_, )
supermod.anypartytexttype0_35.subclass = anypartytexttype0_35Sub
# end class anypartytexttype0_35Sub


class dateSub(supermod.date):
    def __init__(self, Format=None, valueOf_=None):
        super(dateSub, self).__init__(Format, valueOf_, )
supermod.date.subclass = dateSub
# end class dateSub


class amountSub(supermod.amount):
    def __init__(self, AmountCurrencyIdentifier=None, valueOf_=None):
        super(amountSub, self).__init__(AmountCurrencyIdentifier, valueOf_, )
supermod.amount.subclass = amountSub
# end class amountSub


class epiAmountSub(supermod.epiAmount):
    def __init__(self, AmountCurrencyIdentifier=None, valueOf_=None):
        super(epiAmountSub, self).__init__(AmountCurrencyIdentifier, valueOf_, )
supermod.epiAmount.subclass = epiAmountSub
# end class epiAmountSub


class unitAmountSub(supermod.unitAmount):
    def __init__(self, AmountCurrencyIdentifier=None, UnitPriceUnitCode=None, valueOf_=None):
        super(unitAmountSub, self).__init__(AmountCurrencyIdentifier, UnitPriceUnitCode, valueOf_, )
supermod.unitAmount.subclass = unitAmountSub
# end class unitAmountSub


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
    def __init__(self, MessageIdentifier=None, MessageTimeStamp=None, RefToMessageIdentifier=None, ImplementationCode=None):
        super(MessageDetailsTypeSub, self).__init__(MessageIdentifier, MessageTimeStamp, RefToMessageIdentifier, ImplementationCode, )
supermod.MessageDetailsType.subclass = MessageDetailsTypeSub
# end class MessageDetailsTypeSub


class AnyPartyPostalAddressDetailsTypeSub(supermod.AnyPartyPostalAddressDetailsType):
    def __init__(self, AnyPartyStreetName=None, AnyPartyTownName=None, AnyPartyPostCodeIdentifier=None, CountryCode=None, CountryName=None, AnyPartyPostOfficeBoxIdentifier=None):
        super(AnyPartyPostalAddressDetailsTypeSub, self).__init__(AnyPartyStreetName, AnyPartyTownName, AnyPartyPostCodeIdentifier, CountryCode, CountryName, AnyPartyPostOfficeBoxIdentifier, )
supermod.AnyPartyPostalAddressDetailsType.subclass = AnyPartyPostalAddressDetailsTypeSub
# end class AnyPartyPostalAddressDetailsTypeSub


class FactoringPartyPostalAddressDetailsTypeSub(supermod.FactoringPartyPostalAddressDetailsType):
    def __init__(self, FactoringPartyStreetName=None, FactoringPartyTownName=None, FactoringPartyPostCodeIdentifier=None, CountryCode=None, CountryName=None, FactoringPartyPostOfficeBoxIdentifier=None):
        super(FactoringPartyPostalAddressDetailsTypeSub, self).__init__(FactoringPartyStreetName, FactoringPartyTownName, FactoringPartyPostCodeIdentifier, CountryCode, CountryName, FactoringPartyPostOfficeBoxIdentifier, )
supermod.FactoringPartyPostalAddressDetailsType.subclass = FactoringPartyPostalAddressDetailsTypeSub
# end class FactoringPartyPostalAddressDetailsTypeSub


class ShipmentPartyDetailsTypeSub(supermod.ShipmentPartyDetailsType):
    def __init__(self, ShipmentPartyIdentifier=None, ShipmentOrganisationName=None, ShipmentOrganisationDepartment=None, ShipmentOrganisationTaxCode=None, ShipmentCode=None, ShipmentPostalAddressDetails=None, ShipmentSiteCode=None):
        super(ShipmentPartyDetailsTypeSub, self).__init__(ShipmentPartyIdentifier, ShipmentOrganisationName, ShipmentOrganisationDepartment, ShipmentOrganisationTaxCode, ShipmentCode, ShipmentPostalAddressDetails, ShipmentSiteCode, )
supermod.ShipmentPartyDetailsType.subclass = ShipmentPartyDetailsTypeSub
# end class ShipmentPartyDetailsTypeSub


class ShipmentPostalAddressDetailsTypeSub(supermod.ShipmentPostalAddressDetailsType):
    def __init__(self, ShipmentStreetName=None, ShipmentTownName=None, ShipmentPostCodeIdentifier=None, CountryCode=None, CountryName=None, ShipmentPostOfficeBoxIdentifier=None):
        super(ShipmentPostalAddressDetailsTypeSub, self).__init__(ShipmentStreetName, ShipmentTownName, ShipmentPostCodeIdentifier, CountryCode, CountryName, ShipmentPostOfficeBoxIdentifier, )
supermod.ShipmentPostalAddressDetailsType.subclass = ShipmentPostalAddressDetailsTypeSub
# end class ShipmentPostalAddressDetailsTypeSub


class PackageDetailsTypeSub(supermod.PackageDetailsType):
    def __init__(self, PackageLength=None, PackageWidth=None, PackageHeight=None, PackageWeight=None, PackageNetWeight=None, PackageVolume=None, TransportCarriageQuantity=None):
        super(PackageDetailsTypeSub, self).__init__(PackageLength, PackageWidth, PackageHeight, PackageWeight, PackageNetWeight, PackageVolume, TransportCarriageQuantity, )
supermod.PackageDetailsType.subclass = PackageDetailsTypeSub
# end class PackageDetailsTypeSub


class DefinitionDetailsTypeSub(supermod.DefinitionDetailsType):
    def __init__(self, DefinitionHeaderText=None, DefinitionValue=None):
        super(DefinitionDetailsTypeSub, self).__init__(DefinitionHeaderText, DefinitionValue, )
supermod.DefinitionDetailsType.subclass = DefinitionDetailsTypeSub
# end class DefinitionDetailsTypeSub


class DefinitionHeaderTextTypeSub(supermod.DefinitionHeaderTextType):
    def __init__(self, DefinitionCode=None, valueOf_=None):
        super(DefinitionHeaderTextTypeSub, self).__init__(DefinitionCode, valueOf_, )
supermod.DefinitionHeaderTextType.subclass = DefinitionHeaderTextTypeSub
# end class DefinitionHeaderTextTypeSub


class RowDefinitionDetailsTypeSub(supermod.RowDefinitionDetailsType):
    def __init__(self, RowDefinitionHeaderText=None, RowDefinitionValue=None):
        super(RowDefinitionDetailsTypeSub, self).__init__(RowDefinitionHeaderText, RowDefinitionValue, )
supermod.RowDefinitionDetailsType.subclass = RowDefinitionDetailsTypeSub
# end class RowDefinitionDetailsTypeSub


class RowDefinitionHeaderTextTypeSub(supermod.RowDefinitionHeaderTextType):
    def __init__(self, DefinitionCode=None, valueOf_=None):
        super(RowDefinitionHeaderTextTypeSub, self).__init__(DefinitionCode, valueOf_, )
supermod.RowDefinitionHeaderTextType.subclass = RowDefinitionHeaderTextTypeSub
# end class RowDefinitionHeaderTextTypeSub


class RowOverDuePaymentDetailsTypeSub(supermod.RowOverDuePaymentDetailsType):
    def __init__(self, RowOriginalInvoiceIdentifier=None, RowOriginalInvoiceDate=None, RowOriginalDueDate=None, RowOriginalInvoiceTotalAmount=None, RowOriginalEpiRemittanceInfoIdentifier=None, RowPaidVatExcludedAmount=None, RowPaidVatIncludedAmount=None, RowPaidDate=None, RowUnPaidVatExcludedAmount=None, RowUnPaidVatIncludedAmount=None, RowCollectionDate=None, RowCollectionQuantity=None, RowCollectionChargeAmount=None, RowInterestRate=None, RowInterestStartDate=None, RowInterestEndDate=None, RowInterestPeriodText=None, RowInterestDateNumber=None, RowInterestChargeAmount=None, RowInterestChargeVatAmount=None):
        super(RowOverDuePaymentDetailsTypeSub, self).__init__(RowOriginalInvoiceIdentifier, RowOriginalInvoiceDate, RowOriginalDueDate, RowOriginalInvoiceTotalAmount, RowOriginalEpiRemittanceInfoIdentifier, RowPaidVatExcludedAmount, RowPaidVatIncludedAmount, RowPaidDate, RowUnPaidVatExcludedAmount, RowUnPaidVatIncludedAmount, RowCollectionDate, RowCollectionQuantity, RowCollectionChargeAmount, RowInterestRate, RowInterestStartDate, RowInterestEndDate, RowInterestPeriodText, RowInterestDateNumber, RowInterestChargeAmount, RowInterestChargeVatAmount, )
supermod.RowOverDuePaymentDetailsType.subclass = RowOverDuePaymentDetailsTypeSub
# end class RowOverDuePaymentDetailsTypeSub


class RowAnyPartyDetailsTypeSub(supermod.RowAnyPartyDetailsType):
    def __init__(self, RowAnyPartyText=None, RowAnyPartyIdentifier=None, RowAnyPartyOrganisationName=None, RowAnyPartyOrganisationDepartment=None, RowAnyPartyOrganisationTaxCode=None, RowAnyPartyPostalAddressDetails=None, RowAnyPartyOrganisationUnitNumber=None, RowAnyPartySiteCode=None):
        super(RowAnyPartyDetailsTypeSub, self).__init__(RowAnyPartyText, RowAnyPartyIdentifier, RowAnyPartyOrganisationName, RowAnyPartyOrganisationDepartment, RowAnyPartyOrganisationTaxCode, RowAnyPartyPostalAddressDetails, RowAnyPartyOrganisationUnitNumber, RowAnyPartySiteCode, )
supermod.RowAnyPartyDetailsType.subclass = RowAnyPartyDetailsTypeSub
# end class RowAnyPartyDetailsTypeSub


class RowAnyPartyPostalAddressDetailsTypeSub(supermod.RowAnyPartyPostalAddressDetailsType):
    def __init__(self, RowAnyPartyStreetName=None, RowAnyPartyTownName=None, RowAnyPartyPostCodeIdentifier=None, CountryCode=None, CountryName=None, RowAnyPartyPostOfficeBoxIdentifier=None):
        super(RowAnyPartyPostalAddressDetailsTypeSub, self).__init__(RowAnyPartyStreetName, RowAnyPartyTownName, RowAnyPartyPostCodeIdentifier, CountryCode, CountryName, RowAnyPartyPostOfficeBoxIdentifier, )
supermod.RowAnyPartyPostalAddressDetailsType.subclass = RowAnyPartyPostalAddressDetailsTypeSub
# end class RowAnyPartyPostalAddressDetailsTypeSub


class RowProgressiveDiscountDetailsTypeSub(supermod.RowProgressiveDiscountDetailsType):
    def __init__(self, RowDiscountPercent=None, RowDiscountAmount=None, RowDiscountTypeCode=None, RowDiscountTypeText=None):
        super(RowProgressiveDiscountDetailsTypeSub, self).__init__(RowDiscountPercent, RowDiscountAmount, RowDiscountTypeCode, RowDiscountTypeText, )
supermod.RowProgressiveDiscountDetailsType.subclass = RowProgressiveDiscountDetailsTypeSub
# end class RowProgressiveDiscountDetailsTypeSub


class CashDiscountVatDetailsTypeSub(supermod.CashDiscountVatDetailsType):
    def __init__(self, CashDiscountVatPercent=None, CashDiscountVatAmount=None):
        super(CashDiscountVatDetailsTypeSub, self).__init__(CashDiscountVatPercent, CashDiscountVatAmount, )
supermod.CashDiscountVatDetailsType.subclass = CashDiscountVatDetailsTypeSub
# end class CashDiscountVatDetailsTypeSub


class RowPackageDetailsTypeSub(supermod.RowPackageDetailsType):
    def __init__(self, RowPackageLength=None, RowPackageWidth=None, RowPackageHeight=None, RowPackageWeight=None, RowPackageNetWeight=None, RowPackageVolume=None, RowTransportCarriageQuantity=None):
        super(RowPackageDetailsTypeSub, self).__init__(RowPackageLength, RowPackageWidth, RowPackageHeight, RowPackageWeight, RowPackageNetWeight, RowPackageVolume, RowTransportCarriageQuantity, )
supermod.RowPackageDetailsType.subclass = RowPackageDetailsTypeSub
# end class RowPackageDetailsTypeSub


class SellerOfficialPostalAddressDetailsTypeSub(supermod.SellerOfficialPostalAddressDetailsType):
    def __init__(self, SellerOfficialStreetName=None, SellerOfficialTownName=None, SellerOfficialPostCodeIdentifier=None, CountryCode=None, CountryName=None):
        super(SellerOfficialPostalAddressDetailsTypeSub, self).__init__(SellerOfficialStreetName, SellerOfficialTownName, SellerOfficialPostCodeIdentifier, CountryCode, CountryName, )
supermod.SellerOfficialPostalAddressDetailsType.subclass = SellerOfficialPostalAddressDetailsTypeSub
# end class SellerOfficialPostalAddressDetailsTypeSub


class SubRowDefinitionDetailsTypeSub(supermod.SubRowDefinitionDetailsType):
    def __init__(self, SubRowDefinitionHeaderText=None, SubRowDefinitionValue=None):
        super(SubRowDefinitionDetailsTypeSub, self).__init__(SubRowDefinitionHeaderText, SubRowDefinitionValue, )
supermod.SubRowDefinitionDetailsType.subclass = SubRowDefinitionDetailsTypeSub
# end class SubRowDefinitionDetailsTypeSub


class SubRowDefinitionHeaderTextTypeSub(supermod.SubRowDefinitionHeaderTextType):
    def __init__(self, DefinitionCode=None, valueOf_=None):
        super(SubRowDefinitionHeaderTextTypeSub, self).__init__(DefinitionCode, valueOf_, )
supermod.SubRowDefinitionHeaderTextType.subclass = SubRowDefinitionHeaderTextTypeSub
# end class SubRowDefinitionHeaderTextTypeSub


class SubRowOverDuePaymentDetailsTypeSub(supermod.SubRowOverDuePaymentDetailsType):
    def __init__(self, SubRowOriginalInvoiceIdentifier=None, SubRowOriginalInvoiceDate=None, SubRowOriginalDueDate=None, SubRowOriginalInvoiceTotalAmount=None, SubRowOriginalEpiRemittanceInfoIdentifier=None, SubRowPaidVatExcludedAmount=None, SubRowPaidVatIncludedAmount=None, SubRowPaidDate=None, SubRowUnPaidVatExcludedAmount=None, SubRowUnPaidVatIncludedAmount=None, SubRowCollectionDate=None, SubRowCollectionQuantity=None, SubRowCollectionChargeAmount=None, SubRowInterestRate=None, SubRowInterestStartDate=None, SubRowInterestEndDate=None, SubRowInterestPeriodText=None, SubRowInterestDateNumber=None, SubRowInterestChargeAmount=None, SubRowInterestChargeVatAmount=None):
        super(SubRowOverDuePaymentDetailsTypeSub, self).__init__(SubRowOriginalInvoiceIdentifier, SubRowOriginalInvoiceDate, SubRowOriginalDueDate, SubRowOriginalInvoiceTotalAmount, SubRowOriginalEpiRemittanceInfoIdentifier, SubRowPaidVatExcludedAmount, SubRowPaidVatIncludedAmount, SubRowPaidDate, SubRowUnPaidVatExcludedAmount, SubRowUnPaidVatIncludedAmount, SubRowCollectionDate, SubRowCollectionQuantity, SubRowCollectionChargeAmount, SubRowInterestRate, SubRowInterestStartDate, SubRowInterestEndDate, SubRowInterestPeriodText, SubRowInterestDateNumber, SubRowInterestChargeAmount, SubRowInterestChargeVatAmount, )
supermod.SubRowOverDuePaymentDetailsType.subclass = SubRowOverDuePaymentDetailsTypeSub
# end class SubRowOverDuePaymentDetailsTypeSub


class SubRowAnyPartyDetailsTypeSub(supermod.SubRowAnyPartyDetailsType):
    def __init__(self, SubRowAnyPartyText=None, SubRowAnyPartyIdentifier=None, SubRowAnyPartyOrganisationName=None, SubRowAnyPartyOrganisationDepartment=None, SubRowAnyPartyOrganisationTaxCode=None, SubRowAnyPartyPostalAddressDetails=None, SubRowAnyPartyOrganisationUnitNumber=None, SubRowAnyPartySiteCode=None):
        super(SubRowAnyPartyDetailsTypeSub, self).__init__(SubRowAnyPartyText, SubRowAnyPartyIdentifier, SubRowAnyPartyOrganisationName, SubRowAnyPartyOrganisationDepartment, SubRowAnyPartyOrganisationTaxCode, SubRowAnyPartyPostalAddressDetails, SubRowAnyPartyOrganisationUnitNumber, SubRowAnyPartySiteCode, )
supermod.SubRowAnyPartyDetailsType.subclass = SubRowAnyPartyDetailsTypeSub
# end class SubRowAnyPartyDetailsTypeSub


class SubRowAnyPartyPostalAddressDetailsTypeSub(supermod.SubRowAnyPartyPostalAddressDetailsType):
    def __init__(self, SubRowAnyPartyStreetName=None, SubRowAnyPartyTownName=None, SubRowAnyPartyPostCodeIdentifier=None, CountryCode=None, CountryName=None, SubRowAnyPartyPostOfficeBoxIdentifier=None):
        super(SubRowAnyPartyPostalAddressDetailsTypeSub, self).__init__(SubRowAnyPartyStreetName, SubRowAnyPartyTownName, SubRowAnyPartyPostCodeIdentifier, CountryCode, CountryName, SubRowAnyPartyPostOfficeBoxIdentifier, )
supermod.SubRowAnyPartyPostalAddressDetailsType.subclass = SubRowAnyPartyPostalAddressDetailsTypeSub
# end class SubRowAnyPartyPostalAddressDetailsTypeSub


class SubRowProgressiveDiscountDetailsTypeSub(supermod.SubRowProgressiveDiscountDetailsType):
    def __init__(self, SubRowDiscountPercent=None, SubRowDiscountAmount=None, SubRowDiscountTypeCode=None, SubRowDiscountTypeText=None):
        super(SubRowProgressiveDiscountDetailsTypeSub, self).__init__(SubRowDiscountPercent, SubRowDiscountAmount, SubRowDiscountTypeCode, SubRowDiscountTypeText, )
supermod.SubRowProgressiveDiscountDetailsType.subclass = SubRowProgressiveDiscountDetailsTypeSub
# end class SubRowProgressiveDiscountDetailsTypeSub


class SubRowPackageDetailsTypeSub(supermod.SubRowPackageDetailsType):
    def __init__(self, SubRowPackageLength=None, SubRowPackageWidth=None, SubRowPackageHeight=None, SubRowPackageWeight=None, SubRowPackageNetWeight=None, SubRowPackageVolume=None, SubRowTransportCarriageQuantity=None):
        super(SubRowPackageDetailsTypeSub, self).__init__(SubRowPackageLength, SubRowPackageWidth, SubRowPackageHeight, SubRowPackageWeight, SubRowPackageNetWeight, SubRowPackageVolume, SubRowTransportCarriageQuantity, )
supermod.SubRowPackageDetailsType.subclass = SubRowPackageDetailsTypeSub
# end class SubRowPackageDetailsTypeSub


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
        rootTag = 'Finvoice'
        rootClass = supermod.Finvoice
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
        rootTag = 'Finvoice'
        rootClass = supermod.Finvoice
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
        rootTag = 'Finvoice'
        rootClass = supermod.Finvoice
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
        rootTag = 'Finvoice'
        rootClass = supermod.Finvoice
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
