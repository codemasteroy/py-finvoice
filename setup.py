#!/usr/bin/env python

from distutils.core import setup

setup(
		name='py-finvoice',
		version='1.0',
		description='Python module for generating Finvoice invoices',
		author='Mohanjith Sudirikku Hannadige',
		author_email='moha@mohanjith.net',
		url='http://www.codemaster.fi/python/finvoice/',
		packages=[ 'finvoice', 'finvoice.ack', 'finvoice.attachment', 'finvoice.receiver', 'finvoice.sender', 'finvoice.soap' ]
)
