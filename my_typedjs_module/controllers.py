from odoo import http
from odoo.http import request

class TypedJsConfigController(http.Controller):
    @http.route('/my_typedjs_module/get_config', type='json', auth='public')
    def get_config(self):
        config = request.env['my_typedjs_module.config'].sudo().search([], limit=1)

        if config:
            return {
                'strings': config.strings.split('\n'),
                'typeSpeed': config.typeSpeed,
                'backSpeed': config.backSpeed,
                'loop': config.loop,
            }
        else:
            return {}
