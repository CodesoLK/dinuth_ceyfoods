# -*- coding: utf-8 -*-

from flectra import models, fields, api, _

# class openacademy(models.Model):
#     _name = 'openacademy.openacademy'

#     name = fields.Char()

#inheriting model
class LoanAttributesModification(models.Model):
    _inherit = 'hr.loan'
    guarantee_one = fields.Many2one('hr.employee', string="Guarantee One", domain=[('guarentee_count_total', '<',2 )])
    guarantee_two = fields.Many2one('hr.employee', string="Guarantee Two",  domain=[('guarentee_count_total', '<', 2)])
    
    transfered_loan = fields.Boolean('Transfered Loan', default=False)
    

    


    def loan_transfer_to_the_guarantee(self):
        self.ensure_one()
        pending_installments = self.env['hr.loan.line'].search_count([('loan_id','=',self.id),('paid','=',False)])
        
        return {
            'name': _('Loan Transfer'),
            'type': 'ir.actions.act_window',            
            'res_model': 'loan.transfer.guarantee.wizard',
            'view_mode': 'form',
            'view_type' : 'form',
            
            'context': dict(
                self.env.context,
                default_employee_id=self.employee_id.id,
                default_pending_amount=self.balance_amount,
                default_no_of_installments=pending_installments,
                default_guarantee_one=self.guarantee_one.id,
                default_guarantee_two=self.guarantee_two.id,
                default_loan_id=self.id,
                
            ),
            'target'    : 'new',
        }
  