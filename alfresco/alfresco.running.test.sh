#!/bin/bash
TEST_VALUE=$(docker exec alfresco ps -ef)
echo $TEST_VALUE | grep 'Dcatalina.base'
if [ $? -eq 0 ]; then
    echo "1"
else
    echo "0"
fi