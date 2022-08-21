## Linux

- Packages to be installed

  - libboost-all-dev
  - libpthread-stubs0-dev

  ```sh
  sudo apt-get install libboost-all-dev libpthread-stubs0-dev
  ```

- Command to run

  ```sh
  g++ -I /usr/include/boost -pthread source/server.cc
  ```

- Chrome Extensions
  1. Smart Websocket Client - (https://chrome.google.com/webstore/detail/smart-websocket-client/omalebghpgejjiaoknljcfmglgbpocdp/)
