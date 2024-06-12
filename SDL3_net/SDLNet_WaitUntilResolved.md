###### (This function is part of SDL_net, a separate library from SDL.)
# SDLNet_WaitUntilResolved

Block until an address is resolved.

## Header File

Defined in [<SDL3_net/SDL_net.h>](https://github.com/libsdl-org/SDL_net/blob/main/include/SDL3_net/SDL_net.h)

## Syntax

```c
int SDLNet_WaitUntilResolved(SDLNet_Address *address, Sint32 timeout);
```

## Function Parameters

|                                    |             |                                                                                                                      |
| ---------------------------------- | ----------- | -------------------------------------------------------------------------------------------------------------------- |
| [SDLNet_Address](SDLNet_Address) * | **address** | The [SDLNet_Address](SDLNet_Address) object to wait on.                                                              |
| Sint32                             | **timeout** | Number of milliseconds to wait for resolution to complete. -1 to wait indefinitely, 0 to check once without waiting. |

## Return Value

(int) Returns 1 if successfully resolved, -1 if resolution failed, 0 if
still resolving (this function timed out without resolution); if -1, call
SDL_GetError() for details.

## Remarks

The [SDLNet_Address](SDLNet_Address) objects returned by
[SDLNet_ResolveHostname](SDLNet_ResolveHostname) take time to do their
work, so it is does so _asynchronously_ instead of making your program wait
an indefinite amount of time.

However, if you want your program to sleep until the address resolution is
complete, you can call this function.

This function takes a timeout value, represented in milliseconds, of how
long to wait for resolution to complete. Specifying a timeout of -1
instructs the library to wait indefinitely, and a timeout of 0 just checks
the current status and returns immediately (and is functionally equivalent
to calling [SDLNet_GetAddressStatus](SDLNet_GetAddressStatus)).

Resolution can fail after some time (DNS server took awhile to reply that
the hostname isn't recognized, etc), so be sure to check the result of this
function instead of assuming it worked!

Once an address is successfully resolved, it can be used to connect to the
host represented by the address.

If you don't want your program to block, you can call
[SDLNet_GetAddressStatus](SDLNet_GetAddressStatus) from time to time until
you get a non-zero result.

## Thread Safety

It is safe to call this function from any thread, and several threads can
block on the same address simultaneously.

## Version

This function is available since SDL_Net 3.0.0.

## See Also

- [SDLNet_GetAddressStatus](SDLNet_GetAddressStatus)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction)

