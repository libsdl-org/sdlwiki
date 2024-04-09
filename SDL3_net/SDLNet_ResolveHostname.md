###### (This function is part of SDL_net, a separate library from SDL.)
# SDLNet_ResolveHostname

Resolve a human-readable hostname.

## Header File

Defined in SDL_net.h

## Syntax

```c
SDLNet_Address * SDLNet_ResolveHostname(const char *host);

```

## Function Parameters

|              |                          |
| ------------ | ------------------------ |
| **host**     | The hostname to resolve. |

## Return Value

Returns A new [SDLNet_Address](SDLNet_Address) on success, NULL on error;
call SDL_GetError() for details.

## Remarks

SDL_net doesn't operate on human-readable hostnames (like "www.libsdl.org")
but on computer-readable addresses. This function converts from one to the
other. This process is known as "resolving" an address.

You can also use this to turn IP address strings (like "159.203.69.7") into
[SDLNet_Address](SDLNet_Address) objects.

Note that resolving an address is an asynchronous operation, since the
library will need to ask a server on the internet to get the information it
needs, and this can take time (and possibly fail later). This function will
not block. It either returns NULL (catastrophic failure) or an unresolved
[SDLNet_Address](SDLNet_Address). Until the address resolves, it can't be
used.

If you want to block until the resolution is finished, you can call
[SDLNet_WaitUntilResolved](SDLNet_WaitUntilResolved)(). Otherwise, you can
do a non-blocking check with
[SDLNet_GetAddressStatus](SDLNet_GetAddressStatus)().

When you are done with the returned [SDLNet_Address](SDLNet_Address), call
[SDLNet_UnrefAddress](SDLNet_UnrefAddress)() to dispose of it. You need to
do this even if resolution later fails asynchronously.

## Thread Safety

It is safe to call this function from any thread.

## Version

This function is available since SDL_Net 3.0.0.

## See Also

* [SDLNet_WaitUntilResolved](SDLNet_WaitUntilResolved)
* [SDLNet_GetAddressStatus](SDLNet_GetAddressStatus)
* [SDLNet_RefAddress](SDLNet_RefAddress)
* [SDLNet_UnrefAddress](SDLNet_UnrefAddress)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction)

