# -*- coding: utf-8 -*-
from odoo import api, fields, models, _


class Nurse(models.Model):
    _inherit = ['res.partner']
    notes1=fields.Char(string='Notes',tracking=True)