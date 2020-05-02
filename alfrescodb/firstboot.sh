#!/bin/bash
docker run --name alfrescodb \
    -p changeme_alfrescodb_port:5432 \
    -d -i -t \
    changeme_ownername/alfrescodb