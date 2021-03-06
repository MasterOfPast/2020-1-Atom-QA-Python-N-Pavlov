from paramiko import SSHClient, AutoAddPolicy, AuthenticationException, SSHException
import time


class SSH():
    def __init__(self, **kwargs):
        self.client = SSHClient()
        self.client.set_missing_host_key_policy(AutoAddPolicy())
        self.kwargs = kwargs

    def __enter__(self):
        kw = self.kwargs
        try:
            self.client.connect(
                hostname=kw.get('hostname'),
                port=int(kw.get('port', 22)),
                username=kw.get('username'),
                password=kw.get('password'),
            )
        except AuthenticationException:
            print("Authentication failed, please verify your credentials")
        except SSHException as sshException:
            print(f"Could not establish SSH connection {sshException}")

        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.client.close()

    def exec_cmd(self, cmd):
        stdin, stdout, stderr = self.client.exec_command(cmd)
        data = stdout.read()
        data = data.decode()

        err = stderr.read()
        err = err.decode()

        if err:
            raise Exception(f'Err:{err}')

        return data

    def last_strs(self, path, number=1):
        time.sleep(0.5)
        return self.exec_cmd(f'cat {path} | tail -n {number}')

    def change_to_root(self):
        # Попытка сделать смену пользователя
        stdin, stdout, stderr = self.client.exec_command('su')
        stdin.write('a1b2c3\n')


if __name__ == "__main__":
    with SSH(hostname='192.168.56.101', username='root', password='a1b2c3',
             port=2203) as ssh:
        time.sleep(0.5)
        print(ssh.exec_cmd('cat /var/log/messages | tail -n 2'))
