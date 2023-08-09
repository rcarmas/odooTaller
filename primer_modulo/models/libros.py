from odoo import models, fields, api

class Libros(models.Model):
    _name = 'libros'

    name = fields.Char(string='Nombre del Libro', required=True)
    editorial = fields.Char(string='Editorial', required=True)
    isbn = fields.Char(string='ISBN', required=True)
    autor_id = fields.Many2one(comodel_name="autor", string="Autor", required=True)

