import socket
import threading


def main():
    # 创建TCP套接字
    tcp_server_scoket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    # 端口复用
    tcp_server_scoket.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,True)
    # 绑定端口号
    tcp_server_scoket.bind(('',8000))
    # 监听端口
    tcp_server_scoket.listen(128)

    while True:

        # 接受TCP连接
        new_socket,ip_addr = tcp_server_scoket.accept()

        recv_data = new_socket.recv(4096)
        if len(recv_data) == 0:
            new_socket.close()
            return
        recv_content = recv_data.decode('utf-8')
        request_list = recv_content.split(' ',maxsplit=2)
        request_path = request_list[1]
        print(request_path)
        if request_path == '/':
            request_path = '/index.html'

        try:
            with open("static" + request_path,'rb') as file:
                file_data = file.read()

        except FileNotFoundError as a:
            with open('static/error.html','rb') as file:
                file_data = file.read()
                print(a)
                response_line = 'HTTP/1.1 404 Not Found\r\n'
            # 响应头
            response_header = 'Server:pws/1.0\r\n'
            # 响应体
            response_body = file_data

            response = (response_line + response_header + '\r\n').encode('utf-8') + response_body

            new_socket.send(response)
        else:
            response_line = 'HTTP/1.1 200 OK\r\n'
            # 响应头
            response_header = 'Server:pws/1.0\r\n'
            # 响应体
            response_body = file_data

            response = (response_line + response_header+ '\r\n').encode('utf-8') + response_body

            new_socket.send(response)
        finally:
            new_socket.close()


if __name__ == '__main__':
    main()
        # web_thread = threading.Thread(target=web_serve,args=(new_socket,ip_addr))
        # web_thread.setDaemon(True)
        # web_thread.start()
