# -*- coding: utf-8 -*-
from odoo import api, fields, models, _


class Governorates(models.Model):
    _name = "cf.hospital.governorates"
    _inherit = ["mail.thread", 'mail.activity.mixin']
    _description = "Governorates"
    _rec_name = "governorate_name"

    web_id = fields.Integer(string="Web ID",tracking=True)
    governorate_name= fields.Char(string='GOV name',translate=True, required=True, tracking=True)
