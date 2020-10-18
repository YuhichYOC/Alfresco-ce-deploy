FROM yuhichyoc/openjdk

RUN mkdir /opt/alfresco

COPY ./[alfresco-search].zip /opt/alfresco/
RUN unzip /opt/alfresco/[alfresco-search].zip -d /opt/alfresco/ \
    && rm /opt/alfresco/[alfresco-search].zip

COPY ./Deployer.py /opt/alfresco/
RUN python3 /opt/alfresco/Deployer.py \
    && rm /opt/alfresco/Deployer.py
