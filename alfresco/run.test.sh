#!/bin/bash
curl --head [alfresco_host]:8080
if [ $? -eq 0 ]; then
  echo "1"
else
  echo "0"
fi
