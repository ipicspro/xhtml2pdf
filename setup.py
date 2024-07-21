from setuptools import setup, find_packages


setup(name='xhtml2pdf',
    version='0.1',
    url='https://github.com/ipicspro/xhtml2pdf',
    license='MIT',
    author='IS',
    author_email='info@ecommaker.com',
    description='xhtml2pdf',
    #packages=find_packages(exclude=['tests']),
    packages=['xhtml2pdf'],
    long_description=open('README.md').read(),
    zip_safe=False,
    setup_requires=['nose'],
#   dependency_links=['emoji'],
    install_requires=['reportlab','python-bidi'],
    test_suite='nose.collector')

