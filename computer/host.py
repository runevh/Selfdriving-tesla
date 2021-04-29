import cv2
import pickle
import socket
import struct

# create socket

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host_ip = '192.168.1.2'  # paste your server ip address here
port = 9999
client_socket.connect((host_ip, port))  # a tuple
data = b""
payload_size = struct.calcsize("Q")

def getFrame():
    return frame

def linedetection(frame69):
    gray = cv2.cvtColor(frame69, cv2.COLOR_BGR2GRAY)

    kernel_size = 5
    blur_gray = cv2.GaussianBlur(gray, (kernel_size, kernel_size), 0)

    low_threshold = 50
    high_threshold = 150
    edges = cv2.Canny(blur_gray, low_threshold, high_threshold)

    cv2.imshow("Video test stream", edges)

while True:
    while len(data) < payload_size:
        packet = client_socket.recv(4 * 1024)  # 4K
        if not packet: break
        data += packet
    packed_msg_size = data[:payload_size]
    data = data[payload_size:]
    msg_size = struct.unpack("Q", packed_msg_size)[0]

    while len(data) < msg_size:
        data += client_socket.recv(4 * 1024)
    frame_data = data[:msg_size]
    data = data[msg_size:]
    frame = pickle.loads(frame_data)
    scale_percent = 400  # percent of original size

    width = int(frame.shape[1] * scale_percent / 100)
    height = int(frame.shape[0] * scale_percent / 100)
    dim = (width, height)
    resized = cv2.resize(frame, dim, interpolation=cv2.INTER_AREA)

    cv2.imshow("lol",resized)

    linedetection(resized)

    key = cv2.waitKey(1) & 0xFF
    if key == ord('z'):
        print("z")
    if key == ord('q'):
        print("q")
    if key == ord('s'):
        print("s")
    if key == ord('d'):
        print("d")

    if key == ord('v'):
        break
client_socket.close()

