# -*- coding: utf-8 -*-

from flectra import models, fields, api, _
from datetime import datetime

# class openacademy(models.Model):
#     _name = 'openacademy.openacademy'

#     name = fields.Char()

class HRPayrollBonus(models.Model):
    _name = 'hr.payroll.bonus'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _rec_name = 'name_seq'
    name_seq = fields.Char(string='Bonus Sequence', required=True, copy=False, readonly=True, index=True, default=lambda self: _('New'))
    employee = fields.Many2one('hr.employee', string="Employee")
    employment_confirmed_date = fields.Date(string='Employment Confirmed on')
    current_date = fields.Date(string='Today', default=datetime.today())
    amount = fields.Float('Amount')
    total = fields.Float('Total Payable')
    user_group_director = fields.Boolean(string="check field", compute='get_user_director')
    state = fields.Selection([
        ('draft', 'Draft'),
        ('waiting_approval', 'Waiting Approval'),
        ('approved', 'Approved'),
        ('refused', 'Refused'),
        ('canceled', 'Canceled'),
    ], string="State", default='draft', track_visibility='onchange', copy=False, )

    @api.depends('user_group_director')
    def get_user_director(self):
        res_user = self.env['res.users'].search([('id', '=', self._uid)])
        if res_user.has_group('dinuth_ceyfoods.hr_user_group_director'):
            self.user_group_director = True
        else:
            self.user_group_director = False

    @api.onchange('amount','employment_confirmed_date')
    def calculate_total(self):
        if self.employment_confirmed_date and self.current_date:
            employment_confirmed_on = datetime.strptime(str(self.employment_confirmed_date), '%Y-%m-%d')
            current_date_is = datetime.strptime(str(self.current_date), '%Y-%m-%d')
            worked_days = current_date_is - employment_confirmed_on
            total = round(int(worked_days.days)/30)
            self.total = total * self.amount

    @api.onchange('employee')
    def get_employment_confirmed_date(self):
        contract = self.env['hr.contract'].search([('employee_id', '=', self.employee.id), ('employee_type', '=', 'permanent')], limit=1)
        contract_permanent_date = contract.date_start
        self.employment_confirmed_date = contract_permanent_date

    @api.model
    def create(self, vals):
        if vals.get('name_seq', _('New')) == _('New'):
            vals['name_seq'] = self.env['ir.sequence'].next_by_code('hr.payroll.bonus.sequence') or _('New')

        result = super(HRPayrollBonus, self).create(vals)
        return result

    @api.multi
    def action_refuse(self):
        self.write({'state': 'refused'})

    @api.multi
    def action_submit(self):
        self.write({'state': 'waiting_approval'})

    @api.multi
    def action_cancel(self):
        self.write({'state': 'canceled'})

    @api.multi
    def action_approve(self):
        self.write({'state': 'approved'})

# HR Bonus Fixed
class HRPayrollBonusFixed(models.Model):
    _name = 'hr.payroll.bonus.fixed'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _rec_name = 'name_seq'
    name_seq = fields.Char(string='Bonus Sequence', required=True, copy=False, readonly=True, index=True,
                           default=lambda self: _('New'))
    employee = fields.Many2one('hr.employee', string="Employee")
    employment_confirmed_date = fields.Date(string='Employment Confirmed on')
    current_date = fields.Date(string='Today', default=datetime.today())
    total = fields.Float('Total Payable')
    user_group_director = fields.Boolean(string="check field", compute='get_user_director')
    state = fields.Selection([
        ('draft', 'Draft'),
        ('waiting_approval', 'Waiting Approval'),
        ('approved', 'Approved'),
        ('refused', 'Refused'),
        ('canceled', 'Canceled'),
    ], string="State", default='draft', track_visibility='onchange', copy=False, )

    @api.depends('user_group_director')
    def get_user_director(self):
        res_user = self.env['res.users'].search([('id', '=', self._uid)])
        if res_user.has_group('dinuth_ceyfoods.hr_user_group_director'):
            self.user_group_director = True
        else:
            self.user_group_director = False

    @api.model
    def create(self, vals):
        if vals.get('name_seq', _('New')) == _('New'):
            vals['name_seq'] = self.env['ir.sequence'].next_by_code('hr.payroll.bonus.fixed.sequence') or _('New')

        result = super(HRPayrollBonusFixed, self).create(vals)
        return result

    @api.multi
    def action_refuse(self):
        self.write({'state': 'refused'})

    @api.multi
    def action_submit(self):
        self.write({'state': 'waiting_approval'})

    @api.multi
    def action_cancel(self):
        self.write({'state': 'canceled'})

    @api.multi
    def action_approve(self):
        self.write({'state': 'approved'})