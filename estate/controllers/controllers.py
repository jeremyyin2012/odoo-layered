# -*- coding: utf-8 -*-
from odoo import http
from ..providers import Providers
from ..services import Services

import logging

logger = logging.getLogger(__name__)


class EstateController(http.Controller):
    @http.route('/api/estate/ping/', auth='public')
    def index(self, **kw):
        pvd = Providers(http.request.env)
        svc = Services(http.request.env, pvd)
        res = svc.estate_property.do_sth()
        logger.info(f"{res=}")
        return "hello world"
    #
    # @http.route('/my_module/my_module/objects/', auth='public')
    # def list(self, **kw):
    #     return http.request.render('my_module.listing', {
    #         'root': '/my_module/my_module',
    #         'objects': http.request.env['my_module.my_module'].search([]),
    #     })
    #
    # @http.route('/my_module/my_module/objects/<model("my_module.my_module"):obj>/', auth='public')
    # def object(self, obj, **kw):
    #     return http.request.render('my_module.object', {
    #         'object': obj
    #     })
