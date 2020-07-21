{
    'name': 'Hospital Management',
    'version': '13.0.1.2',
    'summary': 'Module for managing the Hospital',
    'description': 'Hospital Management System',
    'author': "Md. Mohaymenul Islam",
    'category': 'test',
    'author': 'Unisoft Systems Limited',
    'website': 'unisoft.com',
    'depends': ['mail', 'sale'],
    'data': [
        'security/ir.model.access.csv',
        'security/security.xml',
        'wizards/create_appointment.xml',
        'data/data.xml',
        'data/corn.xml',
        'data/mail_template.xml',
        'data/sequence.xml',
        'views/patient.xml',
        'views/appointment.xml',
        'views/doctor.xml',
        'views/lab.xml',
        'reports/report.xml',
        'reports/patient_card.xml',
        'reports/sale_report_inherit.xml',
    ],
    'demo': [],
    'installable': True,
    'application': True,
    'auto_install': False,
    'external_dependencies': {
        'python': [],
    }
}
