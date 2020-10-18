import re

TOMCAT_VERSION = '[tomcat_version]'

REPOSITORY_DIRECTORY = '[path_to_repository_directory]'

SOLR_HOST = '[solr_host]'
SOLR_PORT = '[solr_port]'

ACTIVEMQ_HOST = '[activemq_host]'
ACTIVEMQ_PORT = '[activemq_port]'

DB_HOST = '[db_host]'
DB_PORT = '[db_port]'
DB_USERNAME = '[db_username]'
DB_PASSWORD = '[db_password]'


class FileEntity:

    def __init__(self):
        self.path = ''
        self.content = []

    def set_path(self, arg):
        self.path = arg

    def get_content(self):
        return self.content

    def set_content(self, arg):
        self.content = arg

    def read(self):
        self.content.clear()
        with open(self.path, 'r') as f:
            lines = f.read().split('\n')
            for line in lines:
                self.content.append(line)

    def write(self):
        with open(self.path, 'w') as f:
            for line in self.content:
                f.write(line)
                f.write('\n')


class GlobalPropertiesEditor:

    def __init__(self):
        self.content = []
        self.tomcat = ''
        self.repository_directory = ''
        self.db_username = ''
        self.db_password = ''
        self.db_host = ''
        self.db_port = ''
        self.solr_host = ''
        self.solr_port = ''
        self.activemq_host = ''
        self.activemq_port = ''

    def set_tomcat(self, arg):
        self.tomcat = arg

    def set_repository_directory(self, arg):
        self.repository_directory = arg

    def set_db_username(self, arg):
        self.db_username = arg

    def set_db_password(self, arg):
        self.db_password = arg

    def set_db_host(self, arg):
        self.db_host = arg

    def set_db_port(self, arg):
        self.db_port = arg

    def set_solr_host(self, arg):
        self.solr_host = arg

    def set_solr_port(self, arg):
        self.solr_port = arg

    def set_activemq_host(self, arg):
        self.activemq_host = arg

    def set_activemq_port(self, arg):
        self.activemq_port = arg

    def run(self):
        fe = FileEntity()
        fe.set_path('/opt/alfresco/' + self.tomcat + '/shared/classes/alfresco-global.properties')
        fe.read()
        self.content = fe.get_content()
        self.content = self.uncomment_repository_setting()
        self.content = self.uncomment_db_setting()
        self.content = self.uncomment_postgres_setting()
        self.content = self.uncomment_alfresco()
        self.content = self.uncomment_share()
        self.content = self.insert_solr_setting()
        self.content = self.insert_activemq_setting()
        fe.set_content(self.content)
        fe.write()

    def uncomment_repository_setting(self):
        new_content = []
        p = re.compile('^#dir\\.root')
        for line in self.content:
            m = p.match(line)
            if m is not None:
                new_content.append('dir.root=' + self.repository_directory)
            else:
                new_content.append(line)
        return new_content

    def uncomment_db_setting(self):
        new_content = []
        p_user = re.compile('^#db\\.username')
        p_pass = re.compile('^#db\\.password')
        for line in self.content:
            m_user = p_user.match(line)
            m_pass = p_pass.match(line)
            if m_user is not None:
                new_content.append('db.username=' + self.db_username)
            elif m_pass is not None:
                new_content.append('db.password=' + self.db_password)
            else:
                new_content.append(line)
        return new_content

    def uncomment_postgres_setting(self):
        new_content = []
        p_start = re.compile('^# *PostgreSQL *connection')
        p_driver = re.compile('^#db\\.driver')
        p_url = re.compile('^#db\\.url')
        start = False
        driver_uncommented = False
        url_uncommented = False
        for line in self.content:
            m_start = p_start.match(line)
            m_driver = p_driver.match(line)
            m_url = p_url.match(line)
            if m_start is not None:
                new_content.append(line)
                start = True
            elif start and (not driver_uncommented) and m_driver is not None:
                new_content.append('db.driver=org.postgresql.Driver')
                driver_uncommented = True
            elif start and (not url_uncommented) and m_url is not None:
                new_content.append('db.url=jdbc:postgresql://' + self.db_host + ':' + self.db_port + '/alfresco')
                url_uncommented = True
            else:
                new_content.append(line)
        return new_content

    def uncomment_alfresco(self):
        new_content = []
        p_context = re.compile('^#alfresco\\.context')
        p_host = re.compile('^#alfresco\\.host')
        p_port = re.compile('^#alfresco\\.port')
        p_protocol = re.compile('^#alfresco\\.protocol')
        for line in self.content:
            m_context = p_context.match(line)
            m_host = p_host.match(line)
            m_port = p_port.match(line)
            m_protocol = p_protocol.match(line)
            if m_context is not None:
                new_content.append('alfresco.context=alfresco')
            elif m_host is not None:
                new_content.append('alfresco.host=${localname}')
            elif m_port is not None:
                new_content.append('alfresco.port=8080')
            elif m_protocol is not None:
                new_content.append('alfresco.protocol=http')
            else:
                new_content.append(line)
        return new_content

    def uncomment_share(self):
        new_content = []
        p_context = re.compile('^#share\\.context')
        p_host = re.compile('^#share\\.host')
        p_port = re.compile('^#share\\.port')
        p_protocol = re.compile('^#share\\.protocol')
        for line in self.content:
            m_context = p_context.match(line)
            m_host = p_host.match(line)
            m_port = p_port.match(line)
            m_protocol = p_protocol.match(line)
            if m_context is not None:
                new_content.append('share.context=share')
            elif m_host is not None:
                new_content.append('share.host=${localname}')
            elif m_port is not None:
                new_content.append('share.port=8080')
            elif m_protocol is not None:
                new_content.append('share.protocol=http')
            else:
                new_content.append(line)
        return new_content

    def insert_solr_setting(self):
        new_content = self.content
        new_content.append('')
        new_content.append('index.subsystem.name=solr6')
        new_content.append('solr.secureComms=none')
        new_content.append('solr.host=' + self.solr_host)
        new_content.append('solr.port=' + self.solr_port)
        return new_content

    def insert_activemq_setting(self):
        new_content = self.content
        new_content.append('')
        new_content.append(
            'messaging.broker.url=failover:(tcp://' + self.activemq_host + ':' + self.activemq_port + ')?timeout=3000')
        return new_content


