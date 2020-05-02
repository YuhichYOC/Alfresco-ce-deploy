#!/bin/bash
cd changeme_workdirectory_fullpath/alfresco
TEST_VALUE=$(./alfresco.running.test.sh)
echo $TEST_VALUE | grep "0$"
if [ $? -eq 0 ]; then
    echo "container alfresco going to stop"
    docker stop alfresco
else
    echo "container alfresco is not able to be stopped"
fi