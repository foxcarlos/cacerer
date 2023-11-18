# -*- coding: utf-8 -*-
import logging

from odoo import models, fields, api

logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)
_logger = logging.getLogger(__name__)


class Bulletin(models.Model):
    _name = "laboratory.bulletin"
    _description = "Laboratory Bulletin"

    name = fields.Char("Bulletin Identifier", required=True)
    partner_id = fields.Many2one("res.partner", string="Client")
    sale_order_id = fields.Many2one("sale.order", string="Sale Order")
    reception_date = fields.Datetime("Reception Date", default=fields.Datetime.now)
    analysis_ids = fields.One2many(
        "laboratory.analysis", "bulletin_id", string="Analysis"
    )
    state = fields.Selection(
        [
            ("new", "New"),
            ("in_progress", "In Progress"),
            ("completed", "Completed"),
            ("cancelled", "Cancelled"),
        ],
        string="Status",
        default="new",
    )
