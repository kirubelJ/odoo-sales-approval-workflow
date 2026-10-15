from odoo import models,_
from odoo.exceptions import UserError


class SaleOrder(models.Model):
    _inherit = "sale.order"

    def action_confirm(self):
        for order in self:
            if order.line:
                raise UserError(_(
                    "The following orders are not in a state requiring confirmation"
                ))
        return super(SaleOrder, self).action_confirm(self)
