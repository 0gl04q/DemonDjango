from setuptools import setup, find_packages

setup(
    name='DemonDjango',
    version='1.0',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'asgiref==3.8.1',
        'Django==5.0.4',
        'djangorestframework==3.15.1',
        'sqlparse==0.5.0',
        'tzdata==2024.1',
    ],
    scripts=['scripts/demon_script.sh'],
)
