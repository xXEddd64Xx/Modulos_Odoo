# -*- coding: utf-8 -*-
from datetime import timedelta

from odoo import models, fields, api
from odoo.exceptions import ValidationError


# Modelo base, creado como modelo abstracto 
# Este modelo lo heredarara el modelo BibliotecaComic
# Y se ha creado puramente con fin didáctico para ver herencia entre modelos

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

    _name = 'socio'

    _description = 'Socio de biblioteca'

    _inherit = ['base.archive']
    
    nombre = fields.Char('Nombre', required=True)
    
    apellido = fields.Char('Apellido', required=False)
    
    socio_ids = fields.Char('Id', required=False,)

    


