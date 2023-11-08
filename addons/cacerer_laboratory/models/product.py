# -*- coding: utf-8 -*-

from odoo import models, fields, api


class ProductTemplate(models.Model):
    _inherit = "product.product"

    laboratory_ids = fields.Many2many(
        "laboratory.laboratory",  # nombre del modelo al que se relaciona
        "product_template_laboratory_rel",  # nombre de la tabla de relación
        "product_template_id",  # campo para "este" registro
        "laboratory_id",  # campo para "otro" registro
        string="Laboratories",
    )
