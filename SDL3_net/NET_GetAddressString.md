###### (This function is part of SDL_net, a separate library from SDL.)
# NET_GetAddressString

Get a human-readable string from a resolved address.

## Header File

Defined in [<SDL3_net/SDL_net.h>](https://github.com/libsdl-org/SDL_net/blob/main/include/SDL3_net/SDL_net.h)

## Syntax

```c
const char * NET_GetAddressString(NET_Address *address);
```

## Function Parameters

|                              |             |                                          |
| ---------------------------- | ----------- | ---------------------------------------- |
| [NET_Address](NET_Address) * | **address** | The [NET_Address](NET_Address) to query. |

## Return Value

(const char *) Returns a string, or NULL on error; call SDL_GetError() for
details.

## Remarks

This returns a string that's "human-readable", in that it's probably a
string of numbers and symbols, like "159.203.69.7" or
"2604:a880:800:a1::71f:3001". It won't be the original hostname (like
"icculus.org"), but it's suitable for writing to a log file, etc.

Do not free or modify the returned string; it belongs to the
[NET_Address](NET_Address) that was queried, and is valid as long as the
object lives. Either make sure the address has a reference as long as you
need this or make a copy of the string.

This will return NULL if resolution is still in progress, or if resolution
failed. You can use [NET_GetAddressStatus](NET_GetAddressStatus)() or
[NET_WaitUntilResolved](NET_WaitUntilResolved)() to make sure resolution
has successfully completed before calling this.

## Thread Safety

It is safe to call this function from any thread.

## Version

This function is available since SDL_net 3.0.0.

## See Also

- [NET_GetAddressStatus](NET_GetAddressStatus)
- [NET_WaitUntilResolved](NET_WaitUntilResolved)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategorySDLNet](CategorySDLNet)

