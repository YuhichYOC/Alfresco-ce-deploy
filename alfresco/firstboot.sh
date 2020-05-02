#!/bin/bash
docker run --name alfresco \
    -p 8080:8080 \
    -d -i -t \
    changeme_ownername/alfresco