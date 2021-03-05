# -*- coding: utf-8 -*-

from flectra import models, fields, api,_
# from random import random

# class openacademy(models.Model):
#     _name = 'openacademy.openacademy'

#     name = fields.Char()

#inheriting model
class EmployeeBankAttributesModification(models.Model):
    _inherit = 'res.partner.bank'
    branch_name = fields.Text(string="Branch Name")