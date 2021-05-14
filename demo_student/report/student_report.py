import time
from odoo import models, fields, api


class report_student_info(models.AbstractModel):
    _name = 'report.demo_student.report_student_info'

    @api.model
    def _get_report_values(self, docids, data=None):
        student_ids = self.env['student.student'].browse(data.get('studer_ids'))
        user_ids = self._context.get('uid')
        user_id = self.env['res.users'].browse(user_ids)
        return {
            'user_name': user_id.name,
            'email': user_id.login,
            'docs': student_ids,
            'docids': docids,
            'start_date': data.get('wiz_start_date'),
            'end_date': data.get('wiz_end_date'),
            'dept_code':student_ids.dept_ids.dept_code,
            'dept_name':student_ids.dept_ids.dept_name,
            'date_today': fields.Datetime.now(),
        }
