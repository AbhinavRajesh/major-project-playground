import React from "react";

const Message = ({ message }: { message: string | undefined }) => {
  if (message)
    return (
      <div className="mp-chatMessage">
        <img alt="stream" src={message} />
      </div>
    );
  return <p>No media stream available</p>;
};

export default Message;
