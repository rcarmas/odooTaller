from odoo import models, fields, api

class Autor(models.Model):
    _name = 'autor'
    name = fields.Char(string='Nombre', required=True)

