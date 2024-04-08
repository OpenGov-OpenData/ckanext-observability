# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

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
    namespace_packages=['ckanext', 'ckanext.observability'],
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'ckantoolkit>=0.0.7'
        'opentelemetry-api==1.24.0',
        'opentelemetry-sdk==1.24.0',
        'opentelemetry-instrumentation==0.45b0',
        'opentelemetry-instrumentation-flask==0.45b0',
        'opentelemetry-exporter-prometheus==0.45b0',
        'prometheus-client==0.20.0'
    ],
    entry_points='''
    [ckan.plugins]
    opengov_observability=ckanext.observability.plugin:OpenTelemetryPlugin
    '''
)
