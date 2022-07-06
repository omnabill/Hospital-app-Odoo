# -*- coding: utf-8 -*-
from odoo import api, fields, models, _


class Price_List(models.Model):
    _name = "cf.hospital.pricelist"
    _inherit = ["mail.thread", 'mail.activity.mixin']
    _description = "Price List"
    _rec_name = "name"

    web_id = fields.Integer(string='Web ID', tracking=True)

    name= fields.Char(string='Name', required=True, tracking=True)
    main_pl = fields.Char(string='main PL', required=True, tracking=True)
    copy_from = fields.Integer(string='copy from', required=True, tracking=True)
    admin_id = fields.Integer(string='Admin ID', tracking=True)
    status = fields.Boolean(string='Status', default=False, tracking=True)
    disabled = fields.Boolean(string='disabled',default=False)

