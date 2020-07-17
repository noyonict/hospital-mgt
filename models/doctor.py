from odoo import api, fields, models


class HospitalDoctor(models.Model):
    _name = 'hospital.doctor'
    _description = 'Hospital Doctor Mgt'

    name = fields.Char('Name', required=True)
    phone = fields.Char('Phone')
    email = fields.Char('Email')
    gender = fields.Selection([
        ('male', 'Male'),
        ('female', 'Female')
    ], default='male', setring='Gender')
    notes = fields.Char('Notes')
    active = fields.Boolean(default=True)
    user_id = fields.Many2one('res.users', string='Related User',
                              help='Current user of the doctor')

