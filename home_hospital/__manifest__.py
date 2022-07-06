{
    'name': 'Home Hospital',
    'version': '1.0',
    'summary' : 'Hospital Management',
    'sequence' :  -100,
    'description': """Hospital Management Software""",
    'category': 'Sales',
    'website': '',
    'license':'LGPL-3',
    'depends': [
        'mail'
    ],
    'data': [
        'security/ir.model.access.csv',

        'views/specialties.xml',
        'views/cities.xml',
        'views/medicaltype.xml',
        'views/physician.xml',
        'views/governorates.xml',
        'views/pricelist.xml',
        'views/packages.xml',
        'views/devices.xml',
        'views/nurse_sheet.xml',
        'views/service.xml',
        'views/category.xml',
        'views/request.xml',
        'views/partnerr.xml',
        'views/companies.xml',

        'views/menu.xml'

    ],
    'demo': [],
    'qweb':[],
    'installable':True,
    'application':True,
    'auto_install':False,
}