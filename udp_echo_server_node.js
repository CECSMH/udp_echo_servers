const os = require('os');
const dgram = require('dgram');
const socket = dgram.createSocket('udp4');

const computer_name = ['star platinum', 'killer queen', 'foo fighters', 'gold experience', 'crazy diamond', 'd4c', 'husk', 'stone free', 'white snake', 'gg dolls'][Math.floor(Math.random() * 10)]//os.hostname();
const port = 9090;

socket.on('listening', function () {
	const address = socket.address();
	console.log('Ouvindo em ' + address.address + ":" + address.port);
});

socket.on('message', function (message, remote) {
	console.log(`Recebido: ${remote.address} : ${remote.port} - ${message}`);

	const response = JSON.stringify({ port, name: `${computer_name} - node` })

	socket.send(response, 0, response.length, remote.port, remote.address);
});

socket.bind(port);