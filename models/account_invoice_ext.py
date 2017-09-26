from odoo import models, fields, api
from odoo import _


class AccountInvoiceExt(models.Model):
    _inherit = 'account.invoice'

    description = fields.Char()
    
