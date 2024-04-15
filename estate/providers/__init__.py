from odoo.api import Environment
from ..providers.estate_property import EstatePropertyProvider
from ..providers.echo import EchoProvider
from ..providers.ping import PingProvider


class Providers:

    def __init__(self, env: Environment) -> None:
        self.env = env

    @property
    def estate_property(self) -> EstatePropertyProvider:
        return EstatePropertyProvider(self.env)

    @property
    def echo(self) -> EchoProvider:
        return EchoProvider(self.env)

    @property
    def ping(self) -> PingProvider:
        return PingProvider(env=self.env)
