#!/bin/sh
# ---------------------------------
# Script to clean Tomcat temp files
# ---------------------------------
echo "Cleaning temporary Alfresco files from Tomcat..."
rm -rf /opt/alfresco/apache-tomcat-9.0.34/temp/Alfresco tomcat/work/Catalina/localhost/alfresco
rm -rf /opt/alfresco/apache-tomcat-9.0.34/work/Catalina/localhost/share
rm -rf /opt/alfresco/apache-tomcat-9.0.34/work/Catalina/localhost/awe
rm -rf /opt/alfresco/apache-tomcat-9.0.34/work/Catalina/localhost/wcmqs