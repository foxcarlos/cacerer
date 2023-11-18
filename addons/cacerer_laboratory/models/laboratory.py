# -*- coding: utf-8 -*-
import logging
from odoo import models, fields, api


logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)
_logger = logging.getLogger(__name__)


class Laboratory(models.Model):
    _name = "laboratory.laboratory"
    _description = "Laboratory"

    name = fields.Char()
    description = fields.Char()
    active = fields.Boolean()


class LaboratoryAnalysis(models.Model):
    _name = "laboratory.analysis"
    _description = "Laboratory Test"

    name = fields.Char("Test Name", required=True)
    product_id = fields.Many2one("product.product", string="Product")
    bulletin_id = fields.Many2one("laboratory.bulletin", string="Bulletin")
    results_ids = fields.One2many(
        "laboratory.analysis.result", "analysis_id", string="Results"
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

    @api.depends("variable_name", "value")
    def _compute_result(self):
        """Compute the result based on the variable and formula
        This is a placeholder for actual formula calculation logic
        """
        pass
