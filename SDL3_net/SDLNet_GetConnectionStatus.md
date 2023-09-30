###### (This function is part of SDL_net, a separate library from SDL.)
# SDLNet_GetConnectionStatus

Check if a stream socket is connected, without blocking.

## Syntax

```c
int SDLNet_GetConnectionStatus(SDLNet_StreamSocket *sock);

```

## Function Parameters

|              |                             |
| ------------ | --------------------------- |
| **sock**     | the stream socket to query. |

## Return Value

Returns 1 if successfully connected, -1 if connection failed, 0 if still
connecting; if -1, call SDL_GetError() for details.

## Remarks

The [SDLNet_StreamSocket](SDLNet_StreamSocket) objects returned by
[SDLNet_CreateClient](SDLNet_CreateClient) take time to do negotiate a
connection to a server, so it is does so _asynchronously_ instead of making
your program wait an indefinite amount of time.

This function allows you to check the progress of that work without
blocking.

Connection can fail after some time (server took a while to respond, and
then rejected the connection), so be sure to check the result of this
function instead of assuming it worked because it's non-zero!

Once a connection is successfully made, the stream socket can be used to
send and receive data with the server.

Note that if the connection succeeds, but later the connection is dropped,
this will still report the connection as successful, as it only deals with
the initial asynchronous work of getting connected; you'll know the
connection dropped later when your reads and writes report failures.

## Thread Safety

You should not operate on the same socket from multiple threads at the same
time without supplying a serialization mechanism. However, different
threads may access different sockets at the same time without problems.

## Version

This function is available since SDL_Net 3.0.0.

## Related Functions

* [SDLNet_WaitUntilConnected](SDLNet_WaitUntilConnected)

----
[CategoryAPI](CategoryAPI)

