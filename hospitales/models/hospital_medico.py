# -*- coding: utf-8 -*-
from odoo import models, fields, api
from odoo.exceptions import ValidationError

#Definimos modelo Hospital medico
class HospitalMedico(models.Model):

    _name = 'medico'

    _description = 'Medicos del hospital'

    _rec_name = 'nombre'
    
    nombre = fields.Char('Nombre', required=True, index=True)
    
    apellido = fields.Char('Apellido', required=False)
    
    medico_id = fields.Char('Id de medico', required=True)

    


