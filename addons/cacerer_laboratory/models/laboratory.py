# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Laboratory(models.Model):
    _name = "laboratory.laboratory"
    _description = "Laboratory"

    name = fields.Char()
    description = fields.Char()
