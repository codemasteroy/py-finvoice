#!/usr/bin/env python
# -*- coding: iso8859-15 -*-


## Start of parameters ##

_sellerOrganisationName = {
	'FI': 'Pullis Musiken Oy',
	'SV': 'Pullis Musiken Ab',
	'EN': 'Pullis Musiken Ltd',
}
_sellerAddress = 'Puukatu 2 F'
_sellerTown = 'HELSINKI'
_sellerPostCode = '00112'
_sellerCountryCode = 'FI'
_sellerCountryName = 'Suomi'
_sellerAccounts = [
	{ 'IBAN': 'FI2757800750155448', 'BIC': 'OKOYFIHH' },
	{ 'IBAN': 'FI2721221222212227', 'BIC': 'NDEAFIHH' },
	{ 'IBAN': 'FI2781232323312334', 'BIC': 'PSPBFIHH' },
]

_sellerWebAddressNameText = _sellerOrganisationName['FI']
_sellerWebAddress = 'https://www.pullinmusiikki.fi/'
_sellerInvoiceAddress = '00371999207'
_sellerInvoiceIntermediatorAddress = 'OKOYFIHH'
_sellerYTunnus = '0199920-7'
_sellerIndustryCode = '62020'

_sellerInvoiceTypeDetails = {
	'FI': { 
		'text': 'Kirjanpito palvelu',
		'validation':
		[
			{
				'type': '02',
				'min': None,
				'hyphens': None,
				'spaces': None,
				'max': None,
				'text': 'Viitenumero'
			},
			{
				'type': '09',
				'min': 10,
				'hyphens': True,
				'spaces': None,
				'max': 10,
				'text': 'Asiakasnumero'
			},
		],
	},
	'SV': { 
		'text': 'Bokföring tjänster',
		'validation':
		[
			{
				'type': '02',
				'min': None,
				'hyphens': None,
				'spaces': None,
				'max': None,
				'text': 'Referensnummer'
			},
			{
				'type': '09',
				'min': 10,
				'hyphens': True,
				'spaces': None,
				'max': 10,
				'text': 'Kundnummer'
			},
		],
	},
	'EN': {
		'text': 'Bookkeeping service',
		'validation':
		[
			{
				'type': '02',
				'min': None,
				'hyphens': None,
				'spaces': None,
				'max': None,
				'text': 'Reference number'
			},
			{
				'type': '09',
				'min': 10,
				'hyphens': True,
				'spaces': None,
				'max': 10,
				'text': 'Customer number'
			},
		],
	},
}

_paymentInstructionId = 'Bookkeeping service'

_proposedDueDate = 'NO'
_proposedPaymentPeriod = 'YES'

_messageId = '001'
_messageActionCode = 'ADD'

## End of parameters ##

import sys
import datetime, time

reload( sys )

sys.setdefaultencoding( 'iso8859-15' )

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

from finvoice.soap.envelope import Envelope, Header, Body
from finvoice.soap.msgheader import MessageHeader, From, To, PartyId, Service, MessageData
from finvoice.soap.msgheader import Manifest, Reference, Schema

from pytz import reference

# Date
nowDate = date( "CCYYMMDD", datetime.datetime.now( reference.LocalTimezone() ).date().strftime("%Y%m%d") )

# Seller Postal Address
# SellerStreetName=None, SellerTownName=None, SellerPostCodeIdentifier=None, CountryCode=None, CountryName=None, SellerPostOfficeBoxIdentifier=None
sellerPostalAddress = SellerPostalAddressDetailsType( _sellerAddress, _sellerTown, _sellerPostCode, _sellerCountryCode, _sellerCountryName )

sellerOrganisationNames = {}
# Seller Organization Name
# LanguageCode=None, SellerOrganisationName=None
for (_langCode, _orgName) in _sellerOrganisationName.items():
	sellerOrganisationNames[_langCode] = SellerOrganisationNamesType( _langCode )
	sellerOrganisationNames[_langCode].add_SellerOrganisationName( _orgName )

