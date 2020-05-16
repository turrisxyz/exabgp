# encoding: utf-8
"""
admingroup.py

Created by Evelio Vila on 2016-12-01.
Copyright (c) 2014-2017 Exa Networks. All rights reserved.
"""

from struct import unpack

from exabgp.bgp.message.notification import Notify
from exabgp.bgp.message.update.attribute.bgpls.linkstate import LinkState
from exabgp.bgp.message.update.attribute.bgpls.linkstate import BaseLS


@LinkState.register()
class AdminGroup(BaseLS):
    TLV = 1088
    REPR = 'Admin Group mask'
    JSON = 'admin-group-mask'
    LEN = 4

    @classmethod
    def unpack(cls, data, length):
        cls.check(length)
        return cls(unpack('!L', data[:4])[0])
