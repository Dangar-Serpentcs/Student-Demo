from odoo import models, fields, api


class StudentReportWiz(models.TransientModel):
    _name = 'student.report.wiz'

    start_date = fields.Date("Join Date")
    end_date = fields.Date("End Date")

    def std_report(self):
        print('-----------function call--------', self)
        [data] = self.read()
        student = self.env['student.student'].search([('joining_date', '>=', self.start_date), ('joining_date', '<=', self.end_date)])
        print('------------student---', student)

        datas = {
                'model': 'student.student',
                'form': data,
                'studer_ids': student.ids,
                'wiz_start_date': self.start_date,
                'wiz_end_date': self.end_date,
                }
        return self.env.ref('demo_student.action_report_student').report_action(student, data=datas)

        # print('=-==========ctx-----', ctx)
        # print('------------', self.env.context, std_id, self.name)

