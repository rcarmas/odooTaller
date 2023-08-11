from odoo import models, fields, api

class Autor(models.Model):
    _name = 'autor'
    # _rec_name = 'last_name'
    
    name = fields.Char(string='Nombre', required=True)
    last_name = fields.Char(string="Apellido", required=True)

