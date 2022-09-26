#!/usr/bin/env bash

generate=$1

if [ -z ${generate} ] || [ ${generate} == "python" ]; then

    echo "generating neurovault python SDK..."
    docker run --rm  --user $(id -u):$(id -g) \
        -v $PWD:/local openapitools/openapi-generator-cli:v5.4.0 generate \
        -i /local/NeuroVault/openapi/openapi-schema.yml \
        -g python \
        -o /local/python/neurovault-python-sdk
        # -c /local/neurostore_python_sdk_config.json \
fi
