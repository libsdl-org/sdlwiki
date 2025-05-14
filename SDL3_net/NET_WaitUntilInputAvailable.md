###### (This function is part of SDL_net, a separate library from SDL.)
# NET_WaitUntilInputAvailable

Block on multiple sockets until at least one has data available.

## Header File

Defined in [<SDL3_net/SDL_net.h>](https://github.com/libsdl-org/SDL_net/blob/main/include/SDL3_net/SDL_net.h)

## Syntax

```c
int NET_WaitUntilInputAvailable(void **vsockets, int numsockets, Sint32 timeout);
```

## Function Parameters

|         |                |                                                                                                                             |
| ------- | -------------- | --------------------------------------------------------------------------------------------------------------------------- |
| void ** | **vsockets**   | an array of pointers to various objects that can be waited on, each cast to a void pointer.                                 |
| int     | **numsockets** | the number of pointers in the `vsockets` array.                                                                             |
| Sint32  | **timeout**    | Number of milliseconds to wait for new input to become available. -1 to wait indefinitely, 0 to check once without waiting. |

## Return Value

(int) Returns the number of items that have new input, or -1 on error.

## Remarks

This is a complex function that most apps won't need, but it could be used
to implement a more efficient server or i/o thread in some cases.

This allows you to give it a list of objects and wait for new input to
become available on any of them. The calling thread is put to sleep until
such a time.

The following things can be specified in the `vsockets` array, cast to
`void *`:

- [NET_Server](NET_Server) (reports new input when a connection is ready to
  be accepted with [NET_AcceptClient](NET_AcceptClient)())
- [NET_StreamSocket](NET_StreamSocket) (reports new input when the remote
  end has sent more bytes of data to be read with
  [NET_ReadFromStreamSocket](NET_ReadFromStreamSocket)).
- [NET_DatagramSocket](NET_DatagramSocket) (reports new input when a new
  packet arrives that can be read with
  [NET_ReceiveDatagram](NET_ReceiveDatagram)).

This function takes a timeout value, represented in milliseconds, of how
long to wait for resolution to complete. Specifying a timeout of -1
instructs the library to wait indefinitely, and a timeout of 0 just checks
the current status and returns immediately.

This returns the number of items that have new input, but it does not tell
you which ones; since access to them is non-blocking, you can just try to
read from each of them and see which are ready. If nothing is ready and the
timeout is reached, this returns zero. On error, this returns -1.

## Thread Safety

You should not operate on the same socket from multiple threads at the same
time without supplying a serialization mechanism. However, different
threads may access different sockets at the same time without problems.

## Version

This function is available since SDL_net 3.0.0.

## See Also

- [NET_CreateDatagramSocket](NET_CreateDatagramSocket)
- [NET_SendDatagram](NET_SendDatagram)
- [NET_ReceiveDatagram](NET_ReceiveDatagram)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategorySDLNet](CategorySDLNet)

