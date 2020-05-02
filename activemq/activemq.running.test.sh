#!/bin/bash
TEST_VALUE=$(docker exec activemq /opt/activemq/activemq status)
echo $TEST_VALUE | grep 'ActiveMQ not running'
if [ $? -eq 0 ]; then
    echo "0"
else
    echo "1"
fi