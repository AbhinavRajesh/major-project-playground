
let socket = new WebSocket("ws://127.0.0.1:8080/logger");

export const logger = {
  start: () => {
    socket.onopen = (event) => {
      console.log("Socket connected to Python server");
    };
  },

  receive: (callback: (data: any) => void) =>
    (socket.onmessage = (e: { data: any }) => callback(e.data)),

  send: (data: any) => socket.send(JSON.stringify(data)),
  onclose: (callback: () => void) => {
    socket.onclose = (event) => {
      if (event.wasClean) console.log("Socket closed cleanly");
      else console.log("Socket closed unexpectedly");
      callback();
    };
  },
  close: () => socket.close(),
};
