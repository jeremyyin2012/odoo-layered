from odoo.api import Environment
from ...models.estate_property import EstateProperty


class DataModels:
    def __init__(self, env: Environment):
        self.env = env

    @property
    def estate_property(self) -> EstateProperty:
        return self.env['estate.property']
