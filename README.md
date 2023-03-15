# Major Project

## _Topic: A System for Multiuser and Multiplayer support for Web based Virtual Reality_

## Abstract

There is an absence of multiplayer and multiuser support in WebXR. The project is about creating a system for multiuser and multiplayer support in web based virtual reality. The project solves this problem by creating a networking layer on top of WebXR that would allow other developers to easily integrate the proposed system into their products. The project helps to create a virtual environment enabling people to change the environment as per need. The proposed system is designed for low latency applications like collaborative workflows, massive open world games etc.

## How we plan to implement?

- [x] Create a websocket server-client application using python for backend and HTML-JS for frontend. Websocket API was used
- [x] Upgrade the websocket server for multi client communication.
- [x] Create a communication between multiple clients where the keystrokes of each client would get updated for each user.
- [x] Conference hall using Three js
- [ ] Create avatar
- [ ] Streaming using 
- [ ] Multiplayer support - detect other users coordinates
- [ ] Seat Sitting - Sit on a seat which ever he chooses to
- [ ] Voice channel 

## Setup steps

- [docs/setup.md](./docs/setup.md)

## Compile

```sh
g++ -I /usr/include/boost -pthread source/server.cc -o server.out
```

## Run

```sh
./server.out
```

## References

Mozilla Websocket API Docs
https://developer.mozilla.org/en-US/docs/Web/API/WebSockets_API

Mozilla WebXR Device API
https://developer.mozilla.org/en-US/docs/Web/API/WebXR_Device_API
