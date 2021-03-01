# -*- coding: utf-8 -*-

from flectra import models, fields, api,_
# from random import random

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
    health_check_report = fields.Selection([('pass', 'Pass'),('fail', 'Fail'),],'Health Check Results')
    guarantee_count_total = fields.Integer(string="Guaranteed", default=0)
    user_group_director = fields.Boolean(string="check field", compute='get_user_director')
    salutation = fields.Selection([
        ('Mr', 'Mr.'),
        ('Miss', 'Miss.'),
        ('Mrs', 'Mrs.'),
        ('Hon', 'Hon.'),
    ], default="Mr")
    employee_category = fields.Selection([
        ('senior_executive', 'Senior Executive'),
        ('executive', 'Executive'),
        ('junior_executive', 'Junior Executive'),
        ('category_1', 'Category 1 - Production/Janitorial/Office Asst./Transport Workers'),
        ('category_2', 'Category 2 – Non Executive Office Employees'),
        ('category_3', 'Category 3 – Security'),
        ('category_4', 'Category 4 – Technicians'),
    ], default="category_1" , string="Employee Category")

    @api.depends('user_group_director')
    def get_user_director(self):
        res_user = self.env['res.users'].search([('id', '=', self._uid)])
        if res_user.has_group('dinuth_ceyfoods.hr_user_group_director'):
            self.user_group_director = True
        else:
            self.user_group_director = False
        
    @api.multi
    def open_employee_guarantee(self):
        return False
        # return {
        #     'name': _('Guarentee'),
        #     'domain': ['|',('guarantee_one', '=', self.user_id.id),('guarantee_two', '=', self.user_id.id)],
        #     'view_type': 'form',
        #     'res_model': 'hr.loan',
        #     'view_id': False,
        #     'view_mode': 'tree,form',
        #     'type': 'ir.actions.act_window',
        # }

        # Calculate guarantee count total

        # @api.depends('random_depend')
        # def _get_guarantee_count_total(self):
        #     guarantee_one_count = self.env['hr.loan'].search_count([('guarantee_one', '=', self.id), ('state', '=', 'approve'),
        #                                                    ('balance_amount', '!=', 0)])
        #     guarantee_two_count = self.env['hr.loan'].search_count([('guarantee_two', '=', self.id), ('state', '=', 'approve'),
        #                                                    ('balance_amount', '!=', 0)])
        #     self.guarantee_count_total = guarantee_one_count+guarantee_two_count

        # Random number generation
        # random_depend = fields.Integer(string="Random", compute='_get_random')
        # @api.one
        # def _get_random(self):
        #     self.random_depend = random.randint(0, 6585)