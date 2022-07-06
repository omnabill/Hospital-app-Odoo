# -*- coding: utf-8 -*-
from odoo import api, fields, models, _


class Physician(models.Model):
        _name = "cf.hospital.physician"
        _inherit = ["mail.thread", 'mail.activity.mixin']
        _description = "Physician"
        _rec_name = "name"

        web_id = fields.Integer(string='Web ID', required=True, tracking=True)
        name = fields.Char(string='Name', required=True, tracking=True)
        description = fields.Char(string='Description', required=True, tracking=True)
        admin_id = fields.Integer(string='ID', required=True, tracking=True)
        created_at = fields.Datetime(string='created at', required=True, tracking=True)
        updated_at = fields.Datetime(string='updated at', required=True, tracking=True)
