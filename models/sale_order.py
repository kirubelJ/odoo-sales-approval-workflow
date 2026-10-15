from odoo import models,_
from odoo.exceptions import UserError


class SaleOrder(models.Model):
    _inherit = "sale.order"

    def action_confirm(self):
        # Call the original write method to update the record
        for order in self:
            if order.partner_id:
                raise UserError(_(
                    "The following orders are not in a state requiring confirmation"
                ))
        return super(SaleOrder, self).action_confirm(self)
