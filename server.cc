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
    char server_hbuf[NI_MAXHOST], server_sbuf[NI_MAXSERV];

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
    char client_hbuf[NI_MAXHOST], client_sbuf[NI_MAXSERV];

    SOCKET clientSocket = accept(serverSocket, (sockaddr *)&clientInfo, &clientSize);

    if (clientSocket == INVALID_SOCKET)
    {
        printf("\nFAILED: Socket acception");
    }
    else
    {
        printf("\nSUCCESS: Socket acception");
    }

    // printing server info
    if (getnameinfo((sockaddr *)&serverInfo, sizeof(serverInfo),
                    server_hbuf, sizeof(server_hbuf),
                    server_sbuf, sizeof(server_sbuf),
                    NI_NUMERICHOST | NI_NUMERICSERV) == 0)
    {
        printf("\n\nSERVER @ %s:%s", server_hbuf, server_sbuf);
    }
    // printing client
    if (getnameinfo((sockaddr *)&clientInfo, sizeof(clientInfo),
                    client_hbuf, sizeof(client_hbuf),
                    client_sbuf, sizeof(client_sbuf),
                    NI_NUMERICHOST | NI_NUMERICSERV) == 0)
    {
        printf("\nCLIENT @ %s:%s", client_hbuf, client_sbuf);
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