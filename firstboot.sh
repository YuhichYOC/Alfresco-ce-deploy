#!/bin/bash

# use this for allocating names and ports to each containers.

FIRSTRUN_ALFRESCODB() {
  docker run --name alfrescodb -p 5432:5432 -d -i -t yuhichyoc/alfrescodb
}

FIRSTRUN_ACTIVEMQ() {
  docker run --name activemq -p 5672:5672 -p 8161:8161 -p 61613:61613 -p 61616:61616 -d -i -t yuhichyoc/activemq
}

FIRSTRUN_ARTEMIS() {
  docker run --name artemis -p 5672:5672 -p 8161:8161 -p 61613:61613 -p 61616:61616 -d -i -t yuhichyoc/artemis
}

FIRSTRUN_ALFRESCO_SEARCH() {
  docker run --name alfresco-search -p 8983:8983 -d -i -t yuhichyoc/alfresco-search
}

FIRSTRUN_ALFRESCO() {
  docker run --name alfresco -p 8080:8080 -d -i -t yuhichyoc/alfresco
}

if [ -d /home/ubuntu/alfrescodb ]; then
  FIRSTRUN_ALFRESCODB
fi
if [ -d /home/ubuntu/activemq ]; then
  FIRSTRUN_ACTIVEMQ
fi
if [ -d /home/ubuntu/artemis ]; then
  FIRSTRUN_ARTEMIS
fi
if [ -d /home/ubuntu/alfresco-search ]; then
  FIRSTRUN_ALFRESCO_SEARCH
fi
if [ -d /home/ubuntu/alfresco ]; then
  FIRSTRUN_ALFRESCO
fi
