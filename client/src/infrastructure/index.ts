import config from "../common/config";
import { ClientData } from "../common/types";

let socket = new WebSocket(config.WS_API);

export const SERVER = {
  start: () => {
    socket.onopen = (event) => {
      console.log("Socket connected to Python server");
    };
    socket.onclose = (event) => {
      if (event.wasClean) console.log("Socket closed cleanly");
      else console.log("Socket closed unexpectedly");
    };
  },

  receive: (callback: (data: ClientData) => void) =>
    (socket.onmessage = (e) => callback(JSON.parse(e.data))),

  send: (data: any) => socket.send(JSON.stringify(data)),

  close: () => socket.close(),
};
