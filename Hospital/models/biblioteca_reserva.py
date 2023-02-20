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

    _description = 'Diagnosticos del hospital'

    _inherit = ['base.archive']
    
    paciente = fields.Many2one('socio', string='Paciente', required=True, index=True)

    medico = fields.Many2one('biblioteca.comic', string='Medico', required=True, index=True)

    diagnostico = fields.Html('Diagnóstico', sanitize=True, strip_style=False)
    

    

