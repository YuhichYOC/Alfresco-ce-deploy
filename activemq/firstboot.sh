#!/bin/bash
docker run --name activemq \
    -p 5672:5672 \
    -p 8161:8161 \
    -p 61613:61613 \
    -p 61616:61616 \
    -d -i -t \
    changeme_ownername/activemq