class ApplyAmpsShEditor:

    def __init__(self):
        self.content = []
        self.tomcat = ''

    def set_tomcat(self, arg):
        self.tomcat = arg

    def run(self):
        fe = FileEntity()
        fe.set_path('/opt/alfresco/' + self.tomcat + '/bin/apply_amps.sh')
        fe.read()
        self.content = fe.get_content()
        self.content = self.edit_alf_home()
        self.content = self.edit_catalina_home()
        fe.set_content(self.content)
        fe.write()

    def edit_alf_home(self):
        new_content = []
        p = re.compile('^ *export +ALF_HOME=')
        for line in self.content:
            m = p.match(line)
            if m is not None:
                new_content.append('export ALF_HOME=/opt/alfresco/' + self.tomcat)
            else:
                new_content.append(line)
        return new_content

    def edit_catalina_home(self):
        new_content = []
        p = re.compile('^ *export +CATALINA_HOME=')
        for line in self.content:
            m = p.match(line)
            if m is not None:
                new_content.append('export CATALINA_HOME=$ALF_HOME')
            else:
                new_content.append(line)
        return new_content


class CatalinaPropertiesEditor:

    def __init__(self):
        self.content = []
        self.tomcat = ''

    def set_tomcat(self, arg):
        self.tomcat = arg

    def run(self):
        fe = FileEntity()
        fe.set_path('/opt/alfresco/' + self.tomcat + '/conf/catalina.properties')
        fe.read()
        self.content = fe.get_content()
        self.content = self.edit_shared_loader()
        fe.set_content(self.content)
        fe.write()

    def edit_shared_loader(self):
        new_content = []
        p = re.compile('^ *shared\\.loader=')
        for line in self.content:
            m = p.match(line)
            if m is not None:
                new_content.append('shared.loader=${catalina.base}/shared/classes,${catalina.base}/shared/lib/*.jar')
            else:
                new_content.append(line)
        return new_content


class CleanTomcatShEditor:

    def __init__(self):
        self.content = []
        self.tomcat = ''

    def set_tomcat(self, arg):
        self.tomcat = arg

    def run(self):
        fe = FileEntity()
        fe.set_path('/opt/alfresco/' + self.tomcat + '/bin/clean_tomcat.sh')
        fe.read()
        self.content = fe.get_content()
        self.content = self.edit_rm()
        fe.set_content(self.content)
        fe.write()

    def edit_rm(self):
        new_content = []
        p = re.compile('^ *rm +-rf (tomcat)/(.+)')
        for line in self.content:
            m = p.match(line)
            if m is not None:
                new_content.append('rm -rf /opt/alfresco/' + self.tomcat + '/' + m.group(2))
            else:
                new_content.append(line)
        return new_content


class ServerXmlEditor:

    def __init__(self):
        self.content = []
        self.tomcat = ''

    def set_tomcat(self, arg):
        self.tomcat = arg

    def run(self):
        fe = FileEntity()
        fe.set_path('/opt/alfresco/' + self.tomcat + '/conf/server.xml')
        fe.read()
        self.content = fe.get_content()
        self.content = self.insert_connector_setting()
        fe.set_content(self.content)
        fe.write()

    def insert_connector_setting(self):
        new_content = []
        for line in self.content:
            if line.find('Connector port="8080" protocol="HTTP/1.1"') > 0:
                new_content.append(line + ' URIEncoding="UTF-8"')
            elif line.find('connectionTimeout="20000"') > 0:
                new_content.append(line + ' maxHttpHeaderSize="32768"')
            else:
                new_content.append(line)
        return new_content


if __name__ == '__main__':
    gpe = GlobalPropertiesEditor()
    gpe.set_tomcat(TOMCAT_VERSION)
    gpe.set_repository_directory(REPOSITORY_DIRECTORY)
    gpe.set_db_username(DB_USERNAME)
    gpe.set_db_password(DB_PASSWORD)
    gpe.set_db_host(DB_HOST)
    gpe.set_db_port(DB_PORT)
    gpe.set_solr_host(SOLR_HOST)
    gpe.set_solr_port(SOLR_PORT)
    gpe.set_activemq_host(ACTIVEMQ_HOST)
    gpe.set_activemq_port(ACTIVEMQ_PORT)
    gpe.run()
    aase = ApplyAmpsShEditor()
    aase.set_tomcat(TOMCAT_VERSION)
    aase.run()
    cpe = CatalinaPropertiesEditor()
    cpe.set_tomcat(TOMCAT_VERSION)
    cpe.run()
    ctse = CleanTomcatShEditor()
    ctse.set_tomcat(TOMCAT_VERSION)
    ctse.run()
    sxe = ServerXmlEditor()
    sxe.set_tomcat(TOMCAT_VERSION)
    sxe.run()
