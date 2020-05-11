import socket


def request(method, host, port, params, data=None, headers=None):
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.settimeout(0.6)
    try:
        client.connect((host, port))
    except Exception:
        return 'host died'

    request = f'{method} {params} HTTP/1.1\r\nHost: {host}'
    if headers is not None:
        request += f'\r\n{headers}'
    new_data = ""
    if data is not None:
        request += "\r\nContent-Type:application/x-www-form-urlencoded"
        for key, value in data.items():
            new_data += f'{key}={value}&'
        new_data = new_data[:-1]
        request += f"\r\nContent-Length:{len(new_data)}\r\n\r\n"
        request += new_data
    request += '\r\n\r\n'
    client.send(request.encode())

    total_data = []

    while True:
        try:
            data = client.recv(4096)
            if data:
                total_data.append(data.decode())
            else:
                break
        except Exception:
            break
    client.close()
    return result(total_data)


class result:
    def __init__(self, total_data):
        if len(total_data) == 3:
            self.status_code = int(total_data[0].split(" ")[1])
            self.headers = total_data[1]
            self.data = total_data[2]
        elif len(total_data) == 2:
            if total_data[0].find('Content-Type') != -1:
                self.status_code = int(total_data[0].split(" ")[1])
                self.headers = total_data[0][total_data[0].find('\r\n') + 2:]
                self.data = total_data[1]
            else:
                self.status_code = int(total_data[0].split(" ")[1])
                self.headers = total_data[1][total_data[1].find('\r\n') + 2:
                                             total_data[1].find('\r\n\r\n')]
                self.data = total_data[1][total_data[1].find('\r\n\r\n') + 4:]
        else:
            self.status_code = int(total_data[0].split(" ")[1])
            self.headers = total_data[0][total_data[0].find('\r\n') + 2:
                                         total_data[0].find('\r\n\r\n')]
            self.data = total_data[0].split('\r\n')[-1]

        self.data = self.data.strip('\n')
