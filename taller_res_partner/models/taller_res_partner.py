from odoo import models, fields, api, _

class ResPartner(models.Model):
    _inherit = 'res.partner'
    ingreso = fields.Char(string="Ingreso")