{
    'name': "base_rights",

    'description': """
        app of users base rights
    """,
    'author': "TrackMotors",
    'category': 'Uncategorized',
    'version': '0.1',
    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv',
        'security/base_rights_security.xml',
    ],
    'demo': [
    ],
}