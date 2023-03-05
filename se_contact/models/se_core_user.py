from odoo import api, fields, models
from odoo.exceptions import ValidationError

class SeContact(models.Model):
    _name = 'se.core.user'
    _description = 'SeUser'

    name = fields.Char(string="Name")
    login = fields.Char(string='Login')
    is_student = fields.Boolean(string='Is Student')

