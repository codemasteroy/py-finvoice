#!/usr/bin/env python
# -*- coding: iso8859-15 -*-

import sys
import datetime

reload(sys)

sys.setdefaultencoding("iso8859-15")

from finvoice.sender.senderinfo import ExternalEncoding
from finvoice.sender.senderinfo import FinvoiceSenderInfo
from finvoice.sender.senderinfo import MessageDetailsType
from finvoice.sender.senderinfo import SellerPartyDetailsType
from finvoice.sender.senderinfo import SellerPostalAddressDetailsType
from finvoice.sender.senderinfo import SellerOrganisationNamesType
from finvoice.sender.senderinfo import InvoiceSenderInformationDetailsType
from finvoice.sender.senderinfo import SellerAccountDetailsType
from finvoice.sender.senderinfo import SellerAccountIDType
from finvoice.sender.senderinfo import SellerBicType
from finvoice.sender.senderinfo import SellerInvoiceDetailsType
from finvoice.sender.senderinfo import SellerInvoiceTypeDetailsType
from finvoice.sender.senderinfo import SellerInvoiceTypeTextType
from finvoice.sender.senderinfo import SellerInvoiceIdentifierTextType
from finvoice.sender.senderinfo import date

# Date
nowDate = date( "CCYYMMDD", datetime.datetime.now().date().strftime("%Y%m%d") )

# Seller Postal Address
# SellerStreetName=None, SellerTownName=None, SellerPostCodeIdentifier=None, CountryCode=None, CountryName=None, SellerPostOfficeBoxIdentifier=None
sellerPostalAddress = SellerPostalAddressDetailsType( "Puukatu 2 F", "HELSINKI", 00112, "FI", "Suomi" )

# Seller Organization Name
# LanguageCode=None, SellerOrganisationName=None
sellerOrganisationNamesFi = SellerOrganisationNamesType( "FI" )
sellerOrganisationNamesFi.add_SellerOrganisationName( "Pullis Musiken Oy" )
sellerOrganisationNamesSv = SellerOrganisationNamesType( "SV" )
sellerOrganisationNamesSv.add_SellerOrganisationName( "Pullis Musiken Ab" )
sellerOrganisationNamesEn = SellerOrganisationNamesType( "EN" )
sellerOrganisationNamesEn.add_SellerOrganisationName( "Pullis Musiken Ltd" )

# SellerAccountID=None, SellerBic=None, NewSellerAccountID=None, NewSellerBic=None
sellerAccountDetailsOKOYFIHH = SellerAccountDetailsType( SellerAccountIDType( "IBAN", "FI2757800750155448" ), SellerBicType( "BIC", "OKOYFIHH" ) )
sellerAccountDetailsNDEAFIHH = SellerAccountDetailsType( SellerAccountIDType( "IBAN", "FI2721221222212227" ), SellerBicType( "BIC", "NDEAFIHH" ) )
sellerAccountDetailsNDEAFIHH = SellerAccountDetailsType( SellerAccountIDType( "IBAN", "FI2781232323312334" ), SellerBicType( "BIC", "PSPBFIHH" ) )

# Sender Information
# Version=None, MessageDetails=None, SellerPartyDetails=None, SellerOrganisationUnitNumber=None, InvoiceSenderInformationDetails=None,
# SellerAccountDetails=None, SellerInvoiceDetails=None, ProposedDueDateAccepted=None, ProposedInvoicePeriodAccepted=None
senderInfo = FinvoiceSenderInfo( "2.0" )

# Message Details
# MessageTypeCode=None, MessageTypeText=None, MessageActionCode=None, MessageActionCodeIdentifier=None, MessageDate=None, SenderInfoIdentifier=None
senderInfo.set_MessageDetails( MessageDetailsType( "SENDERINFO", "Sender information", "ADD", "00", nowDate, "001" ) )

# Seller Party Details
# SellerPartyIdentifier=None, SellerOrganisationNames=None, SellerOrganisationBankName=None, SellerPostalAddressDetails=None, IndustryCode=None
sellerPartyDetails = SellerPartyDetailsType( "0199920-7", None, None, sellerPostalAddress, 62020 )
sellerPartyDetails.add_SellerOrganisationNames( sellerOrganisationNamesFi )
sellerPartyDetails.add_SellerOrganisationNames( sellerOrganisationNamesSv )
sellerPartyDetails.add_SellerOrganisationNames( sellerOrganisationNamesEn )

