###### (This function is part of SDL_net, a separate library from SDL.)
# NET_GetAddressStatus

Check if an address is resolved, without blocking.

## Header File

Defined in [<SDL3_net/SDL_net.h>](https://github.com/libsdl-org/SDL_net/blob/main/include/SDL3_net/SDL_net.h)

## Syntax

```c
int NET_GetAddressStatus(NET_Address *address);
```

## Function Parameters

|                              |             |                                          |
| ---------------------------- | ----------- | ---------------------------------------- |
| [NET_Address](NET_Address) * | **address** | The [NET_Address](NET_Address) to query. |

## Return Value

(int) Returns 1 if successfully resolved, -1 if resolution failed, 0 if
still resolving; if -1, call SDL_GetError() for details.

## Remarks

The [NET_Address](NET_Address) objects returned by
[NET_ResolveHostname](NET_ResolveHostname) take time to do their work, so
it does so _asynchronously_ instead of making your program wait an
indefinite amount of time.

This function allows you to check the progress of that work without
blocking.

Resolution can fail after some time (DNS server took awhile to reply that
the hostname isn't recognized, etc), so be sure to check the result of this
function instead of assuming it worked because it's non-zero!

Once an address is successfully resolved, it can be used to connect to the
host represented by the address.

## Thread Safety

It is safe to call this function from any thread.

## Version

This function is available since SDL_net 3.0.0.

## See Also

- [NET_WaitUntilResolved](NET_WaitUntilResolved)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategorySDLNet](CategorySDLNet)

