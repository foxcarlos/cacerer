# -*- coding: utf-8 -*-
{
    "name": "cacerer_laboratory",
    "summary": """Cacerer Laboratory""",
    "description": """Long description of module's purpose""",
    "author": "Carlos Garcia",
    "website": "https://www.carlosgarciadiaz.com.ar",
    "category": "Uncategorized",
    "version": "15.0.1",
    "depends": ["base", "sale", "contacts"],
    # always loaded
    "data": [
        # 'security/ir.model.access.csv',
        # "views/views.xml",
        # "views/templates.xml",
    ],
    # only loaded in demonstration mode
    # "demo": [
    # "demo/demo.xml",
    # ],
    "application": True,
    "installable": True,
    "development_status": "Alpha",
    # "images": ["static/description/icon.png"],
    "maintainers": ["foxcarlos@gmail.com"],
    "external_dependencies": {
        "python": ["lxml"],
    },
    # "post_init_hook": "_account_post_init",
    "license": "LGPL-3",
}
