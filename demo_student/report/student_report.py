import time
from odoo import models, fields, api


class report_student_info(models.AbstractModel):
    _name = 'report.demo_student.report_student_info'

    @api.model
    def _get_report_values(self, docids, data=None):
        """in this function can access the data returned from the button
    click function"""
        # print('----docids-----', docids)
        # print('------data--', type(data.get('studer_ids')))
        # print('-----context---', self._context)
        # print('-----uid---', self._uid)

        # report = self.env['ir.actions.report']._get_report_from_name('module.report_name')

        student_ids = self.env['student.student'].browse(data.get('studer_ids'))

        # print('------record------', student_ids.dept_ids.dept_name)
        # value = []
        user_ids = self._context.get('uid')
        # print('--------user_ids-------------',user_ids)

        user_id = self.env['res.users'].browse(user_ids)
        # print('---------user_id--------',user_id.name, user_id.login)


        return {
            # 'user' : user_name,
            # 'user_loggedin' : user_id,
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
        # return {
        #     'lines': docids.get_lines()
        # }
        # query = """SELECT *
        # FROM sale_order as so
        # JOIN sale_order_line AS sl ON so.id = sl.sale_order_id
        # WHERE sl.id = %s"""
        # value.append(student.student)
        # self._cr.execute(query, value)
        # record = self._cr.dictfetchall()
        # return {
        #         'docs': record,
        #         'date_today': fields.Datetime.now(),
        # }

