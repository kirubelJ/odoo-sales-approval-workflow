from odoo import models, fields, _


class SaleOrderApprover(models.Model):
    _name = "sale.order.approver"

    user_id = fields.Many2one(
        comodel_name='res.users',
        string="Salesperson",
        tracking=2,
    )
