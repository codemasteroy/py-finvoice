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

class MemberLists:
	def get_BanksList(self):
		return [ 
			'OKOYFIHH', # OP-Pohjola-ryhmä
			'NDEAFIHH', # Nordea
			'DABAFIHH', # Danske Bank
			'HELSFIHH', # Säästöpankit, Aktia Säästöpankki Oyj, Paikallisosuuspankit
			'TAPIFI22', # Tapiola Bank Oy
			'AABAFI22', # Ålandsbanken
			'HANDFIHH', # Handelsbanken
			'SBANFIHH', # S-Pankki
			'DNBAFIHX', # DnB NOR Bank
		]
	def get_ServicePorvidersList(self):
		return [ 
			'FIYAPSOL', # YAP Solutions Oy
			'003723327487', # Apix Messaging Oy
			'BAWCFI22', # Basware Oyj
			'003714377140', # Enfo Zender Oy
			'003710948874', # OpusCapita Group Oy
			'003708599126', # Liaison Technologies Oy
			'003703575029', # CGI
			'003717203971', # Notebeat Oy
			'003721291126', # Maventa Oy
			'MAVENTA', # Maventa Oy
			'PAGERO', # Pagero
			'003701150617', # Strålfors Oy
			'003714756079', # TeliaSonera Finland Oyj
			'003701011385', # Tieto Oyj
			'00885060259470028', # Tradeshift
		]
	def get_MembersList():
		return self.get_BanksList() + self.get_MembersList()

class PrintServiceList:
	def get_PrintServiceList(self):
		return {
			'NDEAFIHH': 'tulostukseen',
			'PSPBFIHH': '003718062728810P',
			'DABAFIHH': '003718062728810P',
			'HELSFIHH': 'TULOSTUSPALVELU',
			'OKOYFIHH': 'TULOSTUSPALVELU',
			'003710948874': 'EKIRJE',
			'003723327487': 'TULOSTUS',
			'003721291126': 'PRINT',
		}

class PrintService():
	def get_PrintService(self, member_id):
		psl = PrintServiceList()
		l = psl.get_PrintServiceList()
		if (l[member_id]):
			return l[member_id];
		return ''


