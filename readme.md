# How to deploy Alfresco community edition 6.1.2 distribution zip on your machine

# Alfresco can't startup without these things
## You have to set up these components
1. Alfresco
1. Solr ( Alfresco-search )
1. Database
1. ActiveMQ

## You have to modify these settings for your environment
### 1. For guide Alfresco accesses to other component
1. IP address, the machine Solr is running.
1. Port number, Solr is listening.
1. IP address, the machine ActiveMQ is running.
1. Port number, ActiveMQ is listening.
1. JDBC driver, what RDBMS you use.
1. IP address, the database instance is running.
1. Port number, the database instance is listening.
1. The name of database instance.
1. The name of database user.
1. Password for access to database.
### 2. For guide Solr accesses to other component
1. IP address, the machine Solr is running.
1. Port number, Solr is listening.
1. IP address, the machine Alfresco is running.
1. Port number, Alfresco is listening.
### 3. For guide Alfresco uses storage
1. Data directory root to store any documents.

## In Dockerfile
### Alfresco
- https://github.com/YuhichYOC/Alfresco-ce-deploy/blob/master/alfresco/Dockerfile
- After build image & run new container, you have to run apply_amps.sh manually.
### Solr
- https://github.com/YuhichYOC/Alfresco-ce-deploy/blob/master/alfresco-search/Dockerfile
### Database ( Postgresql )
- https://github.com/YuhichYOC/Alfresco-ce-deploy/blob/master/alfrescodb/Dockerfile
### ActiveMQ
- https://github.com/YuhichYOC/Alfresco-ce-deploy/blob/master/activemq/Dockerfile

