# -*- coding: utf-8 -*-
from odoo import api, fields, models, _


class cities(models.Model):
    _name = "cf.hospital.cities"
    _inherit = ["mail.thread", 'mail.activity.mixin']
    _description = "Cities"
    _rec_name = "city_name"

    web_id = fields.Integer(string='Web ID', required=True, tracking=True)

    governorate_id= fields.Many2one('cf.hospital.governorates',string='governorate ID', required=True, tracking=True)
    city_name =  fields.Char(string='city Name', required=True, tracking=True,translate=True)
    # city_name_ar = fields.Char(string='city Name in Arabic', required=True, tracking=True)
    # city_name_en = fields.Char(string='city Name in English', required=True, tracking=True)

