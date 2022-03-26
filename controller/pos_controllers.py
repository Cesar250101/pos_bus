# -*- coding: utf-8 -*-
##############################################################################
#
#    TL Technology
#    Copyright (C) 2019 ­TODAY TL Technology (<https://www.posodoo.com>).
#    Odoo Proprietary License v1.0 along with this program.
#
##############################################################################
from odoo.http import request
from odoo.addons.bus.controllers.main import BusController
from odoo import http, _
from datetime import datetime
import odoo

version_info = odoo.release.version_info[0]

datetime.strptime('2012-01-01', '%Y-%m-%d')

import logging

_logger = logging.getLogger(__name__)


class pos_bus(BusController):

    def _poll(self, dbname, channels, last, options):
        channels = list(channels)
        if request.env.user:
            channels.append((request.db, 'pos.sync.sessions', request.env.user.id))
        return super(pos_bus, self)._poll(dbname, channels, last, options)


    @http.route('/pos/test/polling', type="json", auth="public")
    def test_polling(self, pos_id, messages):
        _logger.info('test_polling POS ID: %s' % pos_id)
        request.env['bus.bus'].sendmany(
            [[(request.env.cr.dbname, 'pos.test.polling', 1), messages]])
        return 1

    @http.route('/pos/sync', type="json", auth="public")
    def send(self, bus_id, messages):
        for message in messages:
            user_send_id = message['user_send_id']
            _logger.info(message['value']['action'])
            sessions = request.env['pos.session'].sudo().search([
                ('state', '=', 'opened'),
                ('user_id', '!=', user_send_id),
                ('config_id.bus_id', '=', bus_id),
            ])
            if not sessions:
                _logger.error('Have not session the same branch/store for sync')
                return True
            for session in sessions:
                request.env['bus.bus'].sendmany(
                        [[(request.env.cr.dbname, 'pos.sync.sessions', session.user_id.id), message]])
        return True

