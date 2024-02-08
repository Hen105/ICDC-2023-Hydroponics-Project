const express = require ('express')
const SerialPort = require("serialport")
const Readline = require ("@serialport/parser-readline");

const ap = epress ();
const port = new SerialPort('/dev/ttyACMO', { baudRate: 9600});
const parser = port.pipe(new Readline({ delimiter: "/n"}));

app.get ("/", (reg, res) => {
		res.sendFile(__dirname + "/water2.html");
});

app.get("/send8", (req, res) => {
	port.write('8')
	res.send("Command Sent")
});

app.listen(3000, () => {
	console.log("Server started on http://localhost:3000")
});
