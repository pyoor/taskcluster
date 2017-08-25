# coding=utf-8
#####################################################
# THIS FILE IS AUTOMATICALLY GENERATED. DO NOT EDIT #
#####################################################
# noqa: E128,E201
from .asyncclient import AsyncBaseClient
from .asyncclient import createApiClient
from .asyncclient import config
from .asyncclient import createTemporaryCredentials
from .asyncclient import createSession
_defaultConfig = config


class SchedulerEvents(AsyncBaseClient):
    """
    The scheduler, typically available at `scheduler.taskcluster.net` is
    responsible for accepting task-graphs and schedule tasks on the queue as
    their dependencies are completed successfully.

    This document describes the AMQP exchanges offered by the scheduler,
    which allows third-party listeners to monitor task-graph submission and
    resolution. These exchanges targets the following audience:
     * Reporters, who displays the state of task-graphs or emails people on
       failures, and
     * End-users, who wants notification of completed task-graphs

    **Remark**, the task-graph scheduler will require that the `schedulerId`
    for tasks is set to the `schedulerId` for the task-graph scheduler. In
    production the `schedulerId` is typically `"task-graph-scheduler"`.
    Furthermore, the task-graph scheduler will also require that
    `taskGroupId` is equal to the `taskGraphId`.

    Combined these requirements ensures that `schedulerId` and `taskGroupId`
    have the same position in the routing keys for the queue exchanges.
    See queue documentation for details on queue exchanges. Hence, making
    it easy to listen for all tasks in a given task-graph.

    Note that routing key entries 2 through 7 used for exchanges on the
    task-graph scheduler is hardcoded to `_`. This is done to preserve
    positional equivalence with exchanges offered by the queue.
    """

    classOptions = {
        "exchangePrefix": "exchange/taskcluster-scheduler/v1/"
    }

    """
    Task-Graph Running Message

    When a task-graph is submitted it immediately starts running and a
    message is posted on this exchange to indicate that a task-graph have
    been submitted.

    This exchange outputs: ``http://schemas.taskcluster.net/scheduler/v1/task-graph-running-message.json#``This exchange takes the following keys:

     * routingKeyKind: Identifier for the routing-key kind. This is always `'primary'` for the formalized routing key. (required)

     * taskId: Always takes the value `_`

     * runId: Always takes the value `_`

     * workerGroup: Always takes the value `_`

     * workerId: Always takes the value `_`

     * provisionerId: Always takes the value `_`

     * workerType: Always takes the value `_`

     * schedulerId: Identifier for the task-graphs scheduler managing the task-graph this message concerns. Usually `task-graph-scheduler` in production. (required)

     * taskGraphId: Identifier for the task-graph this message concerns (required)

     * reserved: Space reserved for future routing-key entries, you should always match this entry with `#`. As automatically done by our tooling, if not specified.
    """

    def taskGraphRunning(self, *args, **kwargs):
        return self._makeTopicExchange({'routingKey': [{'constant': 'primary', 'multipleWords': False, 'required': True, 'summary': "Identifier for the routing-key kind. This is always `'primary'` for the formalized routing key.", 'name': 'routingKeyKind'}, {'multipleWords': False, 'required': False, 'summary': 'Always takes the value `_`', 'name': 'taskId'}, {'multipleWords': False, 'required': False, 'summary': 'Always takes the value `_`', 'name': 'runId'}, {'multipleWords': False, 'required': False, 'summary': 'Always takes the value `_`', 'name': 'workerGroup'}, {'multipleWords': False, 'required': False, 'summary': 'Always takes the value `_`', 'name': 'workerId'}, {'multipleWords': False, 'required': False, 'summary': 'Always takes the value `_`', 'name': 'provisionerId'}, {'multipleWords': False, 'required': False, 'summary': 'Always takes the value `_`', 'name': 'workerType'}, {'multipleWords': False, 'required': True, 'summary': 'Identifier for the task-graphs scheduler managing the task-graph this message concerns. Usually `task-graph-scheduler` in production.', 'name': 'schedulerId'}, {'multipleWords': False, 'required': True, 'summary': 'Identifier for the task-graph this message concerns', 'name': 'taskGraphId'}, {'multipleWords': True, 'required': False, 'summary': 'Space reserved for future routing-key entries, you should always match this entry with `#`. As automatically done by our tooling, if not specified.', 'name': 'reserved'}], 'name': 'taskGraphRunning', 'exchange': 'task-graph-running', 'schema': 'http://schemas.taskcluster.net/scheduler/v1/task-graph-running-message.json#'}, *args, **kwargs)

    """
    Task-Graph Extended Message

    When a task-graph is extended, that is additional tasks is added to the
    task-graph, a message is posted on this exchange. This is useful if you
    are monitoring a task-graph and what to track states of the individual
    tasks in the task-graph.

    This exchange outputs: ``http://schemas.taskcluster.net/scheduler/v1/task-graph-extended-message.json#``This exchange takes the following keys:

     * routingKeyKind: Identifier for the routing-key kind. This is always `'primary'` for the formalized routing key. (required)

     * taskId: Always takes the value `_`

     * runId: Always takes the value `_`

     * workerGroup: Always takes the value `_`

     * workerId: Always takes the value `_`

     * provisionerId: Always takes the value `_`

     * workerType: Always takes the value `_`

     * schedulerId: Identifier for the task-graphs scheduler managing the task-graph this message concerns. Usually `task-graph-scheduler` in production. (required)

     * taskGraphId: Identifier for the task-graph this message concerns (required)

     * reserved: Space reserved for future routing-key entries, you should always match this entry with `#`. As automatically done by our tooling, if not specified.
    """

    def taskGraphExtended(self, *args, **kwargs):
        return self._makeTopicExchange({'routingKey': [{'constant': 'primary', 'multipleWords': False, 'required': True, 'summary': "Identifier for the routing-key kind. This is always `'primary'` for the formalized routing key.", 'name': 'routingKeyKind'}, {'multipleWords': False, 'required': False, 'summary': 'Always takes the value `_`', 'name': 'taskId'}, {'multipleWords': False, 'required': False, 'summary': 'Always takes the value `_`', 'name': 'runId'}, {'multipleWords': False, 'required': False, 'summary': 'Always takes the value `_`', 'name': 'workerGroup'}, {'multipleWords': False, 'required': False, 'summary': 'Always takes the value `_`', 'name': 'workerId'}, {'multipleWords': False, 'required': False, 'summary': 'Always takes the value `_`', 'name': 'provisionerId'}, {'multipleWords': False, 'required': False, 'summary': 'Always takes the value `_`', 'name': 'workerType'}, {'multipleWords': False, 'required': True, 'summary': 'Identifier for the task-graphs scheduler managing the task-graph this message concerns. Usually `task-graph-scheduler` in production.', 'name': 'schedulerId'}, {'multipleWords': False, 'required': True, 'summary': 'Identifier for the task-graph this message concerns', 'name': 'taskGraphId'}, {'multipleWords': True, 'required': False, 'summary': 'Space reserved for future routing-key entries, you should always match this entry with `#`. As automatically done by our tooling, if not specified.', 'name': 'reserved'}], 'name': 'taskGraphExtended', 'exchange': 'task-graph-extended', 'schema': 'http://schemas.taskcluster.net/scheduler/v1/task-graph-extended-message.json#'}, *args, **kwargs)

    """
    Task-Graph Blocked Message

    When a task is completed unsuccessfully and all reruns have been
    attempted, the task-graph will not complete successfully and it's
    declared to be _blocked_, by some task that consistently completes
    unsuccessfully.

    When a task-graph becomes blocked a messages is posted to this exchange.
    The message features the `taskId` of the task that caused the task-graph
    to become blocked.

    This exchange outputs: ``http://schemas.taskcluster.net/scheduler/v1/task-graph-blocked-message.json#``This exchange takes the following keys:

     * routingKeyKind: Identifier for the routing-key kind. This is always `'primary'` for the formalized routing key. (required)

     * taskId: Always takes the value `_`

     * runId: Always takes the value `_`

     * workerGroup: Always takes the value `_`

     * workerId: Always takes the value `_`

     * provisionerId: Always takes the value `_`

     * workerType: Always takes the value `_`

     * schedulerId: Identifier for the task-graphs scheduler managing the task-graph this message concerns. Usually `task-graph-scheduler` in production. (required)

     * taskGraphId: Identifier for the task-graph this message concerns (required)

     * reserved: Space reserved for future routing-key entries, you should always match this entry with `#`. As automatically done by our tooling, if not specified.
    """

    def taskGraphBlocked(self, *args, **kwargs):
        return self._makeTopicExchange({'routingKey': [{'constant': 'primary', 'multipleWords': False, 'required': True, 'summary': "Identifier for the routing-key kind. This is always `'primary'` for the formalized routing key.", 'name': 'routingKeyKind'}, {'multipleWords': False, 'required': False, 'summary': 'Always takes the value `_`', 'name': 'taskId'}, {'multipleWords': False, 'required': False, 'summary': 'Always takes the value `_`', 'name': 'runId'}, {'multipleWords': False, 'required': False, 'summary': 'Always takes the value `_`', 'name': 'workerGroup'}, {'multipleWords': False, 'required': False, 'summary': 'Always takes the value `_`', 'name': 'workerId'}, {'multipleWords': False, 'required': False, 'summary': 'Always takes the value `_`', 'name': 'provisionerId'}, {'multipleWords': False, 'required': False, 'summary': 'Always takes the value `_`', 'name': 'workerType'}, {'multipleWords': False, 'required': True, 'summary': 'Identifier for the task-graphs scheduler managing the task-graph this message concerns. Usually `task-graph-scheduler` in production.', 'name': 'schedulerId'}, {'multipleWords': False, 'required': True, 'summary': 'Identifier for the task-graph this message concerns', 'name': 'taskGraphId'}, {'multipleWords': True, 'required': False, 'summary': 'Space reserved for future routing-key entries, you should always match this entry with `#`. As automatically done by our tooling, if not specified.', 'name': 'reserved'}], 'name': 'taskGraphBlocked', 'exchange': 'task-graph-blocked', 'schema': 'http://schemas.taskcluster.net/scheduler/v1/task-graph-blocked-message.json#'}, *args, **kwargs)

    """
    Task-Graph Finished Message

    When all tasks of a task-graph have completed successfully, the
    task-graph is declared to be finished, and a message is posted to this
    exchange.

    This exchange outputs: ``http://schemas.taskcluster.net/scheduler/v1/task-graph-finished-message.json#``This exchange takes the following keys:

     * routingKeyKind: Identifier for the routing-key kind. This is always `'primary'` for the formalized routing key. (required)

     * taskId: Always takes the value `_`

     * runId: Always takes the value `_`

     * workerGroup: Always takes the value `_`

     * workerId: Always takes the value `_`

     * provisionerId: Always takes the value `_`

     * workerType: Always takes the value `_`

     * schedulerId: Identifier for the task-graphs scheduler managing the task-graph this message concerns. Usually `task-graph-scheduler` in production. (required)

     * taskGraphId: Identifier for the task-graph this message concerns (required)

     * reserved: Space reserved for future routing-key entries, you should always match this entry with `#`. As automatically done by our tooling, if not specified.
    """

    def taskGraphFinished(self, *args, **kwargs):
        return self._makeTopicExchange({'routingKey': [{'constant': 'primary', 'multipleWords': False, 'required': True, 'summary': "Identifier for the routing-key kind. This is always `'primary'` for the formalized routing key.", 'name': 'routingKeyKind'}, {'multipleWords': False, 'required': False, 'summary': 'Always takes the value `_`', 'name': 'taskId'}, {'multipleWords': False, 'required': False, 'summary': 'Always takes the value `_`', 'name': 'runId'}, {'multipleWords': False, 'required': False, 'summary': 'Always takes the value `_`', 'name': 'workerGroup'}, {'multipleWords': False, 'required': False, 'summary': 'Always takes the value `_`', 'name': 'workerId'}, {'multipleWords': False, 'required': False, 'summary': 'Always takes the value `_`', 'name': 'provisionerId'}, {'multipleWords': False, 'required': False, 'summary': 'Always takes the value `_`', 'name': 'workerType'}, {'multipleWords': False, 'required': True, 'summary': 'Identifier for the task-graphs scheduler managing the task-graph this message concerns. Usually `task-graph-scheduler` in production.', 'name': 'schedulerId'}, {'multipleWords': False, 'required': True, 'summary': 'Identifier for the task-graph this message concerns', 'name': 'taskGraphId'}, {'multipleWords': True, 'required': False, 'summary': 'Space reserved for future routing-key entries, you should always match this entry with `#`. As automatically done by our tooling, if not specified.', 'name': 'reserved'}], 'name': 'taskGraphFinished', 'exchange': 'task-graph-finished', 'schema': 'http://schemas.taskcluster.net/scheduler/v1/task-graph-finished-message.json#'}, *args, **kwargs)

    funcinfo = {
    }


__all__ = ['createTemporaryCredentials', 'config', '_defaultConfig', 'createApiClient', 'createSession', 'SchedulerEvents']
