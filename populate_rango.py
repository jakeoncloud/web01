import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mysite.settings')

import django
django.setup()

from rango.models import Category, Page


def add_page(cat, title, url, views=0):
    p = Page.objects.get_or_create(category=cat, title=title)[0]
    p.url = url
    p.views = views
    p.save()
    return p


def add_cat(name, views=0, likes=0):
    c = Category.objects.get_or_create(name=name)
    c[0].views = views
    c[0].likes = likes
    c[0].save()
    return c


def populate():

    # First create dictionaries to store pages.
    python_pages = [
        {"title": "Offcial Django Tutorial",
         "url": "https://docs.python.org/3/tutorial/index.html"},
        {"title": "How to Think Like a Computer Scientist",
         "url": "http://www.greenteapress.com/thinkpython/"},
        {"title": "Learn Python in 10 Minutes",
         "url": "http://www.korokithakis.net/tutorials/python/"}
    ]

    django_pages = [
        {"title": "Official Django Tutorial",
         "url": "https://docs.djangoproject.com/en/1.10/intro/tutorial01/"},
        {"title": "Django Rocks",
         "url": "http://www.djangorocks.com/"},
        {"title": "How to Tango with Django",
         "url": "http://www.tangowithdjango.com/"}
    ]

    other_pages = [
        {"title": "Bottle",
         "url": "http://bottlepy.org/docs/dev/"},
        {"title": "Flask",
         "url": "http://flask.pocoo.org"}
    ]

    # Then dictionary for Categories that take pages dict above and store in
    # within
    cats = {"Python": {"pages": python_pages, "views": 128, 'likes': 64},
            "Django": {"pages": django_pages, 'views': 64, 'likes': 32},
            "Other Frameworks": {"pages": other_pages, 'views': 32, 'likes': 16}
            }

    for cat, cat_data in cats.items():
        c = add_cat(cat, cat_data['views'], cat_data['likes'])[0]

        for p in cat_data["pages"]:
            page = add_page(c, p["title"], p['url'])

    for c in Category.objects.all():

        for page in Page.objects.filter(category=c):
            print("{0} - {1}".format(str(c), str(page)))


if __name__ == "__main__":
    print('Starting Rango Population Script...')
    populate()
