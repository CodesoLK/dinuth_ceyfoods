# -*- coding: utf-8 -*-

from flectra import models, fields, api, _

# class openacademy(models.Model):
#     _name = 'openacademy.openacademy'

#     name = fields.Char()

#inheriting model
class EmployeeAttributesModification(models.Model):
    _inherit = 'hr.employee'
    type_id = fields.Many2one('hr.recruitment.degree', "Qualification")
    applicant_experience = fields.Integer(string="Experience (Months)")
    is_production = fields.Boolean(string="Production")
    health_check = fields.Boolean(string="Health Check Eligibility")
    health_check_report = fields.Selection([ ('pass', 'Pass'),('fail', 'Fail'),],'Health Check Results')
    salutation = fields.Selection([
        ('Mr', 'Mr.'),
        ('Miss', 'Miss.'),
        ('Mrs', 'Mrs.'),
        ('Hon', 'Hon.'),
    ], default="Mr")
    user_group_director = fields.Boolean(string="check field", compute='get_user_director')

    @api.depends('user_group_director')
    def get_user_director(self):
        res_user = self.env['res.users'].search([('id', '=', self._uid)])
        if res_user.has_group('dinuth_ceyfoods.hr_user_group_director'):
            self.user_group_director = True
        else:
            self.user_group_director = False

    # @api.one
    # def _compute_employee_guarentee(self):
    #     """This compute the loan amount and total loans count of an employee.
    #         """
    #     self.loan_count = self.env['hr.loan'].search_count([('employee_id', '=', self.id)])

    # loan_count = fields.Integer(string="Loan Count", compute='_compute_employee_guarentee')