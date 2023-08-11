from odoo import models, fields, api

class Libros(models.Model):
    _name = 'libros'
    _inherit = ['mail.thread','mail.activity.mixin']

    name = fields.Char(string='Nombre del Libro', required=True, tracking=True)
    editorial = fields.Char(string='Editorial', required=True)
    isbn = fields.Char(string='ISBN', required=True)
    autor_id = fields.Many2one(comodel_name="autor", string="Autor", required=True)
    lastname_autor = fields.Char(related="autor_id.last_name", string="Apellido del Autor")
    image = fields.Binary(string='Image')
    categoria_id = fields.Many2one(comodel_name="categoria.libro")
    state = fields.Selection([('draft','Borrador'),('published','Publicado')], default='draft')
    description = fields.Char(string="Desciption", compute="_compute_description") # store=True para que se almacene en la bdd

    @api.depends('name', 'isbn')
    def _compute_description(self):
        self.description = self.name + ' | ' + self.isbn + ' | ' + self.autor_id.name + ' | ' + self.categoria_id.name

    def boton_publicar(self):
        self.state = 'published'

    def boton_borrador(self):
        self.state = "draft"

    _sql_constraints = [("name_uniq","unique (name)", "El nombre del libro ya existe")]
    #nombre de sql constraint
    #unique () los valores que no queeremos que se dupliquen
    #mensaje de error
    #si se desea borrar esta validacion se la borra directamente a la bdd en el apartado constraints

class CategoriaLibro(models.Model):
    _name ="categoria.libro"

    name = fields.Char(string="Nombre de la categoria")

