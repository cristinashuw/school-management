{
    'name': 'School',
    'category': 'School',
    'summary': 'A Module For School Management',
    'description': """
This module gives you a quick view of your school schedules, accessible from your home page.
You can track your teachers and students.
""",
    
    'website':'',
    'author':'Cristina',
    'depends':['web','base'],
    'data':[
        'security/ir.model.access.csv',
        
        'views/registration_view.xml',
        'views/teacher_view.xml',
        'views/student_view.xml',
        'views/wali_murid_view.xml',
        'views/score_nilai_view.xml',


        'views/registration_action.xml',
        'views/teacher_action.xml',
        'views/student_action.xml',
        'views/wali_murid_action.xml',
        'views/score_nilai_action.xml',

        'views/school_menuitem.xml',
        'reports/register_student_qweb.xml'
    ],
    'installable': True,
    'application': True,
    'license': 'OEEL-1',
}