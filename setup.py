# -*- coding: utf-8 -*-
from setuptools import setup, find_packages  # Always prefer setuptools over distutils
from codecs import open  # To use a consistent encoding
from os import path

setup(
    name='ckanext-observability',
    version='0.0.1',
    description="Plugin for Observability using OpenTelemetry and Prometheus in CKAN",
    classifiers=[],
    keywords='',
    author='Sergio Castineyras',
    author_email='scastineyras@opengov.com',
    url='https://github.com/OpenGov-OpenData/ckanext-observability',
    license="AGPL",
    packages=find_packages(exclude=['contrib', 'docs', 'tests*']),
    namespace_packages=['ckanext'],
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'ckantoolkit>=0.0.7',
        'opentelemetry-api==1.24.0',
        'opentelemetry-sdk==1.24.0',
        'opentelemetry-instrumentation==0.45b0',
        'opentelemetry-instrumentation-flask==0.45b0',
        'opentelemetry-exporter-otlp-proto-grpc==1.24.0'
    ],
    entry_points='''
    [ckan.plugins]
    opengov_observability=ckanext.observability.plugin:OpenTelemetryPlugin
    '''
)
