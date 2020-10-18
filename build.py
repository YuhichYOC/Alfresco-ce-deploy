import os
import subprocess

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


class FileEntity:

    def __init__(self):
        self.content = []
        self.path = ''

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


def replace_content(content, keyword, replacement):
    new_content = []
    for line in content:
        new_content.append(line.replace(keyword, replacement))
    return new_content


def prepare_alfrescodb():
    if os.path.isdir('alfrescodb'):
        fe = FileEntity()
        fe.set_path('alfrescodb/Dockerfile')
        fe.read()
        content = fe.get_content()
        new_content = replace_content(content, '[postgres_user]', DB_USERNAME)
        new_content = replace_content(new_content, '[postgres_password]', DB_PASSWORD)
        fe.set_content(new_content)
        fe.write()


def prepare_activemq():
    if os.path.isdir('activemq'):
        fe = FileEntity()
        fe.set_path('activemq/Dockerfile')
        fe.read()
        content = fe.get_content()
        new_content = replace_content(content, '[activemq]', ACTIVEMQ_VERSION)
        fe.set_content(new_content)
        fe.write()


def prepare_artemis():
    if os.path.isdir('artemis'):
        fe = FileEntity()
        fe.set_path('artemis/Dockerfile')
        fe.read()
        content = fe.get_content()
        new_content = replace_content(content, '[artemis]', ARTEMIS_VERSION)
        new_content = replace_content(new_content, '[artemis_user]', ARTEMIS_USER)
        new_content = replace_content(new_content, '[artemis_password]', ARTEMIS_PASSWORD)
        new_content = replace_content(new_content, '[artemis_role]', ARTEMIS_ROLE)
        new_content = replace_content(new_content, '[artemis_allow_anonymous]', ARTEMIS_ALLOW_ANONYMOUS)
        fe.set_content(new_content)
        fe.write()


def prepare_alfresco_search():
    if os.path.isdir('alfresco-search'):
        fe = FileEntity()
        fe.set_path('alfresco-search/Deployer.py')
        fe.read()
        content = fe.get_content()
        new_content = replace_content(content, '[alfresco_host]', ALFRESCO_HOST)
        new_content = replace_content(new_content, '[solr_host]', SOLR_HOST)
        fe.set_content(new_content)
        fe.write()
        fe.set_path('alfresco-search/Dockerfile')
        fe.read()
        content = fe.get_content()
        new_content = replace_content(content, '[alfresco-search]', ALFRESCO_SEARCH)
        fe.set_content(new_content)
        fe.write()


def prepare_alfresco():
    if os.path.isdir('alfresco'):
        fe = FileEntity()
        fe.set_path('alfresco/Deployer.py')
        fe.read()
        content = fe.get_content()
        new_content = replace_content(content, '[tomcat_version]', TOMCAT_VERSION)
        new_content = replace_content(new_content, '[path_to_repository_directory]', PATH_TO_REPOSITORY_DIRECTORY)
        new_content = replace_content(new_content, '[solr_host]', SOLR_HOST)
        new_content = replace_content(new_content, '[solr_port]', SOLR_PORT)
        new_content = replace_content(new_content, '[activemq_host]', ACTIVEMQ_HOST)
        new_content = replace_content(new_content, '[activemq_port]', ACTIVEMQ_PORT)
        new_content = replace_content(new_content, '[db_host]', DB_HOST)
        new_content = replace_content(new_content, '[db_port]', DB_PORT)
        new_content = replace_content(new_content, '[db_username]', DB_USERNAME)
        new_content = replace_content(new_content, '[db_password]', DB_PASSWORD)
        fe.set_content(new_content)
        fe.write()
        fe.set_path('alfresco/ApplyAmpsShRunner.py')
        fe.read()
        content = fe.get_content()
        new_content = replace_content(content, '[apply_amps_sh]',
                                      '/opt/alfresco/' + TOMCAT_VERSION + '/bin/' + APPLY_AMPS_SH)
        fe.set_content(new_content)
        fe.write()
        fe.set_path('alfresco/Dockerfile')
        fe.read()
        content = fe.get_content()
        new_content = replace_content(content, '[tomcat]', TOMCAT_VERSION)
        new_content = replace_content(new_content, '[alfresco]', ALFRESCO_VERSION)
        fe.set_content(new_content)
        fe.write()
        fe.set_path('alfresco/run.test.sh')
        fe.read()
        content = fe.get_content()
        new_content = replace_content(content, '[alfresco_host]', ALFRESCO_HOST)
        fe.set_content(new_content)
        fe.write()
        fe.set_path('start.sh')
        fe.read()
        content = fe.get_content()
        new_content = replace_content(content, '[tomcat]', TOMCAT_VERSION)
        fe.set_content(new_content)
        fe.write()
        fe.set_path('stop.sh')
        fe.read()
        content = fe.get_content()
        new_content = replace_content(content, '[tomcat]', TOMCAT_VERSION)
        fe.set_content(new_content)
        fe.write()


if __name__ == '__main__':
    prepare_alfrescodb()
    prepare_activemq()
    prepare_artemis()
    prepare_alfresco_search()
    prepare_alfresco()
    subprocess.call(['chmod', '754', 'firstboot.sh'])
    subprocess.call(['chmod', '754', 'start.sh'])
    subprocess.call(['chmod', '754', 'stop.sh'])
    if os.path.isdir('openjdk'):
        subprocess.call(['chmod', '754', 'openjdk/build.sh'])
        subprocess.call('openjdk/build.sh')
    if os.path.isdir('alfrescodb'):
        subprocess.call(['chmod', '754', 'alfrescodb/build.sh'])
        subprocess.call('alfrescodb/build.sh')
    if os.path.isdir('activemq'):
        subprocess.call(['chmod', '754', 'activemq/build.sh'])
        subprocess.call(['chmod', '754', 'activemq/run.test.sh'])
        subprocess.call('activemq/build.sh')
    if os.path.isdir('artemis'):
        subprocess.call(['chmod', '754', 'artemis/build.sh'])
        subprocess.call(['chmod', '754', 'artemis/run.test.sh'])
        subprocess.call('artemis/build.sh')
    if os.path.isdir('alfresco-search'):
        subprocess.call(['chmod', '754', 'alfresco-search/build.sh'])
        subprocess.call(['chmod', '754', 'alfresco-search/run.test.sh'])
        subprocess.call('alfresco-search/build.sh')
    if os.path.isdir('alfresco'):
        subprocess.call(['chmod', '754', 'alfresco/build.sh'])
        subprocess.call(['chmod', '754', 'alfresco/run.test.sh'])
        subprocess.call('alfresco/build.sh')
