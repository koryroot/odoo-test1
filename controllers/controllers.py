# -*- coding: utf-8 -*-
# from odoo import http


# class WendryModule(http.Controller):
#     @http.route('/wendry_module/wendry_module/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/wendry_module/wendry_module/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('wendry_module.listing', {
#             'root': '/wendry_module/wendry_module',
#             'objects': http.request.env['wendry_module.wendry_module'].search([]),
#         })

#     @http.route('/wendry_module/wendry_module/objects/<model("wendry_module.wendry_module"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('wendry_module.object', {
#             'object': obj
#         })
