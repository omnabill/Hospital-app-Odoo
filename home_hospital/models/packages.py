# -*- coding: utf-8 -*-
from odoo import api, fields, models, _


class Packages(models.Model):
    _name = "cf.hospital.packages"
    _inherit = ["mail.thread", 'mail.activity.mixin']
    _description = "Packages"
    _rec_name = "name"

    id_web = fields.Integer(string='Web ID', tracking=True)
    name = fields.Char(string='Name', tracking=True, translate=True)
    # name_ar = fields.Char(string='name Arabic', required=True, tracking=True)
    # name_eng = fields.Char(string='name English', required=True, tracking=True)
    description=fields.Char(string='Description', tracking=True)
    price = fields.Float(string='Price',digits=(8,2) ,required=True, tracking=True)
    admin_id = fields.Many2one('res.users',string='Admin', required=True, tracking=True)
    disabled = fields.Boolean(string='Disabled', default=False)
    web_created_at = fields.Datetime(string='created_at', tracking=True)
