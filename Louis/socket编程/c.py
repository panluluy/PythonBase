__author__ = 'Louis-Pan'
import socket

client = socket.socket()
client.connect(("localhost",9999))

while True:
    cmd = input("请输入ssh命令：").strip()
    if len(cmd)==0:continue
    client.send(cmd.encode("utf-8"))
    cmd_res_size = client.recv(1024)
    print("服务器返回ssh命令执行结果总的大小",cmd_res_size)
    client.send("客户端准备接收数据".encode("utf-8"))
    received_size = 0
    received_data = b''
    while received_size < int(cmd_res_size.decode()):
        data = client.recv(1024)
        received_size += len(data)
        print(data.decode())
        received_data += data
    else:
        print("客户端已经接收完数据：",received_size)
client.close()
