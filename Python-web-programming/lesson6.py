import pysftp


def push_file_to_server():
    cnopts = pysftp.CnOpts()
    cnopts.hostkeys = None
    with pysftp.Connection(host='143.244.152.180', username='', password='', cnopts=cnopts):
        local_path = 'testme.txt'
        remote_path = '/home/testme.txt'
        pysftp.put_d(local_path, remote_path)
        pysftp.close()

push_file_to_server()

def pull_file_from_server():
    cnopts = pysftp.CnOpts()
    cnopts.hostkeys = None
    with pysftp.Connection(host='143.244.152.180', username='', password='', cnopts=cnopts):
        remote_path = 'testme.txt'
        local_path = '/home/testme.txt'
        pysftp.get_d(remote_path, local_path)
        pysftp.close()


#does not work. Investigate in docs later. Tutorial old.