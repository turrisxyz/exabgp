#!/usr/bin/env python
# encoding: utf-8
"""
attributes.py

Created by Thomas Mangin on 2009-11-05.
Copyright (c) 2009 Exa Networks. All rights reserved.
"""

import socket

from bgp.utils import *
from bgp.structure.afi import AFI
from bgp.structure.safi import SAFI
from bgp.structure.ip import to_IP,Inet
from bgp.message.update.attribute import Attribute,Flag

# =================================================================== NextHop (3)

def new_NextHop (data,afi=AFI.ipv4):
	return NextHop(Inet(afi,data))

def to_NextHop (ip):
	return NextHop(to_IP(ip))

class NextHop (Attribute):
	ID = Attribute.NEXT_HOP
	FLAG = Flag.TRANSITIVE
	MULTIPLE = False

	# Take an IP as value
	def __init__ (self,value):
		Attribute.__init__(self,value)

	def pack (self):
		return self._attribute(self.value.pack())

	def __len__ (self):
		return len(self.value) - 1

	def __str__ (self):
		return str(self.value)
