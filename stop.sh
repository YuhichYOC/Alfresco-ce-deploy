#!/bin/bash
if [ -d ~/alfresco ]; then
    ~/alfresco/alfresco.stop.sh
    ~/alfresco/alfresco.docker.stop.sh
fi
if [ -d ~/alfresco-search ]; then
    ~/alfresco-search/alfresco-search.stop.sh
    ~/alfresco-search/alfresco-search.docker.stop.sh
fi
if [ -d ~/activemq ]; then
    ~/activemq/activemq.stop.sh
    ~/activemq/activemq.docker.stop.sh
fi
if [ -d ~/alfrescodb ]; then
    ~/alfrescodb/alfrescodb.docker.stop.sh
fi