senderInfo.set_SellerPartyDetails( sellerPartyDetails )

# SellerWebaddressNameText=None, SellerWebaddressText=None, InvoiceSenderAddress=None, InvoiceSenderIntermediatorAddress=None, NewInvoiceSenderAddress=None, NewInvoiceSenderIntermediatorAddress=None
senderInfo.set_InvoiceSenderInformationDetails( InvoiceSenderInformationDetailsType( "Pullin Musiikki Oy", "https://www.pullinmusiikki.fi/", "00371999207", "OKOYFIHH" ) )

senderInfo.add_SellerAccountDetails( sellerAccountDetailsOKOYFIHH )
senderInfo.add_SellerAccountDetails( sellerAccountDetailsNDEAFIHH )

# SellerInvoiceTypeText=None, SellerInvoiceIdentifierText=None
sellerInvoiceTypeDetailsFi = SellerInvoiceTypeDetailsType( SellerInvoiceTypeTextType( "FI", "Kirjanpito palvelu" ) )
sellerInvoiceTypeDetailsSv = SellerInvoiceTypeDetailsType( SellerInvoiceTypeTextType( "SV", "Bokföring tjänster" ) )
sellerInvoiceTypeDetailsEn = SellerInvoiceTypeDetailsType( SellerInvoiceTypeTextType( "EN", "Bookkeeping service" ) )

#LanguageCode=None, SellerInvoiceIdentifierType=None, SellerInvoiceIdentifierMinLength=1, SellerInvoiceIdentifierHyphens=False, SellerInvoiceIdentifierSpaces=False, SellerInvoiceIdentifierMaxLength=35, valueOf_=None, extensiontype_=None
sellerInvoiceTypeDetailsFi.add_SellerInvoiceIdentifierText( SellerInvoiceIdentifierTextType( "FI", "02", None, None, None, None, "Viitenumero" ) )
sellerInvoiceTypeDetailsFi.add_SellerInvoiceIdentifierText( SellerInvoiceIdentifierTextType( "FI", "09", 10, True, False, 10, "Asiakasnumero" ) )

sellerInvoiceTypeDetailsSv.add_SellerInvoiceIdentifierText( SellerInvoiceIdentifierTextType( "SV", "02", None, None, None, None, "Referensnummer" ) )
sellerInvoiceTypeDetailsSv.add_SellerInvoiceIdentifierText( SellerInvoiceIdentifierTextType( "SV", "04", 10, True, False, 10, "Kundnummer" ) )

sellerInvoiceTypeDetailsEn.add_SellerInvoiceIdentifierText( SellerInvoiceIdentifierTextType( "EN", "02", None, None, None, None, "Reference number" ) )
sellerInvoiceTypeDetailsEn.add_SellerInvoiceIdentifierText( SellerInvoiceIdentifierTextType( "EN", "04", 10, True, False, 10, "Customer number" ) )

# SellerDirectDebitIdentifier=None, PaymentInstructionIdentifier=None, SellerInstructionFreeText=None, SellerInvoiceTypeDetails=None, SellerServiceCode=None
sellerInvoiceDetails = SellerInvoiceDetailsType( None, "Bookkeeping service" )
sellerInvoiceDetails.add_SellerInvoiceTypeDetails( sellerInvoiceTypeDetailsFi )
sellerInvoiceDetails.add_SellerInvoiceTypeDetails( sellerInvoiceTypeDetailsSv )
sellerInvoiceDetails.add_SellerInvoiceTypeDetails( sellerInvoiceTypeDetailsEn )

sellerInvoiceDetails.set_SellerServiceCode( "00" )

senderInfo.set_SellerInvoiceDetails( sellerInvoiceDetails )

senderInfo.set_ProposedDueDateAccepted( "NO" )
senderInfo.set_ProposedInvoicePeriodAccepted( "YES" )

encodingHeader = '<?xml version="1.0" encoding="' + ExternalEncoding + '" ?>\n'
sys.stdout.write( encodingHeader )
sys.stdout.write( '<?xml-stylesheet type="text/xsl" href="FinvoiceSenderInfo.xsl"?>\n' )
senderInfo.export( sys.stdout, 0, name_='FinvoiceSenderInfo', namespacedef_='xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:noNamespaceSchemaLocation="FinvoiceSenderInfo.xsd"', pretty_print=True )
