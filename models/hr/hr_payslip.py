# -*- coding: utf-8 -*-

from flectra import models, fields, api, _


# class openacademy(models.Model):
#     _name = 'openacademy.openacademy'

#     name = fields.Char()

# Inheriting models
class pays(models.Model):
    inherit = 'hr.payslip'

    @api.multi
    def action_payslip_done(self):
        for line in self.input_line_ids:
            if line.loan_line_id:
                line.loan_line_id.paid = True
                x = True
                loan = self.env['hr.loan'].search([('id', '=', line.loan_line_id.loan_id.id)])
                for rec in loan.loan_lines:
                    if rec.paid == False:
                        x = False
                if x == True:
                    loan.state = 'finish'

        return super(pays, self).action_payslip_done()
