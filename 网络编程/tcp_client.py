import socket

if __name__ == '__main__':

    # 1创建tcp客户端套接字
    # AF_INET表示ipv4协议
    # SOCK_STREAM表示tcp传输协议
    tcp_client_scoket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    # 建立tcp连接
    tcp_client_scoket.connect(('172.26.133.107',9090))
    # 发送数据到服务端
    send_content = 'Hello world'
    # 把数据转化为网络可以传输的二进制数据
    send_data = send_content.encode('utf-8')
    tcp_client_scoket.send(send_data)
    # 接收服务点的数据
    recv_data = tcp_client_scoket.recv((1024))
    recv_content = recv_data.decode('gbk')
    print(recv_content)
    # 关闭tcp连接
    tcp_client_scoket.close()