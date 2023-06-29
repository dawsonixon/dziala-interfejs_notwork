{
  'name': 'My Typed.js Module',  
  'version': '1.0',  
  'category': 'Website',  
  'summary': 'Adds Typed.js typing animation to website.',  
  'sequence': 10,  
  'author': 'Your Name',  
  'maintainer': 'Your Name',  
  'website': 'https://www.yourwebsite.com',  
  'depends': ['website'],  
  'data': [
    'templates/snippets.xml',
  ],
  'assets': {  
    'web.assets_frontend': [  
      'my_typedjs_module/static/src/js/typed.js',  
      'my_typedjs_module/static/src/js/typedjs_init.js',  
      'my_typedjs_module/static/src/css/typedjs.css'  
    ],  
    'web.assets_qweb': [  
      'my_typedjs_module/static/src/xml/editor.xml',
      'my_typedjs_module/static/src/xml/website_templates.xml',
    ]  
  },
  'demo': [],  
  'installable': True,  
  'application': True,  
  'auto_install': False,  
  'description': 'This is a custom module for Odoo which adds Typed.js typing animation to the website'
}

