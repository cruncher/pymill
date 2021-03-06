from setuptools import setup
__author__ = 'yalnazov'

setup(
    name='paymill-wrapper',
    version='2.4.1',
    description='Python wrapper for PAYMILL API',
    author='Aleksandar Yalnazov',
    author_email='aleksandar.yalnazov@qaiware.com',
    url='https://github.com/paymill/paymill-python',
    license='MIT',
    packages=['paymill', 'paymill.models', 'paymill.services', 'paymill.utils'],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
    install_requires=['requests >= 2.1.0', 'jsonobject>=0.8']  # 'paymill-jsonobject>=0.7.1beta'
)
