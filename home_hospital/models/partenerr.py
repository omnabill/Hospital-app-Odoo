# -*- coding: utf-8 -*-
from odoo import api, fields, models, _


class Partnerr(models.Model):
    _inherit = ['res.partner']

    web_id = fields.Integer(string='Web_id')
    Record_Type = fields.Selection([('1','Doctor'),('2','Nurse'),('3','Driver')],string='Record Type',readonly=True)
    degree = fields.Integer(string='Degree',tracking=True)
    degree2 = fields.Integer(string='Degree 2', tracking=True)

