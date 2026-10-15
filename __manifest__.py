{
    'name': 'HabSync Sales Approval Workflow',
    'version': '17.0.0.0',
    'category': 'Sales/CRM',
    'sequence': 10,
    'summary': 'Quotes above a threshold need manager approval before confirmation',
    'depends': [
        'base_setup', 'sale_management'
    ],
    'data': ['security/ir.model.access.csv',
             'views/sale_order_approver_views.xml', 'views/res_config_settings_views.xml','views/sale_order_views.xml'],
    'auther': 'HabSync Odoo',
    'installable': True,
    'application': False,
    'license': 'LGPL-3',
}
