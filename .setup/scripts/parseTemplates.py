from jinja2 import Template
import json
import os
from certificates import createCertificate

def parse_template(variables, output_filename, template_filename):
    os.makedirs(os.path.dirname(output_filename), exist_ok=True)
    output_file = open(output_filename, "w")
    output_file.write(Template(open(template_filename).read()).render(variables))
    output_file.close()

cwd = os.path.dirname(os.path.realpath(__file__)) + "/"
configFile = open(cwd + "../../config.json")
config = json.load(configFile)

parse_template(config, cwd + "../../docker-compose.yml", cwd + "../templates/docker-compose.yml.j2")
parse_template(config, cwd + "../../php/Dockerfile", cwd + "../templates/php.Dockerfile.j2")
parse_template(config, cwd + "../../nginx/Dockerfile", cwd + "../templates/nginx.Dockerfile.j2")
parse_template(config, cwd + "../../database/setup/entrypoint.sh", cwd + "../templates/setup.entrypoint.sh.j2")

databases = config['databases']
if databases:
    for database in databases:
        for schema in database['schemas']:
            parse_template(schema, cwd + "../../database/sql/" + database['container_name'] + "/" + schema['name'] + ".sql", cwd + "../templates/createDatabase.sql.j2")

projects = config['projects']

for project in projects:
    parse_template(project, cwd + "../../nginx/sites-available/" + project["domain"] + ".conf", cwd + "../templates/template.conf.j2")
    createCertificate(project['domain'])
