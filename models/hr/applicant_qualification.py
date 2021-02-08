# -*- coding: utf-8 -*-

from flectra import models, fields, api, _

# class openacademy(models.Model):
#     _name = 'openacademy.openacademy'

#     name = fields.Char()

class ApplicantQualification(models.Model):
    _inherit = 'hr.applicant'
    type_id = fields.Many2one('hr.recruitment.degree', "Qualification")