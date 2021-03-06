# © 2014-2015 Antiun Ingenieria, SL (Madrid, Spain, http://www.antiun.com)
#             Antonio Espinosa <antonioea@antiun.com>
#             Daniel Gómez-Zurita <danielgz@antiun.com>
# Copyright 2018 Coop IT Easy SCRLfs
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

{
    "name": "Website sale categories mega-menu",
    "summary": "A megamenu to display product categories in the online shop",
    "version": "11.0.1.0.1",
    "category": "Themes/Miscellaneous",
    "website": "https://github.com/OCA/e-commerce/",
    "author": "Antiun Ingeniería S.L., Odoo Community Association (OCA)",
    "license": "AGPL-3",
    "application": False,
    'installable': True,
    "depends": [
        "website_sale",
    ],
    "data": [
        "views/assets.xml",
        "views/layout.xml",
    ],
}
