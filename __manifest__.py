{
    'name': 'Hospital Management',
    'version': '13.0.1.1',
    'summary': 'Module for managing the Hospital',
    'description': 'Hospital Management System',
    'category': 'test',
    'author': 'Unisoft',
    'website': 'unisoft.com',
    'depends': ['mail'],
    'data': [
        'security/ir.model.access.csv',
        'data/data.xml',
        'data/sequence.xml',
        'views/patient.xml',
        'views/appointment.xml',
        'views/doctor.xml',
        'reports/report.xml',
        'reports/patient_card.xml',
    ],
    'demo': [],
    'installable': True,
    'application': True,
    'auto_install': False,
    'external_dependencies': {
        'python': [],
    }
}
