from odoo import models, fields, api, _


class CreatAppointment(models.TransientModel):
    _name = 'create.appointment'
    _description = 'Create Appointment'

    patient_id = fields.Many2one('hospital.patient', string='Patient')
    appointment_date = fields.Date(string='Appointment Date')
    note = fields.Text('Notes', default='Created form the wizard.')

    def create_appointment(self):
        vals = {
            'patient_id': self.patient_id.id,
            'appointment_date': self.appointment_date,
        }
        self.patient_id.message_post(body='Appointment Created Successfully', subject='Appointment Creation')
        self.env['hospital.appointment'].create(vals)

    def get_data(self):
        print('Get data function worked!')
        # appointments = self.env['hospital.appointment'].search(['patient_id', '=', 2])
        appointments = self.env['hospital.appointment'].search([])
        for appointment in appointments:
            print('Appointment ID:', appointment.name)
        return{
            'type': 'ir.actions.do_nothing'
        }

