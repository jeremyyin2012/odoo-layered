from odoo.api import Environment
from .shared import ServicesShared
from ..providers import Providers


class EstatePropertyService:
    def __init__(self, env: Environment, providers: Providers) -> None:
        self.env = env
        self.pvd = providers
        self.shared = ServicesShared(env, providers)

    def do_sth(self) -> str:
        # use pvd to do lots of things
        res_echo = self.pvd.echo.echo()
        res_ping = self.pvd.ping.ping()
        res = self.pvd.estate_property.get_estate_property_sth()
        return res
