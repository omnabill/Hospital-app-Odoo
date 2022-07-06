# -*- coding: utf-8 -*-
from odoo import api, fields, models, _


class NurseSheet(models.Model):
    _name = "cf.hospital.nursesheet"
    _inherit = ["mail.thread", 'mail.activity.mixin']
    _description = "Devices"
    _rec_name = "shift_type"

    id_web = fields.Integer(string='Web ID', tracking=True)
    shift_type= fields.Integer(string='Shift Type', tracking=True)
    # name_ar = fields.Char(string='name Arabic', required=True, tracking=True)
    # name_eng = fields.Char(string='name English', required=True, tracking=True)
    shift_date=fields.Date(string='Shift Date',tracking=True)
    investigation = fields.Char(string='Investigation' , tracking=True)
    oxygen = fields.Char(string='Oxygen' , tracking=True)
    situation= fields.Char(string='Situation', tracking=True)
    issues= fields.Char(string='Issues', tracking=True)
    remarks= fields.Char(string='Remarks', tracking=True)
    notes= fields.Char(string='Notes', tracking=True)
    add_devices= fields.Char(string='Add Devices', tracking=True)
    request_id = fields.Many2one('cf.hospital.request', string='Request ID',required=True, tracking=True)
    admin_id = fields.Many2one('res.users',string='Admin', required=True, tracking=True)
    web_created_at = fields.Datetime(string='created_at', tracking=True)
