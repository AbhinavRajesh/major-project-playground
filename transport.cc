#include <stdio.h>
#include <sys/types.h>
#include <sys/socket.h>

#define PORT 8080

int main() {
    struct sockaddr_in address;

    // Socket creating
    if ((sock = socket(AF_INET, SOCK_STREAM, 0)) < 0) {
        cout << "\nSocket creation error \n";
        return -1;
    }

    // Socket address conversion
    if (inet_pton(AF_INET, "127.0.0.1", &serv_addr.sin_addr) <= 0) {
        cout << "\nInvalid address / Address not supported \n";
        return -1;
    }

    // Socket connecting
    if ((client_fd = connect(sock, (struct sockaddr*)&serv_addr, sizeof(serv_addr))) < 0) {
        cout << "\nConnection Failed \n";
        return -1;
    }

    return 0;
}
