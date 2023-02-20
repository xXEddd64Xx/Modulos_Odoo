# -*- coding: utf-8 -*-
from datetime import timedelta

from odoo import models, fields, api
from odoo.exceptions import ValidationError

class BaseArchive(models.AbstractModel):
    #Nombre y descripcion del modelo
    _name = 'base.archive'
    _description = 'Fichero abstracto'

    activo = fields.Boolean(default=True)

    def archivar(self):
        for record in self:
            record.activo = not record.activo

#Definimos modelo Biblioteca comic
class BibliotecaReserva(models.Model):

    _name = 'reserva'

    _description = 'Reservas de biblioteca'

    _inherit = ['base.archive']
    
    comic_id = fields.Many2one('biblioteca.comic', string='Comic', required=True)
    member_id = fields.Many2one('socio', string='Socio', required=True)
    reservation_start = fields.Date(string='Fecha de inicio de reserva', required=True)
    reservation_end = fields.Date(string='Fecha final', required=True)
    
    @api.constrains('reservation_start')
    def _check_start_date(self):
        # Recorremos el modelo
        for record in self:
            #Comprobamos de cada registro, primero que haya una fecha_publicacion
            #y tras ello, que la fecha no sea posterior a la actual.
            if record.reservation_start and record.reservation_start < fields.Date.today():
                #Si procede, lanzamos una excepcion
                raise models.ValidationError('La fecha de inicio debe ser mayor a la actual')
            
    @api.constrains('reservation_end')
    def _check_release_date(self):
        # Recorremos el modelo
        for record in self:
            #Comprobamos de cada registro, primero que haya una fecha_publicacion
            #y tras ello, que la fecha no sea posterior a la actual.
            if record.reservation_end and record.reservation_end < record.reservation_start:
                #Si procede, lanzamos una excepcion
                raise models.ValidationError('La fecha de devolución debe ser mayor a la de inicio')

    

