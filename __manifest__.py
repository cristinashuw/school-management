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
    'depends': ['web','base'],
    'data': [
        'views/jurusan_kuliah_action.xml',
        'views/jurusan_kuliah_menuitem.xml',
        'views/jurusan_kuliah_view.xml',
        'views/parents_action.xml',
        'views/parents_menuitem.xml',
        'views/parents_view.xml',
        'views/school_action.xml',
        'views/school_menuitem.xml',
        'views/school_view.xml',
        'views/student_action.xml',
        'views/student_menuitem.xml',
        'views/student_view.xml',
        'views/teacher_action.xml',
        'views/teacher_menuitem.xml',
        'views/teacher_view.xml',
        
             
    ],
    'application': True,
}
