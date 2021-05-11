import time
from odoo import models, fields, api
from datetime import datetime
from odoo.exceptions import ValidationError, UserError
from lxml import etree


class StudentStudent(models.Model):
    _name = 'student.student'
    _description = 'Student Student'

    name = fields.Char("Name", required="True")
    teacher_name = fields.Many2one('teacher.information', "Teacher Name")
    last_name = fields.Char("Last name")
    email = fields.Char("Email")
    phone = fields.Char("Phone Number")
    birthdate = fields.Date("BirthDate")
    gender = fields.Selection([('male', 'Male'),
                               ('female', 'Female'),
                               ('other', 'Other')], "Gender", default='male')
    current_date = fields.Datetime("Current Time", default=lambda self: time.strftime('%Y-%m-%d %H:%M:%S'))
    signature = fields.Html("Signature")
    state = fields.Selection([('draft', 'Draft'),
                              ('approve', 'Approve'),
                              ('reject', 'Reject')], "State", default='draft')
    above_eighteen = fields.Boolean(string="Above 18 ?")
    code = fields.Char("Student code", required="True")
    std_image = fields.Binary("Student's image", max_width=10, max_height=10)
    partner_id = fields.Many2one('res.partner', "Related Partner", readonly=True)
    category_id = fields.Many2many('res.partner.category', string="Tags")
    state = fields.Selection([('draft', 'Draft'),
                              ('approve', 'Approve'),
                              ('reject', 'Reject')], "State", default='draft')
    dept_ids = fields.Many2one('department.department', string="department")
    hobby_ids = fields.Many2many('student.hobby',
                                 # 'student_hobby_type_rel',
                                 # 'student_id', 'hobby_id',
                                 string="Hobbies")
    color = fields.Integer()
    active = fields.Boolean('active', default=True)
    sub_id = fields.One2many('subject.subject', 'std_sub_id', string="subjects")
    dept_code = fields.Char("Department Code")
    joining_date = fields.Date("Joining Date", required="True")
    end_date = fields.Date("End Date")
    start_date = fields.Date("Join Date", required="True")
    user_id = fields.Many2one('res.users', "User Name", readonly=True)
    _sql_constraints = [
        ('quq_code', 'check(len(code>6))', 'code must be of at least 6 characters')
    ]

    @api.constrains('birthdate', 'code')
    def _check_birthdate(self):
        # print('--------------constrains---------------------',self)
        # if self.birthdate and self.birthdate == datetime.today().date():
        #  raise ValidationError("Birthday should not be today!")
        if len(self.code) > 4:
            raise ValidationError("code must not be more than 4 characters!")

    @api.onchange('dept_ids')
    def _onchange_dept_code(self):
        self.dept_code = False
        if self.dept_ids:
            self.dept_code = self.dept_ids.dept_code

    def unlink(self):
        for rec in self:
            if rec.state == 'approve':
                raise ValidationError("can not delete till it's in approve state")
        return super(StudentStudent, self).unlink()

    def state_change(self):
        self.state = 'approve'

    def state_rej(self):
        self.state = 'reject'

    def create_user(self):
        user = self.env['res.users'].with_context(no_reset_password=True).create({'name': self.name,
                                                                                  'login': self.email})
        self.user_id = user.id

    @api.model
    def default_get(self, fields):
        result = super(StudentStudent, self).default_get(fields)
        result.update({
                 'phone': "8678687987"
                 })
        return result

    @api.model
    def fields_view_get(self, view_id=None, view_type='form', toolbar=False, submenu=False):
        res = super(StudentStudent, self).fields_view_get(view_id=view_id, view_type=view_type,
                                                          toolbar=toolbar, submenu=submenu)
        if view_type == 'form':
            doc = etree.XML(res['arch'])
            import json
            for node in doc.xpath("//field[@name='last_name']"):
                modifiers = json.loads(node.get("modifiers"))
                modifiers['invisible'] = True
                node.set("modifiers", json.dumps(modifiers))
            res['arch'] = etree.tostring(doc, encoding='unicode')
        return res

    @api.model
    def name_search(self, name='', args=None, operator='ilike', limit=100):
        res = super(StudentStudent, self).name_search(name, args, operator, limit=limit)
        return res

    def name_get(self):
        if self.check_access_rights('read', raise_exception=False):
            res = super(StudentStudent, self).name_get()
            return res
        return self.env['student.student'].browse(self.ids).name_get()

    def std_report(self):
        view_wiz_form_ref = self.env.ref('demo_student.view_wiz_form')
        action = {
            'name': 'Student Report',
            'view_mode': 'form',
            'res_model': 'student.report.wiz',
            'view_id': self.env.ref('demo_student.view_wiz_form').id,
            'type': 'ir.actions.act_window',
            'target': 'new'
        }
        return action


class TeacherInformation(models.Model):
    _name = 'teacher.information'
    _description = 'Teacher Information'

    name = fields.Char("Teacher Name", required="True")
    student_id = fields.One2many('student.student', 'teacher_name', "students")
    state = fields.Selection([('draft', 'Draft'),
                              ('approve', 'Approve'),
                              ('reject', 'Reject')], "State", default='draft')
    email = fields.Char("Email")
    user_id = fields.Many2one('res.users', "User Name", readonly=True)

    def state_change(self):
        self.state = 'approve'

    def state_rej(self):
        self.state = 'reject'

    def create_user(self):
        user = self.env['res.users'].with_context(no_reset_password=True).create({'name': self.name,
                                                                                  'login': self.email})
        self.user_id = user.id


class ContactTag(models.Model):
    _inherit = 'res.partner'

    # name = fields.Char("Name")
    # email=fields.Char("email")
    # phone = fields.Char("Phone")
    # category_id = fields.Many2many('res.partner.category', strting="Tags")

    def write(self, vals):
        part_dict = self.env['res.partner']
        # part_obj = part_dict.search([('name', '=', 'test')])

        # res = {'name': vals.get('name')}

        return super(ContactTag, self).write(vals)
