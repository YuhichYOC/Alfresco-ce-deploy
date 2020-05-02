#!/bin/bash
cd changeme_workdirectory_fullpath/activemq
TEST_VALUE=$(./activemq.running.test.sh)
echo $TEST_VALUE | grep "0$"
if [ $? -eq 0 ]; then
    echo "container activemq going to stop"
    docker stop activemq
else
    echo "container activemq is not able to be stopped"
fi