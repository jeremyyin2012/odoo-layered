from odoo.api import Environment
from .shared import ServicesShared
from ..providers import Providers


class PingService:
    def __init__(self, env: Environment, providers: Providers):
        self.env = env
        self.pvd = providers
        self.shared = ServicesShared(env, providers)

    def ping_sth(self) -> bool:
        self.pvd.ping.ping()
        self.pvd.echo.echo()

        return True
