// THIS IS AN AUTOGENERATED FILE. DO NOT EDIT THIS FILE DIRECTLY.

import Client from '../Client';

export default class WorkerManager extends Client {
  constructor(options = {}) {
    super({
      serviceName: 'worker-manager',
      serviceVersion: 'v1',
      exchangePrefix: '',
      ...options,
    });
    this.ping.entry = {"args":[],"method":"get","name":"ping","query":[],"route":"/ping","stability":"stable","type":"function"}; // eslint-disable-line
    this.createWorkerType.entry = {"args":["name"],"input":true,"method":"put","name":"createWorkerType","output":true,"query":[],"route":"/workertype/<name>","scopes":{"AllOf":["worker-manager:create-worker-type:<name>","worker-manager:provider:<provider>"]},"stability":"experimental","type":"function"}; // eslint-disable-line
    this.updateWorkerType.entry = {"args":["name"],"input":true,"method":"post","name":"updateWorkerType","output":true,"query":[],"route":"/workertype/<name>","scopes":{"AllOf":["worker-manager:update-worker-type:<name>","worker-manager:provider:<provider>"]},"stability":"experimental","type":"function"}; // eslint-disable-line
    this.workerType.entry = {"args":["name"],"method":"get","name":"workerType","output":true,"query":[],"route":"/workertype/<name>","stability":"experimental","type":"function"}; // eslint-disable-line
    this.deleteWorkerType.entry = {"args":["name"],"method":"delete","name":"deleteWorkerType","query":[],"route":"/workertype/<name>","scopes":"worker-manager:delete-worker-type:<name>","stability":"experimental","type":"function"}; // eslint-disable-line
    this.listWorkerTypes.entry = {"args":[],"method":"get","name":"listWorkerTypes","output":true,"query":["continuationToken","limit"],"route":"/workertypes","stability":"experimental","type":"function"}; // eslint-disable-line
  }
  /* eslint-disable max-len */
  // Respond without doing anything.
  // This endpoint is used to check that the service is up.
  /* eslint-enable max-len */
  ping(...args) {
    this.validate(this.ping.entry, args);

    return this.request(this.ping.entry, args);
  }
  /* eslint-disable max-len */
  // Create a new workertype. If the workertype already exists, this will throw an error.
  /* eslint-enable max-len */
  createWorkerType(...args) {
    this.validate(this.createWorkerType.entry, args);

    return this.request(this.createWorkerType.entry, args);
  }
  /* eslint-disable max-len */
  // Given an existing workertype definition, this will modify it and return the new definition.
  /* eslint-enable max-len */
  updateWorkerType(...args) {
    this.validate(this.updateWorkerType.entry, args);

    return this.request(this.updateWorkerType.entry, args);
  }
  /* eslint-disable max-len */
  // Given an existing workertype defition, this will fetch it.
  /* eslint-enable max-len */
  workerType(...args) {
    this.validate(this.workerType.entry, args);

    return this.request(this.workerType.entry, args);
  }
  /* eslint-disable max-len */
  // Delete an existing workertype definition.
  /* eslint-enable max-len */
  deleteWorkerType(...args) {
    this.validate(this.deleteWorkerType.entry, args);

    return this.request(this.deleteWorkerType.entry, args);
  }
  /* eslint-disable max-len */
  // Get the list of all the existing workertypes
  /* eslint-enable max-len */
  listWorkerTypes(...args) {
    this.validate(this.listWorkerTypes.entry, args);

    return this.request(this.listWorkerTypes.entry, args);
  }
}
