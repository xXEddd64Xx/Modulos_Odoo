# -*- coding: utf-8 -*-
from datetime import timedelta

from odoo import models, fields, api
from odoo.exceptions import ValidationError

class BaseArchive(models.AbstractModel):
    
    _name = 'base.archive'
    _description = 'Fichero abstracto'

    
    activo = fields.Boolean(default=True)

    def archivar(self):
        #Por cada registro del modelo
        for record in self:
            #Cambiamos el valor de activo a su version negada
            record.activo = not record.activo


    
#Definimos modelo Biblioteca comic
class BibliotecaComic(models.Model):

    _name = 'biblioteca.comic'
    
    _inherit = ['base.archive']

    _description = 'Medico de Hospital'

    _rec_name = 'nombre'

    #ATRIBUTOS

    nombre = fields.Char('Nombre', required=True, index=True)
    
    apellido = fields.Char('Apellido', required=False)
    
    medico_id = fields.Char('Id de medico', required=True)
    
    


