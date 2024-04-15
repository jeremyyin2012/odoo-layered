from odoo.api import Environment
from ...providers import Providers


class ServicesShared:
    def __init__(self, env: Environment, providers: Providers) -> None:
        self.env = env
        self.pvd = providers

    def some_shared_method_in_services(self) -> None:
        res_echo = self.pvd.echo.echo()
        res_ping = self.pvd.ping.ping()
        ...