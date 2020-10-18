FROM yuhichyoc/openjdk

RUN mkdir /opt/alfresco \
    && mkdir /opt/alfresco/repo

COPY ./[tomcat].zip /opt/alfresco/
RUN unzip /opt/alfresco/[tomcat].zip -d /opt/alfresco/ \
    && rm /opt/alfresco/[tomcat].zip

COPY ./[alfresco].zip /opt/alfresco/
RUN unzip /opt/alfresco/[alfresco].zip -d /opt/alfresco/ \
    && mkdir -p /opt/alfresco/[tomcat]/shared/classes \
    && mkdir -p /opt/alfresco/[tomcat]/shared/lib \
    && mkdir /opt/alfresco/[tomcat]/amps \
    && mkdir /opt/alfresco/[tomcat]/amps_share \
    && rm -r /opt/alfresco/[tomcat]/webapps/* \
    && mv /opt/alfresco/[alfresco]/web-server/shared/classes/alfresco-global.properties.sample /opt/alfresco/[tomcat]/shared/classes/alfresco-global.properties \
    && mv /opt/alfresco/[alfresco]/web-server/webapps/* /opt/alfresco/[tomcat]/webapps/ \
    && mv /opt/alfresco/[alfresco]/web-server/conf/Catalina/localhost/* /opt/alfresco/[tomcat]/conf/ \
    && mv /opt/alfresco/[alfresco]/web-server/lib/* /opt/alfresco/[tomcat]/lib/ \
    && mv /opt/alfresco/[alfresco]/amps/alfresco-share-services.amp /opt/alfresco/[tomcat]/amps/ \
    && mv /opt/alfresco/[alfresco]/bin/apply_amps.sh /opt/alfresco/[tomcat]/bin/ \
    && mv /opt/alfresco/[alfresco]/bin/clean_tomcat.sh /opt/alfresco/[tomcat]/bin/ \
    && mv /opt/alfresco/[alfresco]/bin/alfresco-mmt.jar /opt/alfresco/[tomcat]/bin/ \
    && rm -r /opt/alfresco/[alfresco] \
    && rm /opt/alfresco/[alfresco].zip

RUN chmod 754 /opt/alfresco/[tomcat]/bin/catalina.sh \
    && chmod 754 /opt/alfresco/[tomcat]/bin/startup.sh \
    && chmod 754 /opt/alfresco/[tomcat]/bin/shutdown.sh

COPY ./Deployer.py /opt/alfresco/
RUN python3 /opt/alfresco/Deployer.py \
    && rm /opt/alfresco/Deployer.py

RUN chmod 754 /opt/alfresco/[tomcat]/bin/apply_amps.sh \
    && chmod 754 /opt/alfresco/[tomcat]/bin/clean_tomcat.sh

COPY ./ApplyAmpsShRunner.py /opt/alfresco/
RUN python3 /opt/alfresco/ApplyAmpsShRunner.py \
    && rm /opt/alfresco/ApplyAmpsShRunner.py
