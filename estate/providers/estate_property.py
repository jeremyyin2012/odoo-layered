from ..providers.shared.datamodels import DataModels
from odoo.api import Environment

import logging

logger = logging.getLogger(__name__)


class EstatePropertyProvider:
    def __init__(self, env: Environment) -> None:
        self.env = env
        self.dm = DataModels(env)

    def get_estate_property_sth(self) -> str:
        res = self.dm.estate_property.sudo().search([('name', '=', 'estate_property')])
        logger.info(f"{type(res)=}")
        return res
