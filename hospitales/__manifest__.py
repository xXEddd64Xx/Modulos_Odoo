# -*- coding: utf-8 -*-
{
    'name': "Hospital de locos",

    'summary': """
        Aquí solo tratamos a gente rica""",

    'description': """
        Long description of module's purpose
    """,
    
    'application':True,

    'author': "Gallardo Industries",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Tools',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/hospital_medico.xml',
        'views/hospital_paciente.xml'
    ],
    
}
