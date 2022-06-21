# -*- coding: utf-8 -*-
# Part of TigernixERP. See LICENSE file for full copyright and licensing details.


{
    'name': 'School',
    'category': 'School',
    'summary': 'A Module For School Management',
    'description': """
This module gives you a quick view of your school schedules, accessible from your home page.
You can track your teachers and students.
""",
    'depends': ['base'],
    'data': [
        'views/school_views.xml',
        'views/teacher_views.xml',
        'views/student_views.xml',
        'views/parent_views.xml'
             
    ],
    'application': True,
}
