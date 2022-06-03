import os
from ownca import CertificateAuthority

currentDir = os.path.dirname(os.path.realpath(__file__)) + "/"

def createCertificate(cn):
    ca = CertificateAuthority(ca_storage=currentDir+"../../nginx/ssl", common_name='Your Development')
    ca.issue_certificate(hostname=cn)