# -*- coding: utf-8 -*-

from flectra import models, fields, api, _

# class openacademy(models.Model):
#     _name = 'openacademy.openacademy'

#     name = fields.Char()

#inheriting model
class HealthCheckReportWizard(models.TransientModel):
    _name = 'hr.applicant.health.check.wizard'
    message = fields.Text(string="Message for Wizard", readonly=True, default="Record the Results of Health Check")

    def applicant_health_check_result_pass(self,context=None):
        applicant_id = context.get('default_id')
        search = self.env['hr.applicant'].search([('id','=',applicant_id)])

        search.write({
            'health_check_report' : 'pass'
        })
    
    def applicant_health_check_result_fail(self,context=None):
        applicant_id = context.get('default_id')
        search = self.env['hr.applicant'].search([('id','=',applicant_id)])

        search.write({
            'health_check_report' : 'fail'
        })