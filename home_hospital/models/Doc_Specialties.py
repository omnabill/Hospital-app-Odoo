# -*- coding: utf-8 -*-
from odoo import api, fields, models, _


class Doc_Specialties(models.Model):
    _name = "cf.hospital.docspecialties"
    _inherit = ["mail.thread", 'mail.activity.mixin']
    _description = "Doc_specialities"
    _rec_name = "ID"

    ID = fields.Integer(string='Web ID', required=True, tracking=True)
    user_id = fields.Integer(string='user ID', required=True, tracking=True)
    speciality_id = fields.Integer(string='Speciality ID', required=True, tracking=True)
    created_at = fields.Datetime(string='created at', required=True, tracking=True)
    updated_at = fields.Datetime(string='updated at', required=True, tracking=True)
