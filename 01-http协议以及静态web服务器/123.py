from urllib.parse import quote, unquote, urlencode


def main():
    my_data = 'D:\zbh\Documents\PycharmProjects\pythonProject\01-http协议以及静态web服务器\static\拉拉.html'

    # url编码
    encode_data = quote(my_data)
    print("encode_data : %s " % encode_data)
    # url解码
    decode_data = unquote(encode_data)
    print("decode_data : %s " % decode_data)

    my_query = {'conent': '天天向上'}
    # url参数编码
    encode_query = urlencode(my_query)
    print("encode_query : %s " % encode_query)
    # url参数解码
    decode_query = unquote(encode_query)
    print("decode_query : %s " % decode_query)
    encode_url = 'http://127.0.0.1?' + encode_query
    # url解码
    decode_url = unquote(encode_url)
    print("decode_url : %s " % decode_url)


if __name__ == '__main__':
    main()