# -*- coding: utf-8 -*-
from odoo import api, fields, models, _


class Devices(models.Model):
    _name = "cf.hospital.devices"
    _inherit = ["mail.thread", 'mail.activity.mixin']
    _description = "Devices"
    _rec_name = "name"

    id_web = fields.Integer(string='Web ID', tracking=True)
    name = fields.Char(string='Name', required=True, tracking=True)
    # name_ar = fields.Char(string='name Arabic', required=True, tracking=True)
    # name_eng = fields.Char(string='name English', required=True, tracking=True)
    description=fields.Char(string='Description', tracking=True)
    price = fields.Float(string='Price',digits=(8,2) , tracking=True)
    day_hour = fields.Char(string='Day Hour', tracking=True)
    type = fields.Integer(string='Type', tracking=True)
    admin_id = fields.Many2one('res.users',string='Admin', required=True, tracking=True)
    web_created_at = fields.Datetime(string='created_at', tracking=True)
