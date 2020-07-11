from odoo import models


class PatientCardXLS(models.AbstractModel):
    _name = 'report.om_hospital.report_patient_xls'
    _inherit = 'report.report_xlsx.abstract'

    def generate_xlsx_report(self, workbook, data, obj):
        format1 = workbook.add_format({'font_size': 12, 'align': 'vcenter', 'bold': True})
        format2 = workbook.add_format({'font_size': 10, 'align': 'vcenter'})
        sheet = workbook.add_worksheet('Patient Card')
        sheet.write(2, 2, 'Name', format1)
        sheet.write(2, 3, 'Age', format1)
        sheet.write(3, 2, obj.patient_name, format2)
        sheet.write(3, 3, obj.patient_age, format2)


# class PatientCardXLS(models.AbstractModel):
#     _name = 'report.om_hospital.report_patient_xls'
#     _inherit = 'report.report_xlsx.abstract'
#
#     def generate_xlsx_report(self, workbook, data, partners):
#         for obj in partners:
#             report_name = obj.name
#             # One sheet by partner
#             sheet = workbook.add_worksheet(report_name[:31])
#             bold = workbook.add_format({'bold': True})
#             sheet.write(0, 0, obj.name, bold)
