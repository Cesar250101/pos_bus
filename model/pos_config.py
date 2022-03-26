# -*- coding: utf-8 -*-
##############################################################################
#
#    TL Technology
#    Copyright (C) 2019 ­TODAY TL Technology (<https://www.posodoo.com>).
#    Odoo Proprietary License v1.0 along with this program.
#
##############################################################################
from odoo import api, fields, models, _


class PosConfig(models.Model):
    _inherit = "pos.config"

    floor_ids = fields.Many2many(
        'restaurant.floor',
        'pos_config_restaurant_floor_rel',
        'pos_config_id',
        'floor_id',
        string="Floors")
    user_id = fields.Many2one(
        'res.users',
        'Assigned to'
    )
    sync_multi_session = fields.Boolean(
        'Sync Between Session',
        default=0
    )
    sync_multi_session_times_refresh = fields.Integer(
        'Sync Times Refresh',
        help='It a Millisecond Times for refresh Pos Screen',
        default=2000
    )
    sync_multi_session_offline = fields.Boolean(
        'Sync Between Session Offline',
        default=0
    )
    sync_multi_session_offline_iot_ids = fields.Many2many(
        'pos.iot',
        'pos_config_iot_rel',
        'pos_config_id',
        'iot_box_id',
        string='IoT Boxes',
        help='IoT box use for sync between sessions \n'
             'when Odoo Server Offline or your internet disconected')

    bus_id = fields.Many2one(
        'pos.bus',
        string='Point Sync')
    display_person_add_line = fields.Boolean(
        'Display information line',
        default=0,
        help="When you checked, on pos order lines screen, \n"
             "will display information person created order \n"
             "(lines) Eg: create date, updated date ..")