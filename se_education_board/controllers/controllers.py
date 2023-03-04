# -*- coding: utf-8 -*-
# from odoo import http


# class SeEducationBoard(http.Controller):
#     @http.route('/se_education_board/se_education_board', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/se_education_board/se_education_board/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('se_education_board.listing', {
#             'root': '/se_education_board/se_education_board',
#             'objects': http.request.env['se_education_board.se_education_board'].search([]),
#         })

#     @http.route('/se_education_board/se_education_board/objects/<model("se_education_board.se_education_board"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('se_education_board.object', {
#             'object': obj
#         })
