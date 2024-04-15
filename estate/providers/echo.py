from odoo.api import Environment
from ..providers.shared.datamodels import DataModels


class EchoProvider:
    def __init__(self, env: Environment):
        self.env = env
        self.dm = DataModels(env)

    def echo(self) -> str:
        return 'hello world'
