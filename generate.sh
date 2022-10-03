#!/usr/bin/env bash

generate=$1

if [ -z ${generate} ] || [ ${generate} == "python" || ${generate} == "neurovault-python-sdk" ]; then

    echo "generating neurovault python SDK..."
    docker run --rm --env JAVA_OPTS="${JAVA_OPTS} -Dlog.level=debug" --user $(id -u):$(id -g) \
        -v $PWD:/local openapitools/openapi-generator-cli:v6.2.0 generate \
        -i /local/NeuroVault/openapi/openapi-schema.yml \
        -g python \
        -o /local/python/neurovault-python-sdk \
        -c /local/neurovault_python_sdk_config.json #\
        # --global-property debugModels
fi
