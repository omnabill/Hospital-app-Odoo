# -*- coding: utf-8 -*-
from odoo import api, fields, models, _


class Doctors(models.Model):
    _inherit = ['res.partner']

    country_id = fields.Many2one('res.country', string='Country',tracking=True)
    specialty = fields.Many2one('cf.hospital.specialties', string="Speciality")
    cv = fields.Binary(string='CV' )
    photo = fields.Binary(string='Photo', required=True, tracking=True)
    description = fields.Char(string='Description', tracking=True)
    available_time = fields.Char(string='available_time', tracking=True)
