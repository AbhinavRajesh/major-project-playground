#include<iostream>
#include<string>
#include<WS2tcpip.h>

using namespace std;

#define PORT 8080

int main() {
    WSADATA wsData;
    WORD ver = MAKEWORD(2, 2);

    if (WSAStartup(ver, &wsData) != 0) {
        cout << "Winsock initialization error";
        exit(1);
    }

    SOCKET socket_server = socket(AF_INET, SOCK_STREAM, 0);
    if (socket_server == INVALID_SOCKET) {
        cout << "Couldn\"t create socket";
        exit(1);
    }

    sockaddr_in address;

    address.sin_family = AF_INET;
    address.sin_port = htons(PORT);
    address.sin_addr.S_un.S_addr = INADDR_ANY;

    // Binding Socket to PORT
    if (bind(socket_server, (sockaddr *)&address, sizeof(address))) 
    {
        printf("\nFAILED: Socket binding");
        exit(EXIT_FAILURE);
    }
    else
    {
        printf("\nSUCCESS: Socket binding");
    }

    // Listening
    if (listen(socket_server, 3) < 0)
    {
        printf("\nFAILED: Socket listening");
        exit(EXIT_FAILURE);
    }
    else
    {
        printf("\nSUCCESS: Socket listening");
    }


    sockaddr_in client;
    int clientSize = sizeof(client);

    SOCKET clientSocket = accept(socket_server, (sockaddr *)&client, &clientSize);

    char buf[4096]; // 4Mb

    cout << "Waiting for client to send the message...";

	do
	{
        // Make sure the user has typed in something
        ZeroMemory(buf, 4096);
        int bytesReceived = recv(clientSocket, buf, 4096, 0);
        if (bytesReceived > 0)
        {
            string response = string(buf, 0, bytesReceived);
            // Echo response to console
            cout << "SERVER> " << response << endl;
            // Return the same message back
            int sendResult = send(clientSocket, response.c_str(), response.size() + 1, 0);
            if (sendResult != SOCKET_ERROR) {
                cout << "Error while sending back the data!";
            }
        }
	} while (true);

    closesocket(clientSocket);

    WSACleanup();

    return 0;

}