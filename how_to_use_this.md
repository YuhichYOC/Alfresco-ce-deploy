# How to use build.py

## Following example based on this situation  

1. Run alfresco on the server that has IP 192.168.1.219, listening port is 8080.  
1. Run alfresco-search on the server that has IP 192.168.1.81, listening port is 8983.  
1. Run ActiveMQ Artemis on the server that has IP 192.168.1.81, listening port is 61616.  
1. Run Postgresql on the server that has IP 192.168.1.81, listening port is 5432.  
1. User on 192.168.1.219 is "ubuntu".  
1. User on 192.168.1.81 is "ubuntu".  

## 1. Download packages  

1. alfresco content services community distribution zip  
    from here : https://www.alfresco.com/jp/thank-you/thank-you-downloading-alfresco-community-edition  
    click "Distribution.zip"  
1. alfresco search services zip  
    from here : https://www.alfresco.com/jp/thank-you/thank-you-downloading-alfresco-community-edition  
    click "Alfresco Search Services 1.4.zip"  
1. ActiveMQ or Apache ActiveMQ Artemis archive ( tar.gz )  
    from here : https://activemq.apache.org/  
1. Tomcat  
    from here : https://tomcat.apache.org/download-90.cgi  
    click "zip"  

## 2. Transfer packages  

1. alfresco content services community distribution zip  
    Transfer alfresco-content-services-community-distribution-6.2.0-ga.zip to server you are going to run alfresco.  
1. alfresco search services zip  
    Transfer alfresco-search-services-1.4.0.zip to server you are going to run alfresco-search.  
1. ActiveMQ or Apache ActiveMQ Artemis archive  
    Transfer apache-activemq-5.16.0-bin.tar.gz or apache-artemis-2.15.0-bin.tar.gz to server you are going to run ActiveMQ.  
1. Tomcat archive  
    Transfer apache-tomcat-9.0.39.zip to server you are going to run alfresco.  

## 3. Prepare build.py  

- Rewrite setting in build.py  

```
DB_HOST = '[db_host]'
DB_PORT = '[db_port]'
DB_USERNAME = '[db_username]'
DB_PASSWORD = '[db_password]'

ACTIVEMQ_VERSION = '[activemq_version]'
ACTIVEMQ_HOST = '[activemq_host]'
ACTIVEMQ_PORT = '[activemq_port]'

ARTEMIS_VERSION = '[artemis_version]'
ARTEMIS_USER = '[artemis_user]'
ARTEMIS_PASSWORD = '[artemis_password]'
ARTEMIS_ROLE = '[artemis_role]'
ARTEMIS_ALLOW_ANONYMOUS = '[artemis_allow_anonymous]'  # true or false

ALFRESCO_SEARCH = '[alfresco_search]'
SOLR_HOST = '[solr_host]'
SOLR_PORT = '[solr_port]'

TOMCAT_VERSION = '[tomcat_version]'

ALFRESCO_VERSION = '[alfresco_version]'
ALFRESCO_HOST = '[alfresco_host]'
PATH_TO_REPOSITORY_DIRECTORY = '[path_to_repository_directory]'
APPLY_AMPS_SH = '[apply_amps_sh_filename]'
```
↓ like this ↓  
```
DB_HOST = '192.168.1.81'
DB_PORT = '5432'
DB_USERNAME = 'alfresco'
DB_PASSWORD = 'alfresco'

ACTIVEMQ_VERSION = ''
ACTIVEMQ_HOST = '192.168.1.81'
ACTIVEMQ_PORT = '61616'

ARTEMIS_VERSION = 'apache-artemis-2.15.0'
ARTEMIS_USER = 'admin'
ARTEMIS_PASSWORD = 'admin'
ARTEMIS_ROLE = 'admins'
ARTEMIS_ALLOW_ANONYMOUS = 'true'  # true or false

ALFRESCO_SEARCH = 'alfresco-search-services-1.4.0'
SOLR_HOST = '192.168.1.81'
SOLR_PORT = '8983'

TOMCAT_VERSION = 'apache-tomcat-9.0.39'

ALFRESCO_VERSION = 'alfresco-content-services-community-distribution-6.2.0-ga'
ALFRESCO_HOST = '192.168.1.219'
PATH_TO_REPOSITORY_DIRECTORY = '/opt/alfresco/repo'
APPLY_AMPS_SH = 'apply_amps.sh'
```

## 4. Transfer scripts to each servers  

1. Transfer build.py, firstboot.sh, start.sh, stop.sh to 192.168.1.219 and 192.168.1.81.  
1. Transfer openjdk, alfresco to 192.168.1.219. ( whole directory )  
1. Transfer openjdk, alfresco-search, alfrescodb, artemis to 192.168.1.81 ( whole directory )  
```
192.168.1.219
/home
└/ubuntu
　└/alfresco
　│└ApplyAmpsShRunner.py
　│└build.sh
　│└Deployer.py
　│└Dockerfile
　│└run.test.sh
　└/openjdk
　│└build.sh
　│└Dockerfile
　└build.py
　└firstboot.sh
　└start.sh
　└stop.sh
　└alfresco-content-services-community-distribution-6.2.0-ga.zip
　└apache-tomcat-9.0.39.zip

192.168.1.81
/home
└/ubuntu
　└/alfresco-search
　│└build.sh
　│└Deployer.py
　│└Dockerfile
　│└run.test.sh
　└/alfrescodb
　│└build.sh
　│└Dockerfile
　└/artemis
　│└build.sh
　│└Dockerfile
　│└run.test.sh
　└/openjdk
　│└build.sh
　│└Dockerfile
　└build.py
　└firstboot.sh
　└start.sh
　└stop.sh
　└alfresco-search-services-1.4.0.zip
　└apache-artemis-2.15.0-bin.tar.gz
```

## 5. Move packages into build directories  

1. Move alfresco content services community distribution zip into alfresco.  
1. Move alfresco search services zip into alfresco-search.  
1. Move Apache ActiveMQ Artemis archive into artemis.  
1. Move tomcat archive into alfresco.  
```
192.168.1.219
/home
└/ubuntu
　└/alfresco
　│└ApplyAmpsShRunner.py
　│└build.sh
　│└Deployer.py
　│└Dockerfile
　│└run.test.sh
　│└alfresco-content-services-community-distribution-6.2.0-ga.zip
　│└apache-tomcat-9.0.39.zip
　└/openjdk
　│└build.sh
　│└Dockerfile
　└build.py
　└firstboot.sh
　└start.sh
　└stop.sh

192.168.1.81
/home
└/ubuntu
　└/alfresco-search
　│└build.sh
　│└Deployer.py
　│└Dockerfile
　│└run.test.sh
　│└alfresco-search-services-1.4.0.zip
　└/alfrescodb
　│└build.sh
　│└Dockerfile
　└/artemis
　│└build.sh
　│└Dockerfile
　│└run.test.sh
　│└apache-artemis-2.15.0-bin.tar.gz
　└/openjdk
　│└build.sh
　│└Dockerfile
　└build.py
　└firstboot.sh
　└start.sh
　└stop.sh
```

## 6. Run build.py  

```
python3 build.py
```

## 7. Assign ports and name to each containers  

- Run "firstboot.sh" on 192.168.1.81 and 192.168.1.219.  
```
192.168.1.81
ubuntu@192.168.1.81:~$ ./firstboot.sh

192.168.1.219
ubuntu@192.168.1.219:~$ ./firstboot.sh
```

## To start alfresco / To stop alfresco  

- Run "start.sh" / "stop.sh" in each server.  
