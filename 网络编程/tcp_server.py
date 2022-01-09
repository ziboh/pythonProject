import socket
import time
import threading
def handle_client_request(new_socket,ip_port):
    # tcp_socket_server.accept()
    # 5.接受客服端的套接字
    print('客服端的ip端口号：', ip_port)
    while True:
        recv_data = new_socket.recv(1024)
        if recv_data:
            racv_text = recv_data.decode('gbk')
            print('接收的数据为：', racv_text)
            sessions = open('sessions.txt', 'a+', encoding='gbk')
            sessions.write(f'\n{racv_text}')
            # 6.发送数据到客服端
            send_content = '问题正在处理中...'
            send_data = send_content.encode('gbk')
            new_socket.send(send_data)
        else:
            print(ip_port,'断开连接')
            break
    # 7关闭套接字
    new_socket.close()
if __name__ == '__main__':

    # 1.创建tcp服务端套接字
    tcp_socket_server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    # 设置端口号复用
    tcp_socket_server.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,True)
    # 2.设置端口号
    tcp_socket_server.bind(('',9090))
    # 3.设置监听
    tcp_socket_server.listen(128)
    while True:
        # 4.等待接受连接请求
        new_socket, ip_port = tcp_socket_server.accept()
        thread_tcp_server = threading.Thread(target=handle_client_request, args=(new_socket, ip_port))
        thread_tcp_server.setDaemon(True)
        thread_tcp_server.start()

    # tcp_socket_server.close()
