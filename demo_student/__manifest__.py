{
    "name": "demo student",
    "version": "13.0.1.0.1",
    "license": "LGPL-3",
    "depends": ['base'],
    "sequence": 1,
    "author": "Serpent Consulting Services Pvt. Ltd.",
    "maintainer": "Serpent Consulting Services Pvt. Ltd.",
    "website": "http://www.serpentcs.com",
    "category": "Human Resources",
    "description": """
        to manage student detail
    """,
    "summary": """
        student
    """,
    'data': [
        'security/student_security.xml',
        'security/ir.model.access.csv',
        'views/studentview.xml',
        'views/student_config_view.xml',
        'report/student_report.xml',
        'wizard/std_report_wiz.xml'
        ],
    'installable': True,
    'auto_install': False,
    'application': True,
}