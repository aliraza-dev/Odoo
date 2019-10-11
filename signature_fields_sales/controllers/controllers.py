# -*- coding: utf-8 -*-
from odoo import http

# class SignatureFieldsSales(http.Controller):
#     @http.route('/signature_fields_sales/signature_fields_sales/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/signature_fields_sales/signature_fields_sales/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('signature_fields_sales.listing', {
#             'root': '/signature_fields_sales/signature_fields_sales',
#             'objects': http.request.env['signature_fields_sales.signature_fields_sales'].search([]),
#         })

#     @http.route('/signature_fields_sales/signature_fields_sales/objects/<model("signature_fields_sales.signature_fields_sales"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('signature_fields_sales.object', {
#             'object': obj
#         })