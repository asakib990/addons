from odoo import api, fields, models
from odoo.exceptions import ValidationError


class SeContact(models.Model):
    _name = 'se.contact'
    _description = 'SeContact'

    name = fields.Char(string="Name")
    type = fields.Selection([
        ('invoice', 'Invoice Address'),
        ('delivery', 'Delivery Address'),
        ('other', 'Other Address'),
        ('private', 'Private Address'),
    ], string='Address Type')
    street = fields.Char(string="Street")
    street2 = fields.Char(string='Street2')
    city = fields.Char(string='City')
    country = fields.Char(string='Country')
    state = fields.Char(string='State')
    zip = fields.Char(string='Zip')
    student_id = fields.Many2one('se.student', string='Student_id')

