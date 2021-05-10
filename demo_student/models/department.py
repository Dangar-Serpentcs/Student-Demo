from odoo import models, fields, api


class DepartmentDepartment(models.Model):
    _name = 'department.department'
    _description = 'Department'
    _rec_name = 'dept_name'

    dept_ids = fields.One2many('subject.subject', 'sub_id', string="Department name")
    dept_name = fields.Char("Department Name", required="True")
    dept_code = fields.Char("code")
    Department = fields.Char("Department")


class SubjectSubject(models.Model):
    _name = 'subject.subject'
    _description = 'Subject'
    _rec_name = 'sub_name'

    sub_id = fields.Many2one('department.department')
    sub_name = fields.Char("Subject name", required="True")
    sub_code = fields.Integer("Code")
    std_sub_id = fields.Many2one('student.student', string="Subjects")
    color = fields.Integer()


class Hobby(models.Model):
    _name = 'student.hobby'
    _description = 'Student Hobbies'
    _rec_name = 'hobby_list'

    hobby_list = fields.Char("Hobbies", required="True")
