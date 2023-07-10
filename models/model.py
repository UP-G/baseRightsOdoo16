from odoo import models, fields, api


class base_rights(models.Model):
    _name = 'base_rights.base_rights'
    _description = 'base_rights.base_rights'

    name = fields.Char()
    value = fields.Integer()
    value2 = fields.Float(compute="_value_pc", store=True)
    description = fields.Text()

    @api.depends('value')
    def _value_pc(self):
        for record in self:
            record.value2 = float(record.value) / 100