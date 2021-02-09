# -*- coding: utf-8 -*-

from flectra import models, fields, api, _

# class openacademy(models.Model):
#     _name = 'openacademy.openacademy'

#     name = fields.Char()

#Creating models
# class ApplicantExperienceModel(models.Model):
#     _name = 'hr.applicant.experience'
#     experience_months = fields.Integer('exp_months')
#     hr_applicant = fields.Many2one('hr.applicant')

#inheriting model
class DepartmentAttributeModification(models.Model):
    _inherit = 'hr.department'
    is_production = fields.Boolean(string="Production")

