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
class BibliotecaSocio(models.Model):

    _name = 'paciente'

    _description = 'Paciente del hospital'

    _rec_name = 'nombre'

    _inherit = ['base.archive']
    
    nombre = fields.Char('Nombre', required=True, index=True)
    
    apellido = fields.Char('Apellido', required=False)
    
    sintoma = fields.Char('Sintomas', required=False)

    


