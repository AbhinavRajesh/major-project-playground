/**
 * IGNORE THIS FILE
 * THIS IS ME TRYING TO CONNECT A WEBSOCKET TO A TCP CONNECTION :/
 * https://stackoverflow.com/questions/15160739/possible-for-websocket-client-on-browser-to-talk-to-tcp-socket-server
 */
const URL = "ws://127.0.0.1:8080";
let socket = new WebSocket(URL);

socket.onopen = (e) => {
  console.log("Socket connected to CPP server");
  console.log('Sending "Hello" to server');
  socket.send("Hi, I'm Client");
};

socket.onmessage = (e) => {
  console.log(`Server said: ${e.data}`);
};

socket.onclose = (event) => {
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

socket.onerror = (error) => {
  console.log(error);
  alert(`[error] ${error.message}`);
};

const sendhi = () => {
  socket.send("Hi");
};
