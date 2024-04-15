from odoo.api import Environment
from ..providers.shared.datamodels import DataModels


class PingProvider:
    def __init__(self, env: Environment):
        self.env = env
        self.dm = DataModels(env)

    def ping(self) -> str:
        return 'pong'
