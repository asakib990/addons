# -*- coding: utf-8 -*-

from odoo import models, fields, api


class SeEducationBoard(models.Model):
    _name = "se.education.board"
    _description = 'Education Board'

    name = fields.Char(string='Name', required=True)
    code = fields.Char(string='Code', readonly=True)
    education_board_code = fields.Char(string='Education Board Code')
    company_id = fields.Many2one(comodel_name='res.company', default=lambda self: self.env.user.company_id.id)
    note = fields.Text(string='Note')
    academic_medium_type = fields.Selection(
        [
            ('bangla', 'Bangla'),
            ('english', 'English'),
        ],
        string='Academic Medium Type'
    )
    is_allow_for_ssc = fields.Boolean(string='Is Allow SSC/ Equivalent', default=False)
    is_allow_for_hsc = fields.Boolean(string='Is Allow HSC/ Equivalent', default=False)
    is_allow_for_o_level = fields.Boolean(string='Is Allow O-Level', default=False)
    is_allow_for_a_level = fields.Boolean(string='Is Allow A-Level', default=False)
    is_allow_for_diploma = fields.Boolean(string='Is Allow Diploma', default=False)
    is_allow_for_bachelors = fields.Boolean(string='Is Allow Bachelors', default=False)
    is_allow_for_masters = fields.Boolean(string='Is Allow Masters', default=False)

    _sql_constraints = [
        ('code_unique', 'unique(code)', 'Code already exists!'),
        ('name_unique', 'unique(name)', 'Name already exists!'),
    ]

    @api.model
    def create(self, vals):
        vals['code'] = self.env['ir.sequence'].next_by_code('op.education.board')
        res = super(SeEducationBoard, self).create(vals)
        return res
