"""
Flask-ErrorMail
----------

A Flask extension to automatically send stacktrace error e-mails to site 
administrators when 500 errors occur.

Please refer to the online documentation for details.

Links
`````

* `documentation <http://packages.python.org/Flask-ErrorMail>`_
* `development version
  <https://github.com/jasonwyatt/Flask-ErrorMail/tarball/master>`_
"""
from setuptools import setup


setup(
    name='Flask-ErrorMail',
    version='0.1.0',
    url='http://github.com/jasonwyatt/Flask-ErrorMail',
    license='MIT',
    author='Jason Wyatt Feinstein',
    author_email='jason.feinstein@gmail.com',
    description='Flask extension for sending administrators e-mails with stacktraces when internal server errors occur.',
    long_description=__doc__,
    packages=[
        'flask_errormail',
    ],
    test_suite='nose.collector',
    zip_safe=False,
    platforms='any',
    install_requires=[
        'Flask',
        'Flask-Mail',
    ],
    tests_require=[
        'nose',
    ],
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ]
)