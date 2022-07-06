# -*- coding: utf-8 -*-
from odoo import api, fields, models, _


class Doc_Work(models.Model):
    _name = "cf.hospital.docwork"
    _inherit = ["mail.thread", 'mail.activity.mixin']
    _description = "doc_work"
    _rec_name = "ID"

    ID = fields.Integer(string='Web ID', required=True, tracking=True)
    user_id = fields.Integer(string='user ID', required=True, tracking=True)
    day = fields.Char(string='Day', required=True, tracking=True)
    time_from = fields.Datetime(string='time from', required=True, tracking=True)
    time_to = fields.Datetime(string='time to', required=True, tracking=True)
    created_at = fields.Datetime(string='created at', required=True, tracking=True)
    updated_at = fields.Datetime(string='updated at', required=True, tracking=True)
