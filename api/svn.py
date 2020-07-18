# -*- encoding: utf-8 -*-
__author__ = 'tang'


import pysvn


# Get svn server connection
def ssl_server_trust_prompt(trust_dict):
    # True -> ssl server is trusted
    # False -> ssl server is not trusted
    retcode = True
    # int, the accepted failures allowed
    # Typically just return trust_dict["failures"]
    accepted_failures = trust_dict['failures']
    # True -> remember the certificate in the configuration directory
    # False -> prevent saving the certificate
    save = True
    return retcode, accepted_failures, save


# Login svn
def get_login(realm, username, may_save):
    # True -> subversion is to use the username and password
    # False -> no username and password are available
    retcode = True
    username = 'xxx'
    password = 'xxxxxx'
    # True -> remember the username and password in the configuration directory
    # False -> prevent saving the username and password
    save = False
    return retcode, username, password, save


def upload_to_svn(url, filepath, filename):
    # Start svn client
    client = pysvn.Client()
    # Connect to svn server
    client.callback_ssl_server_trust_prompt = ssl_server_trust_prompt
    # Login svn
    client.callback_get_login = get_login

    # Commit an unversioned file or tree into the repository
    # e.g. svn_url = 'https://xx.xx.xxx.xxx/svn/xxxxxx/xxxxx/xxxx/xxx'
    # e.g. client.import_('C:\Users\\tang\Desktop\\test.docx', svn_url + '/test.docx', '上传文件')
    client.import_(filepath, url + '/' + filename, '上传文件')

    # client.ls() returns a list of dictionaries for each file the given path at the provided revision
    # url_files = client.ls(svn_url, recurse=True)
    # print(url_files)
