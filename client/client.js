/**
 * IGNORE THIS FILE
 * THIS IS ME TRYING TO CONNECT A WEBSOCKET TO A TCP CONNECTION :/
 * https://stackoverflow.com/questions/15160739/possible-for-websocket-client-on-browser-to-talk-to-tcp-socket-server
 */
// const URL = "wss://0.0.0.0:8080";
const URL = "ws://127.0.0.1:8080";
let socket = new WebSocket(URL);

const eventLogger = (event, data = event) => {
  console.log(`[${event.type}]: `, data);
};

socket.onopen = (event) => {
  eventLogger(event);
  console.log("Socket connected to CPP server");
  console.log('Sending "Hello" to server');
  socket.send("Hi, I'm Client");
};

socket.onmessage = (event) => {
  eventLogger(event);
  console.log(`Server said: ${event.data}`);

  const serverContainer = document.getElementById("serverResponse");
  serverContainer.innerHTML = event.data;
};

socket.onclose = (event) => {
  eventLogger(event);
  if (event.wasClean) {
    alert(
      `[close] Connection closed cleanly, code=${event.code} reason=${event.reason}`
    );
  } else {
    // e.g. server process killed or network down
    // event.code is usually 1006 in this case
    alert("[close] Connection died");
  }
};

socket.onerror = (event) => {
  eventLogger(event);
};

const sendhi = () => {
  socket.send("Hi");
};

const handleSubmit = (e) => {
  e.preventDefault();

  socket.send(e.target[0].value);
};
