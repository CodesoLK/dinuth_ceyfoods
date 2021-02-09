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
class ApplicantAttributesModification(models.Model):
    _inherit = 'hr.applicant'
    type_id = fields.Many2one('hr.recruitment.degree', "Qualification")
    applicant_experience = fields.Integer(string="Experience (Months)")

