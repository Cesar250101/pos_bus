# -*- coding: utf-8 -*-
##############################################################################
#
#    TL Technology
#    Copyright (C) 2019 ­TODAY TL Technology (<https://www.posodoo.com>).
#    Odoo Proprietary License v1.0 along with this program.
#
##############################################################################
{
    'name': "POS Sync Sessions Offline",
    'version': '1.0.0.1',
    'category': 'Point of Sale',
    'author': 'TL Technology',
    'sequence': 0,
    'summary': 'POS Sync Sessions Offline',
    'description': """
        If you wanted sync between cashiers, waiters ... pos sessions, the same POS screen \n
        Any events change of current pos session automatic sync realtime to another pos sessions \n
        Example: Session 1 change anything on orders (create, remove, update, set client ...etc) auto sync to Session 2, and Any events change from Session 2 auto sync to Session 1.\n
        If you wanted like it above example, this module create for you\n
        * Module can work 2 mode\n
        1. Sync Online with Your Odoo Server\n
        2. Sync Offline with Lan Local network (Required have 1 POSBOX) for made controllers between POS Session\n
        * Module supported Shop and Restaurant both\n
        ------------------------- Thanks for reading me -----------------------------\n
        ------------------------- Hope you have a good day --------------------------\n
        ------------------------- Bruce Nguye, CTO TL Technology --------------------\n
    
    ....
    """,
    'depends': ['pos_restaurant'],
    'data': [
        'security/ir.model.access.csv',
        'template/import.xml',
        'views/pos_bus.xml',
        'views/pos_config.xml',
        'views/pos_iot.xml',
    ],
    'demo': ['demo/demo.xml'],
    'qweb': [
        'static/src/xml/*.xml'
    ],
    'price': '400',
    'website': 'http://posodoo.com',
    "currency": 'EUR',
    'application': True,
    'images': ['static/description/icon.png'],
    'support': 'thanhchatvn@gmail.com',
    "license": "OPL-1"
}
