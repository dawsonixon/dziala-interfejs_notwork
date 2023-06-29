odoo.define('my_typedjs_module.typedjs_init', function (require) {  
    'use strict';  
  
    var publicWidget = require('web.public.widget');  
  
    publicWidget.registry.TypedJs = publicWidget.Widget.extend({  
      selector: '.element', // Replace .element with the selector of the element you want the typing animation on.  
  
      start: function () {  
        var self = this;
        this._rpc({
          route: '/my_typedjs_module/get_config'
        }).then(function (config) {
          var options = {  
            strings: config.strings, // Dynamic strings from the config
            typeSpeed: config.typeSpeed, // Dynamic type speed from the config
            backSpeed: config.backSpeed, // Dynamic back speed from the config
            loop: config.loop // Dynamic loop value from the config
          };  
  
          var typed = new Typed(self.selector, options);  
        });
      }  
    });  
  
    return publicWidget.registry.TypedJs;
  });
  
   