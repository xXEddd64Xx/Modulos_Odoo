from odoo import models, fields

class Book(models.Model):
    _name = 'library.book'
    name = fields.Char(string='Título', required=True)
    author_id = fields.Many2one('res.partner', string='Autor')
    isbn = fields.Char(string='ISBN')
    publication_date = fields.Date(string='Fecha de publicación')
    active = fields.Boolean(default=True)
    note = fields.Text(string='Nota')