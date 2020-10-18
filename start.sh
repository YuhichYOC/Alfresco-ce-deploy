#!/bin/bash

ALFRESCODB_START() {
  docker start alfrescodb
}

ACTIVEMQ_START() {
  docker start activemq
  docker exec activemq /opt/activemq/activemq start
}

ARTEMIS_START() {
  docker start artemis
  docker exec artemis /opt/artemis/bin/artemis-service start
}

ALFRESCO_SEARCH_START() {
  docker start alfresco-search
  docker exec alfresco-search /opt/alfresco/alfresco-search-services/solr/bin/solr start -force -a "-Dcreate.alfresco.defaults=alfresco,archive"
}

ALFRESCO_START() {
  docker start alfresco
  docker exec alfresco /opt/alfresco/[tomcat]/bin/startup.sh
}

if [ -d /home/ubuntu/alfrescodb ]; then
  ALFRESCODB_START
fi
if [ -d /home/ubuntu/activemq ]; then
  ACTIVEMQ_START
fi
if [ -d /home/ubuntu/artemis ]; then
  ARTEMIS_START
fi
if [ -d /home/ubuntu/alfresco-search ]; then
  ALFRESCO_SEARCH_START
fi
if [ -d /home/ubuntu/alfresco ]; then
  ALFRESCO_START
fi
