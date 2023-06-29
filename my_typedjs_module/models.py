from odoo import models, fields

class TypedJsConfig(models.Model):
    _name = 'my_typedjs_module.config'
    _description = 'Typed.js Configuration'

    strings = fields.Text(string='Strings', required=True, default='First sentence.\nSecond sentence.')
    typeSpeed = fields.Integer(string='Type Speed', required=True, default=40)
    backSpeed = fields.Integer(string='Back Speed', required=True, default=50)
    loop = fields.Boolean(string='Loop', required=True, default=True)