sellerAccountDetails = []
# SellerAccountID=None, SellerBic=None, NewSellerAccountID=None, NewSellerBic=None
for _account in _sellerAccounts:
	sellerAccountDetails.append( SellerAccountDetailsType( SellerAccountIDType( 'IBAN', _account['IBAN'] ), SellerBicType( 'BIC', _account['BIC'] ) ) )

# Sender Information
# Version=None, MessageDetails=None, SellerPartyDetails=None, SellerOrganisationUnitNumber=None, InvoiceSenderInformationDetails=None,
# SellerAccountDetails=None, SellerInvoiceDetails=None, ProposedDueDateAccepted=None, ProposedInvoicePeriodAccepted=None
senderInfo = FinvoiceSenderInfo( '2.0' )

# Message Details
# MessageTypeCode=None, MessageTypeText=None, MessageActionCode=None, MessageActionCodeIdentifier=None, MessageDate=None, SenderInfoIdentifier=None
senderInfo.set_MessageDetails( MessageDetailsType( 'SENDERINFO', 'INVOICER NOTIFICATION', _messageActionCode, None, nowDate, _messageId ) )

# Seller Party Details
# SellerPartyIdentifier=None, SellerOrganisationNames=None, SellerOrganisationBankName=None, SellerPostalAddressDetails=None, IndustryCode=None
sellerPartyDetails = SellerPartyDetailsType( _sellerYTunnus, None, None, sellerPostalAddress, _sellerIndustryCode )

for (_langCode, _orgName) in sellerOrganisationNames.items():
	sellerPartyDetails.add_SellerOrganisationNames( _orgName )

senderInfo.set_SellerPartyDetails( sellerPartyDetails )

# SellerWebaddressNameText=None, SellerWebaddressText=None, InvoiceSenderAddress=None, InvoiceSenderIntermediatorAddress=None, NewInvoiceSenderAddress=None, NewInvoiceSenderIntermediatorAddress=None
senderInfo.set_InvoiceSenderInformationDetails( InvoiceSenderInformationDetailsType( _sellerWebAddressNameText, _sellerWebAddress, _sellerInvoiceAddress, _sellerInvoiceIntermediatorAddress ) )

for _account in sellerAccountDetails:
	senderInfo.add_SellerAccountDetails( _account )

# SellerDirectDebitIdentifier=None, PaymentInstructionIdentifier=None, SellerInstructionFreeText=None, SellerInvoiceTypeDetails=None, SellerServiceCode=None
sellerInvoiceDetails = SellerInvoiceDetailsType( None, _paymentInstructionId )

sellerInvoiceTypeDetails = {}
for (_langCode, _type) in _sellerInvoiceTypeDetails.items():
	# SellerInvoiceTypeText=None, SellerInvoiceIdentifierText=None
	sellerInvoiceTypeDetails[_langCode] = SellerInvoiceTypeDetailsType( SellerInvoiceTypeTextType( _langCode, _type['text'] ) )

	for _validation in _type['validation']:
		#LanguageCode=None, SellerInvoiceIdentifierType=None, SellerInvoiceIdentifierMinLength=1, SellerInvoiceIdentifierHyphens=False, SellerInvoiceIdentifierSpaces=False, SellerInvoiceIdentifierMaxLength=35, valueOf_=None, extensiontype_=None
		sellerInvoiceTypeDetails[_langCode].add_SellerInvoiceIdentifierText( SellerInvoiceIdentifierTextType( _langCode, _validation['type'], _validation['min'], _validation['hyphens'], _validation['spaces'], _validation['max'], _validation['text'] ) )

	sellerInvoiceDetails.add_SellerInvoiceTypeDetails( sellerInvoiceTypeDetails[_langCode] )

# = e-invoicer
sellerInvoiceDetails.set_SellerServiceCode( '00' )

senderInfo.set_SellerInvoiceDetails( sellerInvoiceDetails )

