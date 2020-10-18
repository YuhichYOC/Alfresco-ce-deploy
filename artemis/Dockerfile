FROM yuhichyoc/openjdk

RUN mkdir /opt/artemis

COPY ./[artemis]-bin.tar.gz /opt/artemis/
RUN tar xzf /opt/artemis/[artemis]-bin.tar.gz -C /opt/artemis/ \
    && rm /opt/artemis/[artemis]-bin.tar.gz

RUN chmod 744 /opt/artemis/[artemis]/bin/artemis

RUN /opt/artemis/[artemis]/bin/artemis  create \
    --user [artemis_user] --password [artemis_password] \
    --role [artemis_role] --allow-anonymous [artemis_allow_anonymous] \
    /opt/artemis
