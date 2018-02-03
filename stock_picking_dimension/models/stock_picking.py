# -*- coding: utf-8 -*-
# Copyright 2018 OpenSynergy Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from openerp import models, fields


class StockPicking(models.Model):
    _inherit = "stock.picking"

    picking_lenght = fields.Float(
        string="Lenght",
    )
    picking_width = fields.Float(
        string="Width",
    )
    picking_height = fields.Float(
        string="Height",
    )
