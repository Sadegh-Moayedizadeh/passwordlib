from setuptools import find_packages, setupsetup(
    name = 'passwordlib',
    packages = find_packages(include=['passwordlib']),
    version = '0.1.0',
    description = 'library to help you create sufficient passwords',
    author = 'Mohamad Sadegh Moayedizadeh',
    license = '',
    install_requires = [],
    setup_requires = [],
    test_suite = 'tests',
)
