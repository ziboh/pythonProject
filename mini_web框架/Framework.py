import time
import pymysql


route_list = []
def route(path):

    def decorator(func):
        route_list.append((path,func))
        def inner():
            return func()
        return inner
    return decorator

@route('/index.html')
def index():
    status = "200 OK"
    response_header = [("server","PWS/1.1")]
    with open("template/index.html","r",encoding="utf-8") as file:
        file_data = file.read()
    conn = pymysql.connect(host="localhost",
                           port=3306,
                           user="root",
                           password="123456",
                           database="stock_db",
                           charset="utf8")
    cursor = conn.cursor()
    sql = 'select * from info;'
    cursor.execute(sql)
    result = cursor.fetchall()
    print(result)
    cursor.close()
    conn.close()


    data = ''
    for row in result:
        data += """<tr>
                <td>%s</td>
                <td>%s</td>
                <td>%s</td>
                <td>%s</td>
                <td>%s</td>
                <td>%s</td>
                <td>%s</td>
                <td>%s</td>
                <td><input type="button" value="添加" id="toAdd" name="toAdd" systemidvaule="000007"></td>
               </tr>""" % row

    resonse_bady = file_data.replace('{%content%}',data)
    return status,response_header,resonse_bady

@route('/center.html')
def center():
    status = "200 OK"
    response_header = [("server","PWS/1.1")]
    date = time.ctime()
    return status,response_header,date

def error():
    status = "404 Not Found"
    response_header = [("server","PWS/1.1")]
    data = "404 NOT FOUND"
    return status,response_header,data



def handle_request(env):
    request_path = env["request_path"]
    print(f"动态资源请求地址：{request_path}")

    for path, func in route_list:
        if request_path == path:
            result = func()
            return result
    else:
        return error()


if __name__ == '__main__':
    print(route_list)