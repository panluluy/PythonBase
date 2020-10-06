__author__ = 'Louis-Pan'

import socket,os,time

server = socket.socket()
server.bind(("localhost",9999))
server.listen()

while True:
    conn,addr = server.accept()
    print("开始接受客户端的连接",addr)
    while True:
        print("等待客户端的ssh命令")
        data = conn.recv(1024)
        if not data:
            print("客户端断开连接")
            break
        print("执行ssh命令：",data)
        cmd_res = os.popen(data.decode()).read()
        print("ssh命令返回值大小",len(cmd_res))
        if cmd_res == 0:
            print("cmd窗口没有输入任何内容")
        conn.send(str(len(cmd_res.encode())).encode("utf-8"))
        # time.sleep(0.5)
        client_ack = conn.recv(1024)
        conn.send(cmd_res.encode("utf-8"))
        print("命令发送完成")
server.close()

