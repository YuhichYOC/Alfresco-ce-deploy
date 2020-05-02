#!/bin/bash
cd ~/alfresco-search
TEST_VALUE=$(./alfresco-search.running.test.sh)
echo $TEST_VALUE | grep "0$"
if [ $? -eq 0 ]; then
    echo "container alfresco-search going to stop"
    docker stop alfresco-search
else
    echo "container alfresco-search is not able to be stopped"
fi