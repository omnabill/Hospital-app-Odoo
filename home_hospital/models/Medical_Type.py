# -*- coding: utf-8 -*-
from odoo import api, fields, models, _


class Medical_Type(models.Model):
        _name = "cf.hospital.medicaltype"
        _inherit = ["mail.thread", 'mail.activity.mixin']
        _description = "Medical"
        _rec_name = "name"

        web_id = fields.Integer(string='Web ID', tracking=True)
        name = fields.Char(string="Name",translate=True)
        # name_ar = fields.Char(string='name Arabic', required=True, tracking=True)
        # name_eng = fields.Char(string='name English', required=True, tracking=True)
        price_list_id = fields.Many2one(string='price list id',comodel_name='cf.hospital.pricelist')
        admin_id = fields.Many2one('res.users',string='Admin', tracking=True)
        disabled = fields.Boolean(string='disabled',required=True, default=False)
        # status = fields.Integer(string='status', required=True, tracking=True)
        status = fields.Selection([('option1', 'Status 1'), ('option2', 'Status 2'),('option3', 'Status 3'), ('option4', 'Status 4')],
                                              string='Status',required=True)

        web_created_at = fields.Datetime( tracking=True)
        created_at = fields.Datetime(string='created at', tracking=True)

        # updated_at = fields.Datetime(string='updated at', required=True, tracking=True)
