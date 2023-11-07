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
    analysis_ids = fields.One2many("laboratory.analysis", "bulletin_id", string="Tests")
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


class LaboratoryAnalysis(models.Model):
    _name = "laboratory.analysis"
    _description = "Laboratory Test"

    name = fields.Char("Test Name", required=True)
    product_id = fields.Many2one("product.template", string="Product")
    bulletin_id = fields.Many2one("laboratory.bulletin", string="Bulletin")
    results_ids = fields.One2many(
        "laboratory.analysis.result", "test_id", string="Results"
    )
    normal_range = fields.Char(
        "Normal Range"
    )  # This could be a more complex type depending on the requirements
    is_alert = fields.Boolean("Alert", compute="_compute_alert")


class LaboratoryAnalysisResult(models.Model):
    _name = "laboratory.analysis.result"
    _description = "Laboratory Analysis Result"

    analysis_id = fields.Many2one("laboratory.analysis", string="Analysis")
    variable_name = fields.Char("Variable")
    value = fields.Float("Value")
    manual_result = fields.Char("Manual Result")
    # computed_result = fields.Float('Computed Result', compute='_compute_result')

    @api.depends("variable_name", "value", "test_id.formula")
    def _compute_result(self):
        """Compute the result based on the variable and formula
        This is a placeholder for actual formula calculation logic
        """
        pass
