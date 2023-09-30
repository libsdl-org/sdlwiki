###### (This function is part of SDL_net, a separate library from SDL.)
# SDLNet_GetAddressStatus

Check if an address is resolved, without blocking.

## Syntax

```c
int SDLNet_GetAddressStatus(SDLNet_Address *address);

```

## Function Parameters

|                 |                                                |
| --------------- | ---------------------------------------------- |
| **address**     | The [SDLNet_Address](SDLNet_Address) to query. |

## Return Value

Returns 1 if successfully resolved, -1 if resolution failed, 0 if still
resolving; if -1, call SDL_GetError() for details.

## Remarks

The [SDLNet_Address](SDLNet_Address) objects returned by
[SDLNet_ResolveHostname](SDLNet_ResolveHostname) take time to do their
work, so it is does so _asynchronously_ instead of making your program wait
an indefinite amount of time.

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

This function is available since SDL_Net 3.0.0.

## Related Functions

* [SDLNet_WaitUntilResolved](SDLNet_WaitUntilResolved)

----
[CategoryAPI](CategoryAPI)

