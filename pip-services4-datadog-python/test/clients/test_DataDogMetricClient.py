# -*- coding: utf-8 -*-
import datetime
import os

from pip_services4_components.config import ConfigParams
from pip_services4_data.random import RandomDouble

from pip_services4_datadog.clients.DataDogMetric import DataDogMetric
from pip_services4_datadog.clients.DataDogMetricPoint import DataDogMetricPoint
from pip_services4_datadog.clients.DataDogMetricType import DataDogMetricType
from pip_services4_datadog.clients.DataDogMetricsClient import DataDogMetricsClient


class TestDataDogMetricClient:
    _client: DataDogMetricsClient

    def setup_method(self):
        api_key = os.environ.get('DATADOG_API_KEY') or '782673bc9be6ba74ed5cb5e189596047'

        self._client = DataDogMetricsClient()

        config = ConfigParams.from_tuples(
            'source', 'test',
            'credential.access_key', api_key
        )

        self._client.configure(config)

        self._client.open(None)

    def teardown_method(self):
        self._client.close(None)

    def test_send_metrics(self):
        metrics = [
            DataDogMetric(
                metric='test.metric.1',
                service='TestService',
                host='TestHost',
                type=DataDogMetricType.Gauge,
                points=[
                    DataDogMetricPoint(time=datetime.datetime.now(),
                                       value=RandomDouble.next_double(0, 100))
                ]
            ),
            DataDogMetric(
                metric='test.metric.2',
                service='TestService',
                host='TestHost',
                type=DataDogMetricType.Rate,
                interval=100,
                points=[
                    DataDogMetricPoint(time=datetime.datetime.now(),
                                       value=RandomDouble.next_double(0, 100))
                ]
            ),
            DataDogMetric(
                metric='test.metric.3',
                service='TestService',
                host='TestHost',
                type=DataDogMetricType.Count,
                interval=100,
                points=[
                    DataDogMetricPoint(time=datetime.datetime.now(),
                                       value=RandomDouble.next_double(0, 100))
                ]
            )
        ]

        self._client.send_metrics(None, metrics)
