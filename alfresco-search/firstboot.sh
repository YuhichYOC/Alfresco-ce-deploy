#!/bin/bash
docker run --name alfresco-search \
    -p 8983:8983 \
    -d -i -t \
    changeme_ownername/alfresco-search