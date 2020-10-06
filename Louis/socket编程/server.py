__author__ = 'Louis-Pan'

import socket,os

server = socket.socket()
server.bind(("localhost",6666))
server.listen()

while True:
    conn,addr = server.accept()
    print("新的连接：",addr)
    while True:
        print("等待新的ssh指令")
        data = conn.recv(1024)
        if not data:
            print("客户端已断开连接")
            break
        print("执行ssh指令",data)
        cmd_res = os.popen(data.decode()).read()
        print("发送之前：",len(cmd_res))
        if len(cmd_res)==0:
            cmd_res = "cmd has no output...."
        conn.send(str(len(cmd_res.encode())).encode("utf-8")) # 先发送ssh指令的数据大小
        client_ack = conn.recv(1024)
        conn.send(cmd_res.encode("utf-8"))
        print("send done")
server.close()
