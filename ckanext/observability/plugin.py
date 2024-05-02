# -*- coding: utf-8 -*-
import ckan.plugins as p

from opentelemetry import metrics
from opentelemetry.exporter.otlp.proto.grpc.metric_exporter import OTLPMetricExporter
from opentelemetry.sdk.metrics import MeterProvider
from opentelemetry.sdk.metrics.export import PeriodicExportingMetricReader
from opentelemetry.sdk.resources import SERVICE_NAME, Resource
from opentelemetry.instrumentation.flask import FlaskInstrumentor

import logging
log = logging.getLogger(__name__)

def setup_opentelemetry():
    resource = Resource(attributes={
        SERVICE_NAME: "ckan"
    })
    reader = PeriodicExportingMetricReader(
        OTLPMetricExporter(endpoint="http://grafana-agent-traces.monitoring.svc.cluster.local:4317", insecure=True)
    )
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