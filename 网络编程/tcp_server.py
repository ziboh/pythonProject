import socket
import time

if __name__ == '__main__':

    # 1.创建tcp服务端套接字
    tcp_socket_server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    # 设置端口号复用
    tcp_socket_server.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,True)
    # 2.设置端口号
    tcp_socket_server.bind(('',9090))
    # 3.设置监听
    tcp_socket_server.listen(128)
    # 4.等待接受连接请求
    new_socket,ip_port = tcp_socket_server.accept()
    # 5.接受客服端的套接字
    print('客服端的ip端口号：',ip_port)
    recv_data = new_socket.recv(1024)
    print('接收的数据为：',recv_data.decode('gbk'))
    # 6.发送数据到客服端
    send_content = '问题正在处理中...'
    send_data = send_content.encode('gbk')
    new_socket.send(send_data)
    # 7关闭套接字


    tcp_socket_server.close()
    time.sleep(20)
    new_socket.close()