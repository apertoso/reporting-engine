# -*- coding: utf-8 -*-

from odoo.addons.report_py3o.py3o_parser import py3o_report_extender


# retrieve the record for a given field
def _get_field(obj, field_names):
    if len(field_names) == 1:
        return obj._fields[field_names[0]]
    else:
        return _get_field(obj[field_names[0]], field_names[1:])


@py3o_report_extender()
def report_sample_extender(report_xml, localcontext):
    def get_label(obj, field_name):
        """
        Retrieve the field name for a certain record

        :param odoo_field_object: example: objname.partner_id.bank_ids
        :return: translated label string for the field bank_ids
        """

        foo = report_xml
        bar = localcontext

        obj = obj.with_context(lang=localcontext.get('lang'))
        env = obj.env
        field_obj = _get_field(obj, field_name.split('.'))
        return field_obj._description_string(env)

    def hello_world(name):
        return "Hello, %s" % name

    localcontext.update({
        'get_label': get_label,
        'hello_world': hello_world,
    })
