import React from "react";
import { ClientData } from "../../../common/types";

const Message = ({ message }: { message: ClientData }) => {
  return (
    <div className="mp-chatMessage">
      <p>Client {message.cname}</p>
      <span> &gt;&gt; </span>
      <p>{message.text_data}</p>
    </div>
  );
};

export default Message;
