# -*- coding: utf-8 -*-
{
    'name': "SmartEdu Education Board",
    'summary': 'Education Board Management System.',
    'description': 'Education Board Management System',
    'author': "DSL",
    'category': 'Tools',
    'version': '0.1',
    'depends': ['base',
                'se_education_core',
                ],
    'data': [
        # security
        'security/ir.model.access.csv',
        # views
        'views/se_education_board_view.xml',
        'views/menus.xml',
    ],
    'demo': [],
}
