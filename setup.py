from setuptools import setup, find_packages

setup(
    name='daemon_django_apps',
    version='1.0',
    packages=find_packages(),
    package_data={
        'daemon_django_apps': ['info/templates/*', 'scripts/daemon_script.sh'],
    },
    include_package_data=True,
    install_requires=[
        'asgiref==3.8.1',
        'Django==5.0.4',
        'django-bootstrap5==24.2'
        'djangorestframework==3.15.1',
        'sqlparse==0.5.0',
        'tzdata==2024.1',
    ],
)
