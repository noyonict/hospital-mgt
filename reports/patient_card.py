from odoo import api, models


class PatientCardReport(models.AbstractModel):
    _name = 'report.om_hospital.report_patient'
    _description = 'Patient Card Report'

    @api.model
    def _get_report_values(self, docids, data=None):
        # print('Report function working!')
        model = self.env.context.get('active_model')
        # print('Model', model)
        # print('docids', docids)
        # print('data', data)
        docs = self.env['hospital.patient'].browse(docids[0])
        appointments = self.env['hospital.appointment'].search([('patient_id', '=', docids[0])])
        print('appointments:', appointments)
        print('docs:', docs)
        # report_obj = self.env['ir.actions.report']
        # print('report obj', report_obj)
        # report = report_obj._get_report_from_name('module.report_name')
        docargs = {
            'doc_model': 'hospital.patient',
            'docs': docs,
            'appointments': appointments,
            'data': data,
        }
        return docargs
