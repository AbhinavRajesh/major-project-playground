#define _WIN32_WINNT 0x501
#include <iostream>
#include <string>
#include <WS2tcpip.h>
using namespace std;

#define PORT 8080

int main()
{
    WSADATA wsData;
    WORD ver = MAKEWORD(2, 2);

    if (WSAStartup(ver, &wsData) != 0)
    {
        cout << "Winsock initialization error";
        exit(1);
    }

    SOCKET serverSocket = socket(AF_INET, SOCK_STREAM, 0);
    if (serverSocket == INVALID_SOCKET)
    {
        printf("\nFAILED: Socket creation");
        exit(EXIT_FAILURE);
    }
    else
    {
        printf("\nSUCCESS: Socket creation");
    }

    sockaddr_in serverInfo;

    serverInfo.sin_family = AF_INET;
    serverInfo.sin_port = htons(PORT);
    serverInfo.sin_addr.S_un.S_addr = INADDR_ANY;

    // Binding Socket to PORT
    if (bind(serverSocket, (sockaddr *)&serverInfo, sizeof(serverInfo)))
    {
        printf("\nFAILED: Socket binding");
        exit(EXIT_FAILURE);
    }
    else
    {
        printf("\nSUCCESS: Socket binding");
    }

    // Listening
    if (listen(serverSocket, 3) < 0)
    {
        printf("\nFAILED: Socket listening");
        exit(EXIT_FAILURE);
    }
    else
    {
        printf("\nSUCCESS: Socket listening");
    }

    sockaddr_in clientInfo;
    int clientSize = sizeof(clientInfo);
    char hbuf[NI_MAXHOST], sbuf[NI_MAXSERV];

    SOCKET clientSocket = accept(serverSocket, (sockaddr *)&clientInfo, &clientSize);
    int s = getnameinfo((sockaddr *)&clientInfo, sizeof clientInfo, hbuf, sizeof hbuf,
                        sbuf, sizeof sbuf,
                        NI_NUMERICHOST | NI_NUMERICSERV);
    if (s == 0)
    {
        printf("\nSUCCESS: Socket acception: %s:%s", hbuf, sbuf);
    }
    else
    {
        printf("\nFAILED: Socket acception");
    }

    char buf[4096]; // 4Mb

    cout << "\n\nWaiting for client to send the message...\n";

    do
    {
        // Make sure the user has typed in something
        ZeroMemory(buf, 4096);
        int recvResult = recv(clientSocket, buf, 4096, 0);
        if (recvResult > 0)
        {
            string response = string(buf, 0, recvResult);
            // Echo response to console
            printf("\nSUCCESS: Recieving from client: %d bytes", recvResult);
            // printf("\n%s", response.c_str());
            // Return the same message back
            int sendResult = send(clientSocket, "Hi, I'm server", response.size() + 1, 0);
            if (sendResult == SOCKET_ERROR)
            {
                printf("\nFAILED: Sending to client: %d", WSAGetLastError());
                closesocket(clientSocket);
                WSACleanup();
                return 0;
            }
            else
            {
                printf("\nSUCCESS: Sending to client: %d bytes", sendResult);
            }
        }
        else if (recvResult != 0)
        {
            printf("\nFAILED: Recieving from client: %d", WSAGetLastError());
            closesocket(clientSocket);
            WSACleanup();
            return 0;
        }
    } while (true);

    closesocket(clientSocket);
    WSACleanup();
    return 0;
}