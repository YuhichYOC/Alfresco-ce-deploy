#!/bin/bash

ALFRESCO_STOP() {
  docker exec alfresco /opt/alfresco/[tomcat]/bin/shutdown.sh
  TEST_VALUE=$(/home/ubuntu/alfresco/run.test.sh)
  echo $TEST_VALUE | grep "0$"
  if [ $? -eq 0 ]; then
    echo "container alfresco going to stop"
    docker stop alfresco
  else
    echo "container alfresco is not able to be stopped"
  fi
}

ALFRESCO_SEARCH_STOP() {
  docker exec alfresco-search /opt/alfresco/alfresco-search-services/solr/bin/solr stop
  TEST_VALUE=$(/home/ubuntu/alfresco-search/run.test.sh)
  echo $TEST_VALUE | grep "0$"
  if [ $? -eq 0 ]; then
    echo "container alfresco-search going to stop"
    docker stop alfresco-search
  else
    echo "container alfresco-search is not able to be stopped"
  fi
}

ARTEMIS_STOP() {
  docker exec artemis /opt/artemis/bin/artemis-service stop
  TEST_VALUE=$(/home/ubuntu/artemis/run.test.sh)
  echo $TEST_VALUE | grep "0$"
  if [ $? -eq 0 ]; then
    echo "container artemis going to stop"
    docker stop artemis
  else
    echo "container artemis is not able to be stopped"
  fi
}

ACTIVEMQ_STOP() {
  docker exec activemq /opt/activemq/activemq stop
  TEST_VALUE=$(/home/ubuntu/activemq/run.test.sh)
  echo $TEST_VALUE | grep "0$"
  if [ $? -eq 0 ]; then
    echo "container activemq going to stop"
    docker stop activemq
  else
    echo "container activemq is not able to be stopped"
  fi
}

ALFRESCODB_STOP() {
  docker stop alfrescodb
}

if [ -d /home/ubuntu/alfresco ]; then
  ALFRESCO_STOP
fi
if [ -d /home/ubuntu/alfresco-search ]; then
  ALFRESCO_SEARCH_STOP
fi
if [ -d /home/ubuntu/artemis ]; then
  ARTEMIS_STOP
fi
if [ -d /home/ubuntu/activemq ]; then
  ACTIVEMQ_STOP
fi
if [ -d /home/ubuntu/alfrescodb ]; then
  ALFRESCODB_STOP
fi
