import re

ALFRESCO_HOST = '[alfresco_host]'
SOLR_HOST = '[solr_host]'


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


class SharedPropertiesEditor:

    def __init__(self):
        self.content = []
        self.solr_host = ''

    def set_solr_host(self, arg):
        self.solr_host = arg

    def run(self):
        fe = FileEntity()
        fe.set_path('/opt/alfresco/alfresco-search-services/solrhome/conf/shared.properties')
        fe.read()
        self.content = fe.get_content()
        self.content = self.edit_solr_host()
        self.content = self.uncomment_suggestable_properties()
        self.content = self.uncomment_cross_locale_datatype()
        fe.set_content(self.content)
        fe.write()

    def edit_solr_host(self):
        new_content = []
        p = re.compile('^ *solr\\.host')
        for line in self.content:
            m = p.match(line)
            if m is not None:
                new_content.append('solr.host=' + self.solr_host)
            else:
                new_content.append(line)
        return new_content

    def uncomment_suggestable_properties(self):
        new_content = []
        p = re.compile('^ *# *(alfresco\\.suggestable\\.property)(.+)')
        for line in self.content:
            m = p.match(line)
            if m is not None:
                new_content.append(m.group(1) + m.group(2))
            else:
                new_content.append(line)
        return new_content

    def uncomment_cross_locale_datatype(self):
        new_content = []
        p = re.compile('^ *# *(alfresco\\.cross\\.locale\\.datatype)(.+)')
        for line in self.content:
            m = p.match(line)
            if m is not None:
                new_content.append(m.group(1) + m.group(2))
            else:
                new_content.append(line)
        return new_content


class SolrcorePropertiesEditor:

    def __init__(self):
        self.content = []
        self.alfresco_host = ''

    def set_alfresco_host(self, arg):
        self.alfresco_host = arg

    def run(self):
        fe = FileEntity()
        fe.set_path('/opt/alfresco/alfresco-search-services/solrhome/templates/rerank/conf/solrcore.properties')
        fe.read()
        self.content = fe.get_content()
        self.content = self.edit_alfresco_host()
        fe.set_content(self.content)
        fe.write()

    def edit_alfresco_host(self):
        new_content = []
        p = re.compile('^ *alfresco\\.host')
        for line in self.content:
            m = p.match(line)
            if m is not None:
                new_content.append('alfresco.host=' + self.alfresco_host)
            else:
                new_content.append(line)
        return new_content


class SolrInShEditor:

    def __init__(self):
        self.content = []
        self.solr_host = ''
        self.alfresco_host = ''

    def set_solr_host(self, arg):
        self.solr_host = arg

    def set_alfresco_host(self, arg):
        self.alfresco_host = arg

    def run(self):
        fe = FileEntity()
        fe.set_path('/opt/alfresco/alfresco-search-services/solr.in.sh')
        fe.read()
        self.content = fe.get_content()
        self.content = self.insert_host()
        self.content = self.uncomment_solr_port()
        fe.set_content(self.content)
        fe.write()

    def insert_host(self):
        new_content = ['SOLR_SOLR_HOST=' + self.solr_host, 'SOLR_ALFRESCO_HOST=' + self.alfresco_host]
        for line in self.content:
            new_content.append(line)
        return new_content

    def uncomment_solr_port(self):
        new_content = []
        p = re.compile('^ *# *SOLR_PORT')
        for line in self.content:
            m = p.match(line)
            if m is not None:
                new_content.append('SOLR_PORT=8983')
            else:
                new_content.append(line)
        return new_content


if __name__ == '__main__':
    spe = SharedPropertiesEditor()
    spe.set_solr_host(SOLR_HOST)
    spe.run()
    scpe = SolrcorePropertiesEditor()
    scpe.set_alfresco_host(ALFRESCO_HOST)
    scpe.run()
    sise = SolrInShEditor()
    sise.set_solr_host(SOLR_HOST)
    sise.set_alfresco_host(ALFRESCO_HOST)
    sise.run()
