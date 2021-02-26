# -*- coding: utf-8 -*-

from flectra import models, fields, api, _
from flectra.exceptions import UserError

# class openacademy(models.Model):
#     _name = 'openacademy.openacademy'

#     name = fields.Char()

#inheriting model
class LoanTransferGuaranteeWizard(models.TransientModel):
    _name = 'loan.transfer.guarantee.wizard'

    employee_id = fields.Many2one('hr.employee', string="Employee", readonly=True)
    pending_amount = fields.Float(string="Pending Amount", required=True,)
    no_of_installments = fields.Integer("No of Installments", required=True,)
    guarantee_one = fields.Many2one('hr.employee', string="Guarantee One", required=True, readonly=True)
    percent_guarantee_one = fields.Integer(string="Percentage for Guarantee one (%)", default="50", required=True,)
    guarantee_two = fields.Many2one('hr.employee', string="Guarantee Two", required=True, readonly=True)
    percent_guarantee_two = fields.Integer(string="Percentage for Guarantee Two (%)", default="50", required=True,)

    def create_loans_for_guarantees(self):
        self.ensure_one()
        if self.pending_amount > 0.00 and self.no_of_installments > 0:
            percentage = self.percent_guarantee_one + self.percent_guarantee_two
            if percentage != 100:
                raise UserError(_('Percentages are not correct'))
            loan = self.env['hr.loan']
            guarantee_one_amount = (self.pending_amount * float(self.percent_guarantee_one)) / 100
            guarantee_two_amount = (self.pending_amount * float(self.percent_guarantee_two)) / 100
            one_content = {
                        # 'subject': _('Document-%s Expired On %s') % (i.name, i.expiry_date),
                'employee_id': self.guarantee_one.id,
                'installment': self.no_of_installments,
                'loan_amount': guarantee_one_amount,
                'guarantee_one':'',
                'guarantee_two': '',
                'transferred_loan':True,
            }
            one_loan = loan.create(one_content).compute_installment()

            two_content = {
                        # 'subject': _('Document-%s Expired On %s') % (i.name, i.expiry_date),
                'employee_id': self.guarantee_two.id,
                'installment': self.no_of_installments,
                'loan_amount': guarantee_two_amount,
                'guarantee_one':'',
                'guarantee_two': '',
                'transferred_loan':True,
            }
            two_loan = loan.create(two_content).compute_installment()
            # return {'type': 'ir.actions.act_window_close'}
            # return {
            #     'type': 'ir.actions.act_window_close',
            #     'tag':'reload',
            # }

        else:
            raise UserError(_('Pending Amount and No of installments and need to be more than 0 '))
    
    # def applicant_health_check_result_pass(self,context=None):
    #     applicant_id = context.get('default_id')
    #     search = self.env['hr.applicant'].search([('id','=',applicant_id)])

    #     search.write({
    #         'health_check_report' : 'pass'
    #     })

    # def applicant_health_check_result_fail(self,context=None):
    #     applicant_id = context.get('default_id')
    #     search = self.env['hr.applicant'].search([('id','=',applicant_id)])

    #     search.write({
    #         'health_check_report' : 'fail'
    #     })