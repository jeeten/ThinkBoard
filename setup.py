from setuptools import setup

setup(
    name='ThinkBoard',
    version='1.0',
    #url='http://example.com/flask-sqlite3/',
    packages=['ThinkBoard'],
    include_package_data=True,
    install_requires=[
        'flask',
        'flask-sqlalchemy',
        'flask-marshmallow',
        'flask-migrate',
        'marshmallow-sqlalchemy',
        'mysqlclient',
        'flask-script'
    ],
    license='BSD',
    author='Thinker',
    author_email='thinker@thinkboard.com',
    description='Very short description',
    long_description=__doc__,
    py_modules=['module_name'],
    # if you would be using a package instead use packages instead
    # of py_modules:
    # packages=['flask_sqlite3'],
    zip_safe=False,
    platforms='any',
    classifiers=[
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Think Board License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ]
)
