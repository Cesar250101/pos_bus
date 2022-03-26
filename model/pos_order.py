# -*- coding: utf-8 -*-
##############################################################################
#
#    TL Technology
#    Copyright (C) 2019 ­TODAY TL Technology (<https://www.posodoo.com>).
#    Odoo Proprietary License v1.0 along with this program.
#
##############################################################################
from odoo import api, fields, models

import logging

_logger = logging.getLogger(__name__)

class PosOrderLine(models.Model):
    _inherit = 'pos.order.line'

    note = fields.Char('Note added by the waiter.')
    mp_skip = fields.Boolean('Skip line when sending ticket to kitchen printers.')
    uid = fields.Char('Uid')
    session_info = fields.Char('session_info')
    order_uid = fields.Char('order_uid')
    mp_dirty = fields.Char('mp_dirty')
    state = fields.Char('state')
    creation_time = fields.Char('creation_time')


class PosOrder(models.Model):
    _inherit = 'pos.order'

    @api.model
    def get_table_draft_orders(self, table_id):
        table_orders = super(PosOrder, self).get_table_draft_orders(table_id)
        is_active_sync = False
        if len(table_orders):
            server = self.browse(table_orders[0].get('server_id'))
            self.env.cr.execute("SELECT sync_multi_session FROM pos_config WHERE id=%s" % server.config_id.id)
            datas = self._cr.fetchall()
            if datas:
                is_active_sync = True
        if is_active_sync:
            return []
        else:
            return table_orders

