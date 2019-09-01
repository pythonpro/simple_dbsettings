import os
from setuptools import find_packages, setup

with open(os.path.join(os.path.dirname(__file__), 'README.rst')) as readme:
    README = readme.read()

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='django-simple-dbsettings',
    version='0.0.1',
    packages=find_packages(),
    include_package_data=True,
    install_requires=['django-polymorphic==2.1.2'],
    license='BSD License',
    description='Django Simple DB Settings app',
    long_description=README,
    url='https://github.com/pythonpro/simple_dbsettings',
    author='pythonpro',
    author_email='pythonprogrammer@mail.ru',
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Framework :: Django :: 2.2',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.7',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    ],
)