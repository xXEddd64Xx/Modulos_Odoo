# -*- coding: utf-8 -*-
from odoo import models, fields, api
from odoo.exceptions import ValidationError

#Definimos modelo Hospital paciente
class HospitalPaciente(models.Model):

    _name = 'paciente'

    _description = 'Paciente del hospital'

    _rec_name = 'nombre'
    
    nombre = fields.Char('Nombre', required=True, index=True)
    
    apellido = fields.Char('Apellido', required=False)
    
    sintoma = fields.Char('Sintomas', required=True)

    


