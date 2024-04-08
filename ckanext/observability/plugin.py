# -*- coding: utf-8 -*-
import ckan.plugins as p

from prometheus_client import start_http_server

from opentelemetry import metrics
from opentelemetry.exporter.prometheus import PrometheusMetricReader
from opentelemetry.sdk.metrics import MeterProvider
from opentelemetry.instrumentation.flask import FlaskInstrumentor
from opentelemetry.sdk.resources import SERVICE_NAME, Resource

def setup_opentelemetry():
    resource = Resource(attributes={
        SERVICE_NAME: "ckan-opengov"
    })
    # Start Prometheus client
    start_http_server(port=9464)
    print('Starting HTTP WebServer on port 9464...')
    # Initialize PrometheusMetricReader which pulls metrics from the SDK
    # on-demand to respond to scrape requests
    reader = PrometheusMetricReader()
    provider = MeterProvider(resource=resource, metric_readers=[reader])
    metrics.set_meter_provider(provider)

class OpenTelemetryPlugin(p.SingletonPlugin):
    p.implements(p.IMiddleware, inherit=True)
    p.implements(p.IConfigurable, inherit=True)

    def configure(self, config):
        setup_opentelemetry()

    def make_middleware(self, app, config):
        FlaskInstrumentor().instrument_app(app)
        return app