# coding=utf-8
#####################################################
# THIS FILE IS AUTOMATICALLY GENERATED. DO NOT EDIT #
#####################################################
# noqa: E128,E201
from .client import BaseClient
from .client import createApiClient
from .client import config
from .client import createTemporaryCredentials
from .client import createSession
_defaultConfig = config


class TreeherderEvents(BaseClient):
    """
    The taskcluster-treeherder service is responsible for processing
    task events published by TaskCluster Queue and producing job messages
    that are consumable by Treeherder.

    This exchange provides that job messages to be consumed by any queue that
    attached to the exchange.  This could be a production Treeheder instance,
    a local development environment, or a custom dashboard.
    """

    classOptions = {
        "exchangePrefix": "exchange/taskcluster-treeherder/v1/"
    }

    """
    Job Messages

    When a task run is scheduled or resolved, a message is posted to
    this exchange in a Treeherder consumable format.

    This exchange outputs: ``http://schemas.taskcluster.net/taskcluster-treeherder/v1/pulse-job.json#``This exchange takes the following keys:

     * destination: destination (required)

     * project: project (required)

     * reserved: Space reserved for future routing-key entries, you should always match this entry with `#`. As automatically done by our tooling, if not specified.
    """

    def jobs(self, *args, **kwargs):
        return self._makeTopicExchange({'routingKey': [{'multipleWords': False, 'required': True, 'summary': 'destination', 'name': 'destination'}, {'multipleWords': False, 'required': True, 'summary': 'project', 'name': 'project'}, {'multipleWords': True, 'required': False, 'summary': 'Space reserved for future routing-key entries, you should always match this entry with `#`. As automatically done by our tooling, if not specified.', 'name': 'reserved'}], 'name': 'jobs', 'exchange': 'jobs', 'schema': 'http://schemas.taskcluster.net/taskcluster-treeherder/v1/pulse-job.json#'}, *args, **kwargs)

    funcinfo = {
    }


__all__ = ['createTemporaryCredentials', 'config', '_defaultConfig', 'createApiClient', 'createSession', 'TreeherderEvents']
