from odoo import models, fields, api
from odoo.exceptions import ValidationError

# from se_education_core.models.se_contact import SeContact


class SeStudentCourse(models.Model):
    _name = "se.student.course"
    _description = "Student Course Details"
    _rec_name = 'student_id'

    student_id = fields.Many2one('se.student', 'Student', ondelete="cascade")
    course_id = fields.Many2one('se.course', 'Course', required=True)
    batch_id = fields.Many2one('se.batch', 'Batch', required=True)
    roll_number = fields.Char('Roll Number')
    subject_ids = fields.Many2many('se.subject', string='Subjects')

    _sql_constraints = [
        ('unique_name_roll_number_id',
         'unique(roll_number,course_id,batch_id,student_id)',
         'Roll Number & Student must be unique per Batch!'),
        ('unique_name_roll_number_course_id',
         'unique(roll_number,course_id,batch_id)',
         'Roll Number must be unique per Batch!'),
        ('unique_name_roll_number_student_id',
         'unique(student_id,course_id,batch_id)',
         'Student must be unique per Batch!'),
    ]

    @api.model
    def get_import_templates(self):
        return [{

        }]


class SeStudent(models.Model):
    _name = "se.student"
    _description = "Student"
    _inherits = {"res.partner": "partner_id"}
    # _inherit = ["se.contact"]
    # _inherit = ['mail.thread', 'mail.activity.mixin']

    first_name = fields.Char(string="First Name", translate=True)
    middle_name = fields.Char(string="Middle Name", translate=True)
    last_name = fields.Char(string="Last Name", translate=True)
    student_image = fields.Image("Image")
    birth_date = fields.Date('Birth Date')
    # title = fields.Many2one('res.partner.title', 'Title', states={'done': [('readonly', True)]})   #title should be in admission model
    blood_group = fields.Selection([
        ('A+', 'A+ve'),
        ('B+', 'B+ve'),
        ('O+', 'O+ve'),
        ('AB+', 'AB+ve'),
        ('A-', 'A-ve'),
        ('B-', 'B-ve'),
        ('O-', 'O-ve'),
        ('AB-', 'AB-ve'),
    ], string='Blood Group')
    gender = fields.Selection([
        ('m', 'Male'),
        ('f', 'Female'),
        ('o', 'Other')
    ], string='Gender', required=True, default='m')
    lang = fields.Selection([
        ('eng_us', 'English (US)'),
        ('eng_uk', 'English (UK)'),
    ], string='Language')
    visa_info = fields.Char(string='Visa Info')
    id_number = fields.Char(string='ID Card Number')
    mobile = fields.Char(string="Mobile Number", required=True)
    gr_no = fields.Char(string="GR Number")
    active = fields.Boolean(default=True)
    contact_ids = fields.One2many('se.contact', 'student_id', 'Contact')
    # contact_ids = SeContact.student_id.__class__.__name__
    # contact_ids = fields.One2many(
    #     comodel_name='se.student',
    #     inverse_name='student_id',
    #     string='Contact_ids')

    # nationality = fields.Many2one('res.country', 'Nationality')
    # emergency_contact = fields.Many2one('res.partner', 'Emergency Contact')
    # partner_id = fields.Many2one('res.partner', 'Partner', required=True, ondelete="cascade")
    # user_id = fields.Many2one('res.users', 'User', ondelete="cascade")
    # category_id = fields.Many2one('se.category', 'Category')
    # course_detail_ids = fields.One2many('se.student.course', 'student_id', 'Course Details', track_visibility='onchange')

    _sql_constraints = [(
        'unique_gr_no',
        'unique(gr_no)',
        'GR Number must be unique per student!'
    )]

    @api.onchange('first_name', 'middle_name', 'last_name')
    def _onchange_name(self):
        if not self.middle_name:
            self.name = str(self.first_name) + " " + str(
                self.last_name
            )
        else:
            self.name = str(self.first_name) + " " + str(
                self.middle_name) + " " + str(self.last_name)

    @api.constrains('birth_date')
    def _check_birthdate(self):
        for record in self:
            if record.birth_date > fields.Date.today():
                raise ValidationError((
                    "Birth Date can't be greater than current date!"))

    def create_student_user(self):
        user_group = self.env.ref("base.group_portal") or False
        users_res = self.env['res.users']
        for record in self:
            if not record.user_id:
                user_id = users_res.create({
                    'name': record.name,
                    'partner_id': record.partner_id.id,
                    'login': record.email,
                    'groups_id': user_group,
                    'is_student': True,
                    # 'tz': self._context.get('tz'),        #time_zone
                })
                record.user_id = user_id
