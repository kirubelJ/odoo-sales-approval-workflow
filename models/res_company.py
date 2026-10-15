from odoo import fields, models


class ResCompany(models.Model):
    _inherit = "res.company"

    habsync_approval_threshold = fields.Monetary(
        string="Approval Threshold", currency_field="currency_id", default=10000.0)