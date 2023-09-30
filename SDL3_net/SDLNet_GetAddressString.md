###### (This function is part of SDL_net, a separate library from SDL.)
# SDLNet_GetAddressString

Get a human-readable string from a resolved address.

## Syntax

```c
const char * SDLNet_GetAddressString(SDLNet_Address *address);

```

## Function Parameters

|                 |                                                |
| --------------- | ---------------------------------------------- |
| **address**     | The [SDLNet_Address](SDLNet_Address) to query. |

## Return Value

Returns a string, or NULL on error; call SDL_GetError() for details.

## Remarks

This returns a string that's "human-readable", in that it's probably a
string of numbers and symbols, like "159.203.69.7" or
"2604:a880:800:a1::71f:3001". It won't be the original hostname (like
"icculus.org"), but it's suitable for writing to a log file, etc.

Do not free or modify the returned string; it belongs to the
[SDLNet_Address](SDLNet_Address) that was queried, and is valid as long as
the object lives. Either make sure the address has a reference as long as
you need this or make a copy of the string.

This will return NULL if resolution is still in progress, or if resolution
failed. You can use [SDLNet_GetAddressStatus](SDLNet_GetAddressStatus)() or
[SDLNet_WaitUntilResolved](SDLNet_WaitUntilResolved)() to make sure
resolution has successfully completed before calling this.

## Thread Safety

It is safe to call this function from any thread.

## Version

This function is available since SDL_Net 3.0.0.

## Related Functions

* [SDLNet_GetAddressStatus](SDLNet_GetAddressStatus)
* [SDLNet_WaitUntilResolved](SDLNet_WaitUntilResolved)

----
[CategoryAPI](CategoryAPI)

