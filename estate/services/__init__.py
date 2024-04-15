from odoo.api import Environment
from ..providers import Providers
from ..services.estate_property import EstatePropertyService


class Services:
    def __init__(self, env: Environment, providers: Providers):
        self.env = env
        self.pvd = providers

    @property
    def estate_property(self) -> EstatePropertyService:
        return EstatePropertyService(self.env, self.pvd)
