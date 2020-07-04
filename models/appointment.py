from odoo import api, fields, models, _
from odoo.exceptions import ValidationError


class HospitalAppointment(models.Model):
    _name = 'hospital.appointment'
    _description = 'Patient Appointment'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _order = 'appointment_date, id desc'

    def get_default_note(self):
        return 'e.g: Critical patient'

    def get_patient_id(self):
        return 3

    def action_confirm(self):
        for rec in self:
            rec.state = 'confirm'

    def action_done(self):
        for rec in self:
            rec.state = 'done'

    name = fields.Char(string="Appointment ID", required=True, copy=False, readonly=True,
                       index=True, default=lambda self: _('New'))
    patient_id = fields.Many2one('hospital.patient', string="Patient", required=True, default=get_patient_id)
    patient_age = fields.Integer('Age', related='patient_id.patient_age')
    notes = fields.Text(string="Registration Note", default=get_default_note)
    doctor_note = fields.Text(string="Doctor Notes")
    pharmacy_note = fields.Text(string="Pharmacy Notes")
    appointment_date = fields.Date(string='Date', required=True)
    state = fields.Selection([
        ('draft', 'Draft'),
        ('confirm', 'Confirm'),
        ('done', 'Done'),
        ('cancel', 'Cancelled'),
    ], string="Status", readonly=True, default='draft', track_visibility='always')

    @api.model
    def create(self, vals):
        if vals.get('name', _('New')) == _('New'):
            vals['name'] = self.env['ir.sequence'].next_by_code('hospital.patient.appointment.sequence') or _('New')
        result = super(HospitalAppointment, self).create(vals)
        return result