senderInfo.set_ProposedDueDateAccepted( _proposedDueDate )
senderInfo.set_ProposedInvoicePeriodAccepted( _proposedPaymentPeriod )

_recepients = [
	{
		'Receiver': 'SENDERINFO',
		'Intermediator': 'OKOYFIHH',
	},
	{
		'Receiver': 'SENDERINFO',
		'Intermediator': 'NDEAFIHH',
	},
	{
		'Receiver': 'SENDERINFO',
		'Intermediator': 'DABAFIHH',
	},
	{
		'Receiver': 'SENDERINFO',
		'Intermediator': 'HELSFIHH',
	},
	{
		'Receiver': 'SENDERINFO',
		'Intermediator': 'TAPIFI22',
	},
	{
		'Receiver': 'SENDERINFO',
		'Intermediator': 'AABAFI22',
	},
	{
		'Receiver': 'SENDERINFO',
		'Intermediator': 'HANDFIHH',
	},
	{
		'Receiver': 'SENDERINFO',
		'Intermediator': 'SBANFIHH',
	},
	{
		'Receiver': 'SENDERINFO',
		'Intermediator': 'DNBAFIHX',
	}
]

_now = datetime.datetime.now( reference.LocalTimezone() )
_nowS = datetime.datetime( _now.year, _now.month, _now.day, _now.hour, _now.minute, _now.second, 0, _now.tzinfo )

for (i, _recepient) in enumerate(_recepients):
	envelope = Envelope(  )

	# mustUnderstand=None, version=None, From=None, To=None, CPAId=None, ConversationId=None, Service=None, Action=None, MessageData=None
	messageHeader = MessageHeader( 1, "2.0" )

	# Header=None, Body=None
	header = Header( )
	header.add_anytypeobjs_( messageHeader )

	# PartyId=None, Role=None
	msgFrom = From( None, "Sender" )
	msgFrom.add_PartyId( PartyId( None, _sellerInvoiceAddress ) )

	msgFromI = From( None, "Intermediator" )
	msgFromI.add_PartyId( PartyId( None, _sellerInvoiceIntermediatorAddress ) )

	messageHeader.add_anytypeobjs_( msgFrom )
	messageHeader.add_anytypeobjs_( msgFromI )

	msgTo = To( None, "Receiver" )
	msgTo.add_PartyId( PartyId( None, _recepient['Receiver'] ) )

	msgToI = To( None, "Intermediator" )
	msgToI.add_PartyId( PartyId( None, _recepient['Intermediator'] ) )

	messageHeader.add_anytypeobjs_( msgTo )
	messageHeader.add_anytypeobjs_( msgToI )

	messageHeader.set_CPAId( "yoursandmycpa" )

	messageHeader.set_Service( Service( None, "Routing" ) )
	messageHeader.set_Action( "ProcessInvoice" )

	msgData = MessageData( '{0}/{1}'.format(_messageId, i+1), _nowS )

	messageHeader.set_MessageData( msgData )

	envelope.set_Header( header )

	manifest = Manifest( "2.0", "Manifest" )
	reference = Reference( None, _messageId, None, "FinvoiceSenderInfo" )
	manifest.add_Reference( reference )
	reference.add_Schema( Schema( "2.0", "http://www.pankkiyhdistys.fi/verkkolasku/finvoice/FinvoiceSenderInfo.xsd" ) )

	body = Body( )
	body.add_anytypeobjs_( manifest )

	envelope.set_Body( body )

	envelope.export( sys.stdout, 0, pretty_print=True )

	encodingHeader = '<?xml version="1.0" encoding="' + ExternalEncoding + '" ?>\n'
	sys.stdout.write( encodingHeader )
	sys.stdout.write( '<?xml-stylesheet type="text/xsl" href="FinvoiceSenderInfo.xsl"?>\n' )
	senderInfo.export( sys.stdout, 0, name_='FinvoiceSenderInfo', namespacedef_='xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:noNamespaceSchemaLocation="FinvoiceSenderInfo.xsd"', pretty_print=True )
