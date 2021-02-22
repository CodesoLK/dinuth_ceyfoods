# -*- coding: utf-8 -*-

from flectra import models, fields, api, _

# class openacademy(models.Model):
#     _name = 'openacademy.openacademy'

#     name = fields.Char()

#inheriting model
class LoanAttributesModification(models.Model):
    _inherit = 'hr.loan'
    guarantee_one = fields.Many2one('hr.employee', string="Guarantee One",required=True, domain=[('loan_count', '<',2 )])
    guarantee_two = fields.Many2one('hr.employee', string="Guarantee Two", required=True, domain=[('loan_count', '<',2 )])

    # @api.model
    # def create(self, values):
    #     loan_count = self.env['hr.loan'].search_count([('employee_id', '=', values['employee_id']), ('state', '=', 'approve'),
    #                                                    ('balance_amount', '!=', 0)])
    #     guarentee_one_count = self.env['hr.loan'].search_count([('guarantee_one', '=', values['employee_id']), ('state', '=', 'approve'),
    #                                                    ('balance_amount', '!=', 0)])
    #     guarentee_one_count = self.env['hr.loan'].search_count([('guarantee_two', '=', values['employee_id']), ('state', '=', 'approve'),
    #                                                    ('balance_amount', '!=', 0)])
    #     guarentee_count_total = guarentee_one_count+guarentee_one_count
        
    #     if loan_count:
    #         raise except_orm('Error!', 'The employee has already a pending installment')
    #     else:
    #         values['name'] = self.env['ir.sequence'].get('hr.loan.seq') or ' '
    #         res = super(HrLoan, self).create(values)
    #         return res
    
    # @api.multi
    # def open_employee_guarentee(self):
    #     return {
    #         'name': _('Guarentee'),
    #         'domain': ['|',('guarantee_one', '=', self.id),('guarantee_two', '=', self.id)],
    #         'view_type': 'form',
    #         'res_model': 'hr.loan',
    #         'view_id': False,
    #         'view_mode': 'tree,form',
    #         'type': 'ir.actions.act_window',
    #     }