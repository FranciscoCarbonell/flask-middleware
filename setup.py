from setuptools import setup

setup(
    name='Flask-Middleware',
    version='1.0',
    url='https://github.com/FranciscoCarbonell/flask-middleware',
    license='MIT',
    author='Francisco Carbonell',
    author_email='francabezo@gmail.com',
    description='Basic middleware',
    py_modules=['flask_middleware'],
    zip_safe=False,
    include_package_data=False,
    platforms='any',
    install_requires=['Flask']
)