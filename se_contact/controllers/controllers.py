# -*- coding: utf-8 -*-
# from odoo import http


# class SeContact(http.Controller):
#     @http.route('/se_contact/se_contact', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/se_contact/se_contact/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('se_contact.listing', {
#             'root': '/se_contact/se_contact',
#             'objects': http.request.env['se_contact.se_contact'].search([]),
#         })

#     @http.route('/se_contact/se_contact/objects/<model("se_contact.se_contact"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('se_contact.object', {
#             'object': obj
#         })
