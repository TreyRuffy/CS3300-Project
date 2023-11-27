from django import template

register = template.Library()

navbar_items = [
    {
        'title': 'Home',
        'url': '/'
    },
    {
        'title': 'About',
        'url': '/about'
    },
    {
        'title': 'Contact',
        'url': '/contact'
    },
    {
        'title': 'Horses',
        'url': 'horses',
        'children': [
            {
                'title': 'Add Horse',
                'url': '/add_horse'
            },
            {
                'title': 'Edit Horse',
                'url': '/edit_horse'
            },
            {
                'title': 'Delete Horse',
                'url': '/delete_horse'
            }
        ]
    },
    {
        'title': 'Account',
        'url': 'account',
        'children': [
            {
                'title': 'Login',
                'url': '/login'
            },
            {
                'title': 'Logout',
                'url': '/logout'
            },
            {
                'title': 'Register',
                'url': '/register'
            }
        ]
    }
]

@register.inclusion_tag('cs3300_project/includes/navbar.html')
def navbar(active=None, username=None):
    return {"navbar_items": navbar_items, 'active': active, 'username': username}