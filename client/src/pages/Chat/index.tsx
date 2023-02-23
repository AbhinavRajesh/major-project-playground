import React, { useEffect, useRef, useState } from "react";
import { SERVER } from "../../infrastructure";
import Message from "./common/Message";
// import dashjs from "dashjs";
import "./index.css";

const Chat = () => {
  const [currMessage, setCurrMessage] = useState("");
  const [message, setMessage] = useState<string>("");
  const videoRef = useRef(null);

  const handleStream = () => {
    SERVER.receive((data) => {
      setMessage("");
      URL.revokeObjectURL(message);
      console.log({ data });
      const url = URL.createObjectURL(data);
      setMessage(url);
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
    return () => {
      // SERVER.close();
    };
    // eslint-disable-next-line
  }, []);

  return (
    <div className="mp-Chatbox">
      <Message message={message} />
      <video
        ref={videoRef}
        id="video-player"
        // src={"http://localhost:5000/video.mpd"}
        controls
      ></video>
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
