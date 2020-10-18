FROM yuhichyoc/openjdk

RUN mkdir /opt/activemq

COPY ./[activemq]-bin.tar.gz /opt/activemq/
RUN tar xzf /opt/activemq/[activemq]-bin.tar.gz -C /opt/activemq/ \
    && rm /opt/activemq/[activemq]-bin.tar.gz

RUN chmod 744 /opt/activemq/[activemq]/bin/activemq \
    && ln -s /opt/activemq/[activemq]/bin/activemq /opt/activemq
