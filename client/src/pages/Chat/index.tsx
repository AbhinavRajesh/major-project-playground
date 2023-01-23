import React, { useEffect, useState } from "react";
import { SERVER } from "../../infrastructure";
import Message from "./common/Message";
import "./index.css";

const Chat = () => {
  const [currMessage, setCurrMessage] = useState("");
  const [message, setMessage] = useState<string>();

  const handleStream = () => {
    SERVER.receive((data) => {
      let newFile = data;
      let base64 = "";
      let reader = new FileReader();
      reader.readAsDataURL(newFile);
      reader.onloadend = function () {
        base64 = reader.result as string;
        setMessage(base64);
      };
    });
  };

  const handleSendMessage = (e: React.KeyboardEvent<HTMLInputElement>) => {
    if (e.key === "Enter") {
      if (currMessage) {
        const sendData = {
          text_data: currMessage,
          timestamp: Date.now(),
        };
        SERVER.send(sendData);
        setCurrMessage("");
      }
    }
  };

  const handleUpdateMessage = (e: React.ChangeEvent<HTMLInputElement>) =>
    setCurrMessage(e.target.value);

  useEffect(() => {
    SERVER.start();
    handleStream();
    //
    return () => {
      // SERVER.close();
    };
  }, []);

  return (
    <div className="mp-Chatbox">
      <Message message={message} />
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
