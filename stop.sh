#!/bin/bash
if [ -d changeme_workdirectory_fullpath/alfresco ]; then
    changeme_workdirectory_fullpath/alfresco/alfresco.stop.sh
    changeme_workdirectory_fullpath/alfresco/alfresco.docker.stop.sh
fi
if [ -d changeme_workdirectory_fullpath/alfresco-search ]; then
    changeme_workdirectory_fullpath/alfresco-search/alfresco-search.stop.sh
    changeme_workdirectory_fullpath/alfresco-search/alfresco-search.docker.stop.sh
fi
if [ -d changeme_workdirectory_fullpath/activemq ]; then
    changeme_workdirectory_fullpath/activemq/activemq.stop.sh
    changeme_workdirectory_fullpath/activemq/activemq.docker.stop.sh
fi
if [ -d changeme_workdirectory_fullpath/alfrescodb ]; then
    changeme_workdirectory_fullpath/alfrescodb/alfrescodb.docker.stop.sh
fi