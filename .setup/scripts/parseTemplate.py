from jinja2 import Template
import json
import os
from OpenSSL import crypto, SSL
from certificates import createCertificate

projects = {}
cwd = os.path.dirname(os.path.realpath(__file__)) + "/"
projectsFile = open(cwd + "../../projects.json")
projects = json.load(projectsFile)
dockerComposeConfig = open(cwd + "../templates/docker-compose.yml.j2")

for project in projects:
    outputFile = open(cwd + "../../nginx/sites-available/" + project["domain"] + ".conf", "w")
    nginxConfig = open(cwd + "../templates/template.conf.j2")
    template = Template(nginxConfig.read())
    nginxConfig.close()
    outputFile.write(template.render(project))
    outputFile.close()
    createCertificate(project['domain'])

projectsArray = {"projects": projects}
outputFile = open(cwd + "../../docker-compose.yml", "w")
template = Template(dockerComposeConfig.read())
outputFile.write(template.render(projectsArray))
outputFile.close()
