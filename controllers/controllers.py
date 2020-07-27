# -*- coding: utf-8 -*-
from odoo import http
from odoo.http import request


class MyModule(http.Controller):
    @http.route('/hospital/test/', auth='user')
    def index(self, **kw):
        print(kw)
        return "Hello, world"

    @http.route('/hospital/get_patient', type='json', auth='user')
    def get_patient(self):
        all_patient = request.env['hospital.patient'].search([])
        patients = []
        for patient in all_patient:
            item = {
                'id': patient.id,
                'name': patient.patient_name,
                'seq': patient.name_seq
            }
            patients.append(item)
        res = {"status": 200, 'data': patients}
        return res

# class MyModule(http.Controller):
#     @http.route('/my_module/my_module/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/my_module/my_module/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('my_module.listing', {
#             'root': '/my_module/my_module',
#             'objects': http.request.env['my_module.my_module'].search([]),
#         })

#     @http.route('/my_module/my_module/objects/<model("my_module.my_module"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('my_module.object', {
#             'object': obj
#         })
