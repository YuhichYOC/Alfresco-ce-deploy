#!/bin/bash
if [ -d ~/alfrescodb ]; then
    ~/alfrescodb/alfrescodb.docker.start.sh
fi
if [ -d ~/activemq ]; then
    ~/activemq/activemq.docker.start.sh
    ~/activemq/activemq.start.sh
fi
if [ -d ~/alfresco-search ]; then
    ~/alfresco-search/alfresco-search.docker.start.sh
    ~/alfresco-search/alfresco-search.start.sh
fi
if [ -d ~/alfresco ]; then
    ~/alfresco/alfresco.docker.start.sh
    ~/alfresco/alfresco.start.sh
fi