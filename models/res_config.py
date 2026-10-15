from odoo import api, fields, models

class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'

    habsync_approval_threshold = fields.Monetary(
        related="company_id.habsync_approval_threshold",
        currency_field="currency_id", readonly=False)
