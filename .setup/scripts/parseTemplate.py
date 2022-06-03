from jinja2 import Template
import json
import os
from certificates import createCertificate

def parse_template(variables, output_filename, template_filename):
    output_file = open(output_filename, "w")
    output_file.write(Template(open(template_filename).read()).render(variables))
    output_file.close()

cwd = os.path.dirname(os.path.realpath(__file__)) + "/"
configFile = open(cwd + "../../config.json")
config = json.load(configFile)

parse_template(config, cwd + "../../docker-compose.yml", cwd + "../templates/docker-compose.yml.j2")
parse_template(config, cwd + "../../php/Dockerfile", cwd + "../templates/php.Dockerfile.j2")

projects = config['projects']

for project in projects:
    parse_template(project, cwd + "../../nginx/sites-available/" + project["domain"] + ".conf", cwd + "../templates/template.conf.j2")
    createCertificate(project['domain'])
