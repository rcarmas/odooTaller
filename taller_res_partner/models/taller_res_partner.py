from odoo import models, fields, api, _

class ResPartner(models.Model):
    _inherit = 'res_partner'
    ingreso=fields.Char(string="Nombre Relacionado")