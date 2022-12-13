import React, { useEffect, useState } from "react";
import { ClientData } from "../../common/types";
import { SERVER } from "../../infrastructure";
import Message from "./common/Message";
import "./index.css";

const Chat = () => {
  const [currMessage, setCurrMessage] = useState("");
  const [messages, setMessages] = useState<ClientData[]>([]);

  const handleRecieveMessage = (data: ClientData) => {
    // console.log(data);
    var snd = new Audio("data:audio/wav;base64," + data.audio_data);
    snd.play();
    setMessages((prev) => [...prev, data]);
  };

  const handleSendMessage = (e: React.KeyboardEvent<HTMLInputElement>) => {
    if (e.key === "Enter") {
      const sendData = {
        text_data: currMessage,
        timestamp: Date.now(),
      };
      SERVER.send(sendData);
      setCurrMessage("");
    }
  };

  const handleUpdateMessage = (e: React.ChangeEvent<HTMLInputElement>) =>
    setCurrMessage(e.target.value);

  useEffect(() => {
    SERVER.start();
    SERVER.receive(handleRecieveMessage);
    return () => {
      // SERVER.close();
    };
  }, []);

  return (
    <div className="mp-Chatbox">
      {messages.map((i, _) => (
        <Message key={`${i.cid}_${_}`} message={i} />
      ))}
      <div className="mp-chatInput">
        <input
          value={currMessage}
          onChange={handleUpdateMessage}
          onKeyDown={handleSendMessage}
          placeholder="Type your message here..."
        />
      </div>
    </div>
  );
};

export default Chat;
