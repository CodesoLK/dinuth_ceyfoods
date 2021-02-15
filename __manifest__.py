{
    'name': "Dinuth Cey Foods",
    'version': '1.0.0',
    'sequence': 1,
    'depends': ['base','hr','hr_recruitment'],
    'author': "Sathir M. Mansoor, ©2020. Fortrax Solutions All Rights Reserved.",
    'license':"OPL-1",
    'summary': 'Crafted for Dinuth Cey Foods',
    'category': 'Specific Industry Applications',
    'description': "Dinuth Cey Foods wants to achieve with the ERP product and has been prepared based on the client specifications and after a thorough analysis of the client company.",

    'images' : [],
    'qweb': [],
    
    # data files always loaded at installation
    'data': [
        # Views
        'views/hr/hr_applicant.xml',
        'views/hr/hr_department.xml',
        'views/hr/hr_employee.xml',

        # Data
        'data/hr/stages_for_interview_process.xml',
        'data/hr/schedule_interview_activity_types.xml',
        'data/hr/hr_applicant_qualification.xml',

        # Wizard
        'wizard/hr/applicant_health_check.xml',

        # Security
        'security/hr/ir.model.access.csv',
        'security/hr/security.xml',
    ],

    # website
    'website': 'https://codeso.lk/',
    
    # data files containing optionally loaded demonstration data
    'demo': [],
    'installable': True,
    'application': True,
    'auto_install': False,
}