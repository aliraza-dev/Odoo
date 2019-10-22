# -*- coding: utf-8 -*-

from odoo import models, fields, api
import logging

_logger = logging.getLogger(__name__)


class signature_fields_sales(models.Model):
    _inherit = 'sale.order'
    _description = "Adding Signature Field to Sales Orders"

    x_signature_doc = fields.Binary('Signature Field', help="Add Signature here", required=False)

    x_discount_selection = fields.Selection([
        ('fixed', 'Fixed'),
        ('percentage', 'Percentage')
    ], 'discount', default='fixed')
    x_discount_rate = fields.Float('discount_rate', required=False, default=0.00)

    x_discounted_price = fields.Monetary('Discounted Price', readonly=True,
                                         required=False, default=0.00, compute='_compute_discount')

    # compute method
    @api.depends('amount_total')
    def _compute_discount(self):
        if self.x_discount_rate > 0:
            if self.x_discount_selection == 'percentage':
                self.x_discounted_price = self.amount_untaxed * self.x_discount_rate / 100
                self.amount_total = (self.amount_untaxed - self.x_discounted_price) - self.amount_tax
            elif self.x_discount_selection == 'fixed':
                self.amount_total = (self.amount_untaxed - self.x_discount_rate) - self.amount_tax
                self.x_discounted_price = self.x_discount_rate

    @api.onchange('x_discount_rate')
    def compute_discount_rate(self):
        self._compute_discount()

    @api.onchange('x_discount_selection')
    def _onchange_selection(self):
        self.amount_total = self.amount_untaxed + self.amount_tax
        self.x_discount_rate = 0.0
        self.x_discounted_price = 0.0

# Following code can be used to get anything from sale.order and show it in invoice, you can use any table and any field using following method
class AccountInvoiceRel(models.Model):
    _inherit = 'account.invoice'

    x_signature_doc = fields.Binary(string='Project Name',store=True,related="so_reference.x_signature_doc")

    @api.model
    def get_sale_order_reference(self):
        for rec in self:
            res = rec.env['sale.order'].search([('name', '=', rec.origin)])
            rec.so_reference = res

    so_reference = fields.Many2one('sale.order', compute='get_sale_order_reference')




