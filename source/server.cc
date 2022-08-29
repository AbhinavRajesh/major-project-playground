#include <boost/beast/core.hpp>
#include <boost/beast/websocket.hpp>
#include <iostream>
#include <string>
#include <thread>

namespace beast = boost::beast;         // from <boost/beast.hpp>
namespace http = beast::http;           // from <boost/beast/http.hpp>
namespace websocket = beast::websocket; // from <boost/beast/websocket.hpp>
namespace net = boost::asio;            // from <boost/asio.hpp>
using tcp = boost::asio::ip::tcp;       // from <boost/asio/ip/tcp.hpp>

int main()
{

    auto const address = net::ip::make_address("127.0.0.1");
    auto const port = static_cast<unsigned short>(std::atoi("8080"));

    net::io_context ioc{1};
    tcp::acceptor acceptor{ioc, {address, port}};

    std::cout << "Started server" <<std::endl;

    while (1)
    {

        tcp::socket socket{ioc};
        acceptor.accept(socket);

        std::cout << "socket connection accepted" << std::endl;

        std::thread{[q{std::move(socket)}]()
                    {
                        websocket::stream<tcp::socket> ws{std::move(const_cast<tcp::socket &>(q))};

                        ws.accept();

                        while (1)
                        {
                            try
                            {
                                beast::flat_buffer buffer;

                                ws.read(buffer);

                                auto out = beast::buffers_to_string(buffer.cdata());

                                std::cout << out << std::endl;

                                // Send "pong" as response when "ping" is sent, else return whatever the user sends
                                if (out == "ping")
                                {
                                    ws.write(net::buffer(std::string("pong")));
                                }
                                else
                                {
                                    ws.write(buffer.data());
                                }
                            }
                            catch (beast::system_error const &se)
                            {
                                if (se.code() != websocket::error::closed)
                                {
                                    std::cout << se.code().message() << std::endl;
                                    break;
                                }
                            }
                        }
                    }}
            .detach();
    }

    return 0;
}
