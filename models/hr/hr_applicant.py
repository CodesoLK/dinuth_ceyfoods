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
    is_production = fields.Boolean(string="Production")
    health_check = fields.Boolean(string="Health Check Eligibility")
    health_check_report = fields.Selection([ ('pass', 'Pass'),('fail', 'Fail'),],'Health Check Results')
    marital = fields.Selection([
        ('single', 'Single'),
        ('married', 'Married'),
        ('cohabitant', 'Legal Cohabitant'),
        ('widower', 'Widower'),
        ('divorced', 'Divorced')
    ], string='Marital Status', default='single')
    gender = fields.Selection([
        ('male', 'Male'),
        ('female', 'Female'),
        ('other', 'Other')
    ], default="male")
    salutation = fields.Selection([
        ('Mr', 'Mr.'),
        ('Miss', 'Miss.'),
        ('Mrs', 'Mrs.'),
        ('Hon', 'Hon.'),
    ], default="Mr")

    def create_health_record(self):
        ctx = {
            'default_id': self.id,
        }

        return {
            'name'      : _('Health Check Report'),
            'type'      : 'ir.actions.act_window',
            'res_model' : 'hr.applicant.health.check.wizard',
            'view_mode' : 'form',
            'view_type' : 'form',
            'context'   : ctx,
            'target'    : 'new'
        }

    @api.multi
    def create_employee_from_applicant(self):
        # Stage change of the applicant to seleceted
        stageID = self.env['hr.recruitment.stage'].search([('name','=','Selected')])
        self.stage_id = stageID

        """ Create an hr.employee from the hr.applicants """
        employee = False
        for applicant in self:
            contact_name = False
            if applicant.partner_id:
                address_id = applicant.partner_id.address_get(['contact'])['contact']
                contact_name = applicant.partner_id.name_get()[0][1]
            else :
                new_partner_id = self.env['res.partner'].create({
                    'is_company': False,
                    'name': applicant.partner_name,
                    'email': applicant.email_from,
                    'phone': applicant.partner_phone,
                    'mobile': applicant.partner_mobile
                })
                address_id = new_partner_id.address_get(['contact'])['contact']
            if applicant.job_id and (applicant.partner_name or contact_name):
                applicant.job_id.write({'no_of_hired_employee': applicant.job_id.no_of_hired_employee + 1})
                employee = self.env['hr.employee'].create({
                    'name': applicant.partner_name or contact_name,
                    'job_id': applicant.job_id.id,
                    'address_home_id': address_id,
                    'department_id': applicant.department_id.id or False,
                    'address_id': applicant.company_id and applicant.company_id.partner_id
                            and applicant.company_id.partner_id.id or False,
                    'work_email': applicant.department_id and applicant.department_id.company_id
                            and applicant.department_id.company_id.email or False,
                    'work_phone': applicant.department_id and applicant.department_id.company_id
                            and applicant.department_id.company_id.phone or False,
                    'salutation' : applicant.salutation,
                    'type_id' : applicant.type_id.id,
                    'marital' : applicant.marital,
                    'gender'  : applicant.gender,
                    'applicant_experience' : applicant.applicant_experience,
                    'is_production' : applicant.is_production,
                    'health_check' : applicant.health_check,
                    'health_check_report' : applicant.health_check_report})

                applicant.write({'emp_id': employee.id})
                applicant.job_id.message_post(
                    body=_('New Employee %s Hired') % applicant.partner_name if applicant.partner_name else applicant.name,
                    subtype="hr_recruitment.mt_job_applicant_hired")
                employee._broadcast_welcome()
            else:
                raise UserError(_('You must define an Applied Job and a Contact Name for this applicant.'))

        employee_action = self.env.ref('hr.open_view_employee_list')
        dict_act_window = employee_action.read([])[0]
        if employee:
            dict_act_window['res_id'] = employee.id
        dict_act_window['view_mode'] = 'form,tree'
        return dict_act_window


