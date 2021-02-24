# -*- coding: utf-8 -*-

from flectra import models, fields, api, _

# class openacademy(models.Model):
#     _name = 'openacademy.openacademy'

#     name = fields.Char()

#Creating models
# class CreateEmployeeTypeHrContract(models.Model):
#     _name = 'hr.contract.employee.type'
#     employee_type = fields.Selection([
#         ('casual', 'Casual'),
#         ('probation', 'Probation'),
#         ('permanent', 'Permanent')
#     ], default="casual")

# class CreateEmployeeCategoryHrContract(models.Model):
#     _name = 'hr.contract.employee.category'
#     employee_category = fields.Selection([
#         ('senior_executive', 'Senior Executive'),
#         ('executive', 'Executive'),
#         ('junior_executive', 'Junior Executive'),
#         ('category_1', 'Category 1 - Production/Janitorial/Office Asst./Transport Workers'),
#         ('category_2', 'Category 2 – Non Executive Office Employees'),
#         ('category_3', 'Category 3 – Security – Shift Based Work'),
#         ('category_4', 'Category 4 – Technicians – 12 Hours'),
#     ], default="category_1")

# Inheriting models
class ApplicantContractModification(models.Model):
    _inherit = 'hr.contract'
    employee_type = fields.Selection([
        ('casual', 'Casual'),
        ('probation', 'Probation'),
        ('permanent', 'Permanent')
    ], default="casual")
    employee_category = fields.Selection([
        ('senior_executive', 'Senior Executive'),
        ('executive', 'Executive'),
        ('junior_executive', 'Junior Executive'),
        ('category_1', 'Category 1 - Production/Janitorial/Office Asst./Transport Workers'),
        ('category_2', 'Category 2 – Non Executive Office Employees'),
        ('category_3', 'Category 3 – Security'),
        ('category_4', 'Category 4 – Technicians'),
    ], default="category_1", related="employee_id.employee_category")
    user_group_director = fields.Boolean(string="check field", compute='get_user_director')

    @api.depends('user_group_director')
    def get_user_director(self):
        res_user = self.env['res.users'].search([('id', '=', self._uid)])
        if res_user.has_group('dinuth_ceyfoods.hr_user_group_director'):
            self.user_group_director = True
        else:
            self.user_group_director = False