## Show with picture
![](https://raw.githubusercontent.com/YuhichYOC/Alfresco-ce-deploy/master/img/img1.png, "Installation image")

## Alfresco
1. Make directory alfresco into /opt
1. Make directory repo into /opt/alfresco
1. Install tomcat into /opt/alfresco/apache-tomcat-9.0.34
1. Download alfresco-content-services-community-distribution-6.1.2-ga.zip, unzip into /opt/alfresco
1. Make directory classes into /opt/alfresco/apache-tomcat-9.0.34/shared
1. Make directory lib into /opt/alfresco/apache-tomcat-9.0.34/shared
1. Make directory amps into /opt/alfresco/apache-tomcat-9.0.34
1. Make directory amps_share into /opt/alfresco/apache-tomcat-9.0.34
1. Delete all files/directories in /opt/alfresco/apache-tomcat-9.0.34/webapps ( Webapps installed in original tomcat archive )
1. Move war file in /opt/alfresco/alfresco-content-services-community-distribution-6.1.2-ga/web-server/webapps to /opt/alfresco/apache-tomcat-9.0.34/webapps
1. Move all files in /opt/alfresco/alfresco-content-services-community-distribution-6.1.2-ga/web-server/conf/Catalina/localhost to /opt/alfresco/apache-tomcat-9.0.34/conf
1. Put JDBC driver jar into /opt/alfresco/apache-tomcat-9.0.34/lib
1. Move /opt/alfresco/alfresco-content-services-community-distribution-6.1.2-ga/amps/alfresco-share-services.amp to /opt/alfresco/apache-tomcat-9.0.34/amps
1. Move /opt/alfresco/alfresco-content-services-community-distribution-6.1.2-ga/bin/alfresco-mmt.jar to /opt/alfresco/apache-tomcat-9.0.34/bin
1. Move /opt/alfresco/alfresco-content-services-community-distribution-6.1.2-ga/shared/classes/alfresco-global.properties.sample to /opt/alfresco/apache-tomcat-9.0.34/shared/classes/alfresco-global.properties
1. Move /opt/alfresco/alfresco-content-services-community-distribution-6.1.2-ga/bin/apply_amps.sh to /opt/alfresco/apache-tomcat-9.0.34/bin
1. Move /opt/alfresco/alfresco-content-services-community-distribution-6.1.2-ga/bin/clean_tomcat.sh to /opt/alfresco/apache-tomcat-9.0.34/bin
1. Delete directory /opt/alfresco/alfresco-content-services-community-distribution-6.1.2-ga
1. Delete /opt/alfresco/alfresco-content-services-community-distribution-6.1.2-ga.zip
1. Modify /opt/alfresco/apache-tomcat-9.0.34/shared/classes/alfresco-global.properties as below
    ```INI
    #
    # Sample custom content and index data location
    #
    #dir.root=/srv/alfresco/alf_data
    ↓
    #
    # Sample custom content and index data location
    #
    dir.root=/opt/alfresco/repo
    
    #
    # Sample database connection properties
    #
    #db.username=alfresco
    #db.password=alfresco
    ↓
    #
    # Sample database connection properties
    #
    db.username=alfresco
    db.password=alfresco
    
    #
    # PostgreSQL connection (requires postgresql-8.2-504.jdbc3.jar or equivalent)
    #
    #db.driver=org.postgresql.Driver
    #db.url=jdbc:postgresql://localhost:5432/alfresco
    ↓
    #
    # PostgreSQL connection (requires postgresql-8.2-504.jdbc3.jar or equivalent)
    #
    db.driver=org.postgresql.Driver
    db.url=jdbc:postgresql://192.168.1.3:5432/alfrescodb
    ```
1. Add description into /opt/alfresco/apache-tomcat-9.0.34/shared/classes/alfresco-global.properties as below
    ```INI
    index.subsystem.name=solr6
    solr.secureComms=none
    solr.host=192.168.1.2
    solr.port=8983
    
    messaging.broker.url=failover:(tcp://192.168.1.4:61616)?timeout=3000
    ```
1. Modify /opt/alfresco/apache-tomcat-9.0.34/conf/catalina.properties as below
    ```INI
    shared.loader=
    ↓
    shared.loader=${catalina.base}/shared/classes,${catalina.base}/shared/lib/*.jar
    ```
1. Modify /opt/alfresco/apache-tomcat-9.0.34/conf/server.xml as below
    ```XML
    <Connector port="8080" protocol="HTTP/1.1"
               connectionTimeout="20000"
               redirectPort="8443" />
    ↓
    <Connector
        port="8080"
        protocol="HTTP/1.1"
        URIEncoding="UTF-8"
        connectionTimeout="20000"
        maxHttpHeaderSize="32768"
        redirectPort="8443"
        />
    ```
1. Modify /opt/alfresco/apache-tomcat-9.0.34/bin/apply_amps.sh as below
    ```BASH
    export ALF_HOME=${SCRIPTPATH%/*}
    ↓
    export ALF_HOME=/opt/alfresco/apache-tomcat-9.0.34
    ```
1. Run /opt/alfresco/apache-tomcat-9.0.34/bin/apply_amps.sh

## Solr
1. Make directory alfresco into /opt
1. Download alfresco-search-services-1.3.0.1.zip, unzip into /opt/alfresco
1. Delete /opt/alfresco/alfresco-search-services-1.3.0.1.zip
1. Modify /opt/alfresco/alfresco-search-services/solrhome/conf/shared.properties as below
    ```INI
    #Host details an external client would use to connect to Solr
    solr.host=localhost
    ↓
    #Host details an external client would use to connect to Solr
    solr.host=192.168.1.1
    ```
1. Add description into /opt/alfresco/alfresco-search-services/solr.in.sh as below
    ```BASH
    SOLR_SOLR_HOST=192.168.1.2
    SOLR_ALFRESCO_HOST=192.168.1.1
    ```
1. Modify /opt/alfresco/alfresco-search-services/solr.in.sh as below
    ```BASH
    # Sets the port Solr binds to, default is 8983
    #SOLR_PORT=8983
    ↓
    # Sets the port Solr binds to, default is 8983
    SOLR_PORT=8983
    ```
1. Modify /opt/alfresco/alfresco-search-services/solrhome/templates/rerank/conf/solrcore.properties as below
    ```INI
    #
    # Properties loaded during alfresco tracking
    #
    
    alfresco.host=localhost
    alfresco.port=8080
    ↓
    #
    # Properties loaded during alfresco tracking
    #
    
    alfresco.host=192.168.1.1
    alfresco.port=8080
    ```

## Database ( Postgresql )
1. Install Postgresql, make database as Name=alfrescodb, user=alfresco, password=alfresco

## ActiveMQ
1. Make directory activemq into /opt
1. Download apache-activemq-5.15.12-bin.tar.gz, unzip into /opt/activemq
1. Delete /opt/activemq/apache-activemq-5.15.12-bin.tar.gz

# You shoud do this ( but I can't understand the document. )
## It's nice for more secure application
- You may want to encrypt communication between Alfresco ⇔ Solr.
- Read this. https://docs.alfresco.com/search-community/concepts/generate-keys-overview.html

# As you like
- Install any plugins you want. ( e.g. alfresco-pdf-renderer )
