#!/bin/bash
TEST_VALUE=$(docker exec artemis /opt/artemis/bin/artemis-service status)
echo $TEST_VALUE | grep 'artemis-service is stopped'
if [ $? -eq 0 ]; then
  echo "0"
else
  echo "1"
fi
