FROM python:latest

RUN mkdir /home/dev-ops

RUN pip install jinja2 pyOpenSSL

RUN pip install git+https://github.com/OwnCA/ownca.git


CMD ["python3", "/home/dev-ops/.setup/scripts/parseTemplates.py"]