from odoo import api, fields, models, _
from odoo.exceptions import ValidationError


# class ResPartner(models.Model):
#     _inherit = 'res.partner'
#
#     @api.model
#     def create(self, vals_list):
#         res = super(ResPartner, self).create(vals_list)
#         print('Yes working!')
#         return res


# class SaleOrderInherit(models.Model):
#     _inherit = 'sale.order'
#     patient_name = fields.Char(string='Patient Name')


class HospitalPatient(models.Model):
    _name = 'hospital.patient'
    _rec_name = 'patient_name'
    _description = 'Patient Record'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _order = 'id desc'

    @api.constrains('patient_age')
    def check_age(self):
        for s in self:
            if s.patient_age < 0:
                raise ValidationError(_('The age must be greater than 0'))
            elif s.patient_age > 150:
                raise ValidationError(_(f'The age is {s.patient_age} probably not valid!'))

    @api.depends('patient_age')
    def set_age_group(self):
        for s in self:
            if int(s.patient_age) < 18:
                s.age_group = 'minor'
            else:
                s.age_group = 'major'

    def open_patient_appointment(self):
        return {
            'name': _('Appointments'),
            'domain': [('patient_id', '=', self.id)],
            'view_type': 'form',
            'res_model': 'hospital.appointment',
            'view_id': False,
            'view_mode': 'tree,form',
            'type': 'ir.actions.act_window',
        }

    def get_appointment_count(self):
        count = self.env['hospital.appointment'].search_count([('patient_id', '=', self.id)])
        self.appointment_count = count

    patient_name = fields.Char(string='Name', required=True, track_visibility='always')
    name_seq = fields.Char(string='Patient ID', required=True, copy=False, readonly=True,
                           index=True, default=lambda self: _('New'))
    gender = fields.Selection([
        ('male', 'Male'),
        ('female', 'Female')
    ], default='male', setring='Gender')
    patient_age = fields.Integer('Age', track_visibility='always')
    age_group = fields.Selection([
        ('major', 'Major'),
        ('minor', 'Minor')
    ], setring='Age Group', default='major', compute='set_age_group')
    notes = fields.Text(string='Notes')
    image = fields.Binary(string='Image')
    contact_number = fields.Char(string='Contact Number', track_visibility='always')
    email = fields.Char(string='Email', track_visibility='always')
    blood_group = fields.Char(string='Blood Group', track_visibility='always')
    appointment_count = fields.Integer(string="Appointment", compute='get_appointment_count')
    active = fields.Boolean("Active", default=True)
    doctor_id = fields.Many2one('hospital.doctor', string="Doctor")

    @api.model
    def create(self, vals):
        if vals.get('name_seq', _('New')) == _('New'):
            vals['name_seq'] = self.env['ir.sequence'].next_by_code('hospital.patient.sequence') or _('New')
        result = super(HospitalPatient, self).create(vals)
        return result
