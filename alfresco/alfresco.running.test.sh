#!/bin/bash
curl --head changeme_alfresco_host:8080
if [ $? -eq 0 ]; then
    echo "1"
else
    echo "0"
fi