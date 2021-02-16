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