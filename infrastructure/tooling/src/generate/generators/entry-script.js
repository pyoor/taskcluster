const path = require('path');
const {quote} = require('shell-quote');
const {listServices, readRepoYAML, writeRepoFile} = require('../../utils');
const packageJson = require('../../../../../package.json');

const SERVICES = listServices();

exports.tasks = [];

exports.tasks.push({
  title: 'Build Entrypoint Script',
  requires: [
  ],
  provides: [
    'entrypoint-script',
  ],
  locks: [],
  run: async (requirements, utils) => {
    const procs = {};

    for (const name of SERVICES) {
      const processes = await readRepoYAML(path.join('services', name, 'procs.yml'));
      Object.entries(processes).forEach(([proc, {command}]) => {
        procs[`${name}/${proc}`] = `cd services/${name} && ${command}`;
      });
    }

    // Export all yarn scripts to be callable via a container
    for (const script of Object.keys(packageJson.scripts)) {
      procs[`script/${script}`] = `yarn run ${script}`;
    }

    // this script:
    //  - reads the references from generated/ and creates rootUrl-relative output
    //  - starts nginx to serve that rootUrl-relative output
    procs['references/web'] = 'exec sh infrastructure/references/references.sh';

    // the ui/web process sets up static/env.js to relay configuration values to
    // the frontend, then runs nginx.
    procs['ui/web'] = 'node /app/ui/generate-env-js.js /app/ui/build/static/env.js && ' +
      'nginx -c /app/ui/web-ui-nginx-site.conf -g \'daemon off;\'';

    const entrypointScript = []
      .concat([
        '#! /bin/sh', // note that alpine does not have bash
        '',
        '# DO NOT EDIT. This is an autogenerated file.',
        '',
        'case "${1}" in',
      ])
      .concat(Object.entries(procs).map(([process, command]) =>
        `${process}) exec ${quote(['sh', '-c', command])};;`))
      .concat([
        // catch-all to run whatever command the user specified
        '*) exec "${@}";;',
        'esac',
      ]).join('\n');

    await writeRepoFile('entrypoint', entrypointScript);

    return {'entrypoint-script': entrypointScript};
  },
});