import socket, random, json

name = ['star platinum', 'killer queen', 'foo fighters', 'gold experience', 'crazy diamond', 'd4c', 'husk', 'stone free', 'white snake', 'gg dolls'][random.randint(0,9)]

port = 9090
bufferSize = 1024

response = json.dumps({
    "port" : port,
    "name" : name + " - python"
})

bytesToSend = str.encode(response)

UDPServerSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
UDPServerSocket.bind(('0.0.0.0', port))

print("ouvindo na porta: " + str(port))

while(True):
    bytesAddressPair = UDPServerSocket.recvfrom(bufferSize)
    message = bytesAddressPair[0]
    address = bytesAddressPair[1]

    print("Recebido: " + str(address) + " : " + str(message))

    UDPServerSocket.sendto(bytesToSend, address)

    print("Enviado: " + response)