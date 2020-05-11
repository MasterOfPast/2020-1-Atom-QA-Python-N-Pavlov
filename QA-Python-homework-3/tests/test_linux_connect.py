import pytest
from socket_client import request


class Test_SSH:
    @pytest.mark.SSHD
    def test_root_connect(self, ssh_cl):
        line = ssh_cl.last_strs("/var/log/messages")
        assert line.split()[-1][:-1] == 'root'

    @pytest.mark.SSHD
    def test_nginx_port_http(self, nginx_data):
        # Получаю заголовки и там смотрю что Server: nginx/версия
        host, port = nginx_data
        result = request('GET', host, port, '/', headers='User-Agent: Test\r\nAccept-Encoding: gzip, deflate')
        assert result.status_code == 200
        assert result.headers.split()[1].split('/')[0] == 'nginx'

    @pytest.mark.SSHD
    def test_nginx_port_ssh(self, ssh_cl):
        assert ssh_cl.exec_cmd('netstat -tnlp | grep nginx').split()[3] == '0.0.0.0:801'

    @pytest.mark.SSHD
    def test_check_log(self, ssh_cl, nginx_data, random_name):
        host, port = nginx_data
        request('GET', host, port, '/', headers=f'User-Agent: {random_name}\r\nAccept-Encoding: gzip, deflate')
        line = ssh_cl.last_strs("/var/log/nginx/access.log")

        assert line.split()[11][1: -1] == random_name
        assert line.split()[8] == '200'

    @pytest.mark.SSHD
    def test_kill_port(self, ssh_cl, nginx_data):
        host, port = nginx_data
        ssh_cl.exec_cmd('firewall-cmd --permanent --zone=public --remove-port=801/tcp')
        ssh_cl.exec_cmd('firewall-cmd --reload')
        result = request('GET', host, port, '/', headers='User-Agent: Test\r\nAccept-Encoding: gzip, deflate')
        assert result == 'host died'
        assert ssh_cl.exec_cmd('netstat -tnlp | grep nginx').split()[3] == '0.0.0.0:801'
        ssh_cl.exec_cmd('firewall-cmd --permanent --zone=public --add-port=801/tcp')
        ssh_cl.exec_cmd('firewall-cmd --reload')
