from setuptools import setup, find_packages
setup(
    name='astra-python', 
    version='0.1', 
    description='Astra authentication protocol for python-requests',
    author='Kirsten Hunter',
    author_email='kirsten.hunter@datastax.com',
    url='https://github.com/synedra-datastax/astra-python',
    namespace_packages=['astra'],
    packages=find_packages(),
    python_requires=">=3.3.0",
    install_requires = [
        'requests>=2.3.0',
        'pyOpenSSL >= 0.13',
        'ndg-httpsclient',
        'pyasn1',
        'urllib3'
    ],
    license='LICENSE.txt'
)
