# -*- coding: utf-8 -*-
from odoo import api, fields, models, _


class Companies(models.Model):
    _name = "cf.hospital.company"
    _inherit = ["mail.thread", 'mail.activity.mixin']
    _description = "Company"
    _rec_name = "org_name"

    id_web = fields.Integer(string='Web ID', tracking=True)
    org_name = fields.Char(string='Organization Name', tracking=True)
    email=fields.Char(string='Email', tracking=True)
    phone = fields.Char(string='Phone',tracking=True)
    website = fields.Char(string='WebSite', tracking=True)
    contact_person_name = fields.Char(string='contact_person_name', tracking=True)
    registration_num = fields.Char(string='Regst.Num', tracking=True)
    tax_certificate_num = fields.Char(string='TAX Cert.', tracking=True)
    type = fields.Selection([('1','Type1'),('2','Type2'),('3','Type3')],string='Type', tracking=True)
    pay = fields.Selection([('1','Method1'),('2','Method2'),('3','Method3')],string='Pay', tracking=True)
    description = fields.Char(string='Description', tracking=True)
    price_list_id = fields.Many2one(comodel_name="cf.hospital.pricelist",string='Price List',tracking=True)
    admin_id = fields.Many2one(comodel_name="res.users",string='Admin ID',required=True,tracking=True)
    web_created_at = fields.Datetime(string='created_at', tracking=True)
