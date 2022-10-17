const URL = "ws://127.0.0.1:8080";
let socket = new WebSocket(URL);

const eventLogger = (event, data = event) => {
  console.log(`[${event.type}]: `, data);
};

socket.onopen = (event) => {
  eventLogger(event);
  console.log("Socket connected to Python server");
  document.addEventListener("keypress", ({ key, code }) => {
    socket.send(JSON.stringify({ key, code }));
  });
};

socket.onmessage = (event) => {
  eventLogger(event);
  const serverContainer = document.getElementById("serverResponse");
  let chatStr = "";
  JSON.parse(event.data)["messages"]?.map((msg) => {
    chatStr += `<p><b>${msg?.cid}</b>: ${msg?.msg}</p>`;
  });
  serverContainer.innerHTML = chatStr;
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

const sendmsg = () => {
  let inputMsg = document.getElementById("msgBox").value;
  if (inputMsg) {
    socket.send();
    document.getElementById("msgBox").value = "";
  }
};

const handleSubmit = (e) => {
  e.preventDefault();

  socket.send(e.target[0].value);
};
