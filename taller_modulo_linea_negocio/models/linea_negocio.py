from odoo import models,fields,api

class LineaNegocio(models.Model):
    _name='taller.linea.negocio'
    _description='Linea de negocios'
    name=fields.Char(string='Nombre Linea de negocio')