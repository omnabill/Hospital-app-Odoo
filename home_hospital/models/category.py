# -*- coding: utf-8 -*-
from odoo import api, fields, models, _


class Category(models.Model):
    _name = "cf.hospital.category"
    _inherit = ["mail.thread", 'mail.activity.mixin']
    _description = "Category"
    _rec_name = "name"

    id_web = fields.Integer(string='Web ID', tracking=True)
    name=fields.Char(string="Name", translate=True,required=True,tracking=True)
    parent_id= fields.Many2one('cf.hospital.category',string='Parent Category', tracking=True)
    admin_id= fields.Many2one('res.users',string="Admin",tracking=True)
    disabled=fields.Boolean(string='Disabled',required=True,default=False, tracking=True)

    web_created_at = fields.Datetime(string='created_at', tracking=True)
