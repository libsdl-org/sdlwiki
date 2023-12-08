###### (This function is part of SDL_net, a separate library from SDL.)
# SDLNet_CheckSockets

Check a socket set for data availability.

## Syntax

```c
int SDLNet_CheckSockets(SDLNet_SocketSet set, Uint32 timeout);

```

## Function Parameters

|                 |                                                                                                                              |
| --------------- | ---------------------------------------------------------------------------------------------------------------------------- |
| **set**         | the socket set to check for ready sockets.                                                                                   |
| **timeout**     | the time to wait in milliseconds for new data to arrive. A timeout of zero checks for new data and returns without blocking. |

## Return Value

Returns the number of sockets ready for reading, or -1 if there was an
error with the select() system call.

## Remarks

This function checks to see if data is available for reading on the given
set of sockets. If 'timeout' is 0, it performs a quick poll, otherwise the
function returns when either data is available for reading, or the timeout
in milliseconds has elapsed, whichever occurs first.

## Version

This function is available since SDL_net 2.0.0.

----
[CategoryAPI](CategoryAPI.md)
