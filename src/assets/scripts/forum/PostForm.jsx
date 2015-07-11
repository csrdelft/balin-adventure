let { ModernUIForm } = require('form');
var mui = require('material-ui');
var { SelectField } = mui;
let React = require("react");
let _ = require('underscore');
let mixin = require('object-assign');

class DraadForm extends mixin(ModernUIForm, React.addons.LinkedStateMixin) {

  constructor(props) {
    super(_.extend(props, {
      fields: {
        "titel": {
          "type": "string",
          "required": true,
          "read_only": false,
          "label": "Titel",
          "max_length": 255
        },
        "gesloten": {
          "type": "boolean",
          "required": false,
          "read_only": false,
          "label": "Gesloten"
        },
        "plakkerig": {
          "type": "boolean",
          "required": false,
          "read_only": false,
          "label": "Plakkerig",
        }
      }
    }));
  }
}

module.exports = DraadForm;
