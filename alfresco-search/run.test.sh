#!/bin/bash
TEST_VALUE=$(docker exec alfresco-search /opt/alfresco/alfresco-search-services/solr/bin/solr status)
echo $TEST_VALUE | grep 'No Solr nodes are running.'
if [ $? -eq 0 ]; then
  echo "0"
else
  echo "1"
fi
