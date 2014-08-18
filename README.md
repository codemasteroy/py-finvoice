py-finvoice
============

Python module for generating and parsing Finvoice invoices.

Finvoice message can be used for invoicing and for other business messages, such as quotations, orders, order confirmations, price lists, etc. Due to easy adoption, it is suitable for invoicing between companies of all sizes and for consumer invoicing.

This Python module is based on the XSDs released by the Federation of Financial Services, Finland. 

# Tested

XML has been parsed and XML has been generated using data and have been validated.

## Ilmoittamissanomat
- FinvoiceSenderInfo (SI)
- FinvoiceReceiverInfo (RI)

## Finvoice
- Finvoice
- Finvoice Attachment
- Finvoice Ack

## SOAP EBML
- Envelope
- MessageHeader

# Road Tested

XML generated has been used in actual transactions. XML from actual transactions have been parsed.

## Ilmoittamissanomat
- FinvoiceSenderInfo (SI)

## Finvoice
- Finvoice

## SOAP EBML
- Envelope
- MessageHeader
