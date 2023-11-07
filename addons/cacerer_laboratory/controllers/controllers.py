# -*- coding: utf-8 -*-
# from odoo import http


# class /users/foxcarlos/desarrollo/python/odooProyectos/cacerer/addons/cacererLaboratory(http.Controller):
#     @http.route('//users/foxcarlos/desarrollo/python/odoo_proyectos/cacerer/addons/cacerer_laboratory//users/foxcarlos/desarrollo/python/odoo_proyectos/cacerer/addons/cacerer_laboratory', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('//users/foxcarlos/desarrollo/python/odoo_proyectos/cacerer/addons/cacerer_laboratory//users/foxcarlos/desarrollo/python/odoo_proyectos/cacerer/addons/cacerer_laboratory/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('/users/foxcarlos/desarrollo/python/odoo_proyectos/cacerer/addons/cacerer_laboratory.listing', {
#             'root': '//users/foxcarlos/desarrollo/python/odoo_proyectos/cacerer/addons/cacerer_laboratory//users/foxcarlos/desarrollo/python/odoo_proyectos/cacerer/addons/cacerer_laboratory',
#             'objects': http.request.env['/users/foxcarlos/desarrollo/python/odoo_proyectos/cacerer/addons/cacerer_laboratory./users/foxcarlos/desarrollo/python/odoo_proyectos/cacerer/addons/cacerer_laboratory'].search([]),
#         })

#     @http.route('//users/foxcarlos/desarrollo/python/odoo_proyectos/cacerer/addons/cacerer_laboratory//users/foxcarlos/desarrollo/python/odoo_proyectos/cacerer/addons/cacerer_laboratory/objects/<model("/users/foxcarlos/desarrollo/python/odoo_proyectos/cacerer/addons/cacerer_laboratory./users/foxcarlos/desarrollo/python/odoo_proyectos/cacerer/addons/cacerer_laboratory"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('/users/foxcarlos/desarrollo/python/odoo_proyectos/cacerer/addons/cacerer_laboratory.object', {
#             'object': obj
#         })
