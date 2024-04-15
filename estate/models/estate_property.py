from odoo import models, fields, api, _


class EstateProperty(models.Model):
    _name = 'estate.property'
    _description = 'Estate Property'

    name = fields.Char(string='Name', required=True)

    def do_sth(self) -> str:
        from ..providers import Providers
        from ..services import Services
        pvd = Providers(self.env)
        svc = Services(self.env, pvd)
        res = svc.estate_property.do_sth()
        return res
