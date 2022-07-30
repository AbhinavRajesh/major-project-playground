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
    return 0;
}
