# -*- coding: utf-8 -*-
from odoo import api, fields, models, _


class Service(models.Model):
    _name = "cf.hospital.service"
    _inherit = ["mail.thread", 'mail.activity.mixin']
    _description = "Service"
    _rec_name = "name"

    id_web = fields.Integer(string='Web ID', tracking=True)
    name=fields.Char(string="Name", translate=True,required=True,tracking=True)
    description = fields.Char(string="description", tracking=True)
    category_id= fields.Many2one('cf.hospital.category',string='Category', tracking=True)
    image=fields.Binary(string='up load an image')
    # name_ar = fields.Char(string='name Arabic', required=True, tracking=True)
    # name_eng = fields.Char(string='name English', required=True, tracking=True)
    type= fields.Selection([('0', 'Internal'), ('1', 'External'), ('2', 'Lab')], string='Type')

    site = fields.Boolean(string='Site',required=True,default=False, tracking=True)
    specialty_id= fields.Many2one('cf.hospital.specialties',string="Speciality",tracking=True)
    admin_id= fields.Many2one('res.users',string="Admin", required=True,tracking=True)
    disabled=fields.Boolean(string='Disabled',required=True,default=False, tracking=True)

    web_created_at = fields.Datetime(string='created_at', tracking=True)
