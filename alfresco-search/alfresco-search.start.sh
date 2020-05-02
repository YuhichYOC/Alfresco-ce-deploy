#!/bin/bash
docker exec alfresco-search /opt/alfresco/alfresco-search-services/solr/bin/solr start -force -a "-Dcreate.alfresco.defaults=alfresco,archive"