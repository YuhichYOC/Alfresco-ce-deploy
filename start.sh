#!/bin/bash
if [ -d changeme_workdirectory_fullpath/alfrescodb ]; then
    changeme_workdirectory_fullpath/alfrescodb/alfrescodb.docker.start.sh
fi
if [ -d changeme_workdirectory_fullpath/activemq ]; then
    changeme_workdirectory_fullpath/activemq/activemq.docker.start.sh
    changeme_workdirectory_fullpath/activemq/activemq.start.sh
fi
if [ -d changeme_workdirectory_fullpath/alfresco-search ]; then
    changeme_workdirectory_fullpath/alfresco-search/alfresco-search.docker.start.sh
    changeme_workdirectory_fullpath/alfresco-search/alfresco-search.start.sh
fi
if [ -d changeme_workdirectory_fullpath/alfresco ]; then
    changeme_workdirectory_fullpath/alfresco/alfresco.docker.start.sh
    changeme_workdirectory_fullpath/alfresco/alfresco.start.sh
fi