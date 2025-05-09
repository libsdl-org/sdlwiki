###### (This function is part of SDL_net, a separate library from SDL.)
# NET_ResolveHostname

Resolve a human-readable hostname.

## Header File

Defined in [<SDL3_net/SDL_net.h>](https://github.com/libsdl-org/SDL_net/blob/main/include/SDL3_net/SDL_net.h)

## Syntax

```c
NET_Address * NET_ResolveHostname(const char *host);
```

## Function Parameters

|              |          |                          |
| ------------ | -------- | ------------------------ |
| const char * | **host** | The hostname to resolve. |

## Return Value

([NET_Address](NET_Address) *) Returns A new [NET_Address](NET_Address) on
success, NULL on error; call SDL_GetError() for details.

## Remarks

SDL_net doesn't operate on human-readable hostnames (like `www.libsdl.org`
but on computer-readable addresses. This function converts from one to the
other. This process is known as "resolving" an address.

You can also use this to turn IP address strings (like "159.203.69.7") into
[NET_Address](NET_Address) objects.

Note that resolving an address is an asynchronous operation, since the
library will need to ask a server on the internet to get the information it
needs, and this can take time (and possibly fail later). This function will
not block. It either returns NULL (catastrophic failure) or an unresolved
[NET_Address](NET_Address). Until the address resolves, it can't be used.

If you want to block until the resolution is finished, you can call
[NET_WaitUntilResolved](NET_WaitUntilResolved)(). Otherwise, you can do a
non-blocking check with [NET_GetAddressStatus](NET_GetAddressStatus)().

When you are done with the returned [NET_Address](NET_Address), call
[NET_UnrefAddress](NET_UnrefAddress)() to dispose of it. You need to do
this even if resolution later fails asynchronously.

## Thread Safety

It is safe to call this function from any thread.

## Version

This function is available since SDL_Net 3.0.0.

## See Also

- [NET_WaitUntilResolved](NET_WaitUntilResolved)
- [NET_GetAddressStatus](NET_GetAddressStatus)
- [NET_RefAddress](NET_RefAddress)
- [NET_UnrefAddress](NET_UnrefAddress)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategorySDLNet](CategorySDLNet)

