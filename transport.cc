#include <iostream>

#include <winsock.h> // For Windows
// #include <WS2tcpip.h>

// #include <sys/socket.h> // For Linux
#include <sys/types.h>

using namespace std;

#define PORT 8080

int main()
{
    struct sockaddr_in address
    {
    };

    // Creating socket file descriptor
    // IPV4 - TCP
    int server_fd = socket(AF_INET, SOCK_STREAM, 0);
    if (server_fd == 0)
    {
        printf("\nFAILED: Socket file descriptor creation");
        exit(EXIT_FAILURE);
    }
    else
    {
        printf("\nSUCCESS: Socket file descriptor creation");
    }

    address.sin_family = AF_INET;
    address.sin_addr.S_un.S_addr = INADDR_ANY;
    address.sin_port = htons(PORT);

    // Binding Socket to PORT
    if (bind(server_fd, (struct sockaddr *)&address, sizeof(address)) < 0)
    {
        printf("\nFAILED: Socket binding");
        exit(EXIT_FAILURE);
    }
    else
    {
        printf("\nSUCCESS: Socket binding");
    }

    // Listening
    if (listen(server_fd, 3) < 0)
    {
        printf("\nFAILED: Socket listening");
        exit(EXIT_FAILURE);
    }
    else
    {
        printf("\nSUCCESS: Socket listening");
    }

    return 0;
}
