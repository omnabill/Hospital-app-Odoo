# -*- coding: utf-8 -*-
from odoo import api, fields, models, _


class Specialties(models.Model):
    _name = "cf.hospital.specialties"
    _inherit = ["mail.thread", 'mail.activity.mixin']
    _description = "Specialties"
    _rec_name = "name"

    id_web = fields.Integer(string='Web ID', tracking=True)
    name = fields.Char(string='Name', required=True, tracking=True, translate=True)
    # name_ar = fields.Char(string='name Arabic', required=True, tracking=True)
    # name_eng = fields.Char(string='name English', required=True, tracking=True)
    slot_time = fields.Integer(string='slot time',  tracking=True)
    over_time = fields.Integer(string='over slot', tracking=True)
    parent_id = fields.Many2one('cf.hospital.specialties',string='parent id', tracking=True)
    image_app = fields.Binary(string='image app', tracking=True)
    image = fields.Binary(string='image', required=True, tracking=True)
    note = fields.Char(string='note', tracking=True)
    admin_id = fields.Many2one('res.users',string='Admin', required=True, tracking=True)
    disabled = fields.Boolean(string='disabled', default=False)
    web_created_at = fields.Datetime(string='created_at', tracking=True)
