###### (This function is part of SDL_net, a separate library from SDL.)
# NET_GetAddressBytes

Get the protocol-level bytes of a network address from a resolved address.

## Header File

Defined in [<SDL3_net/SDL_net.h>](https://github.com/libsdl-org/SDL_net/blob/main/include/SDL3_net/SDL_net.h)

## Syntax

```c
const void * NET_GetAddressBytes(NET_Address *address, int *num_bytes);
```

## Function Parameters

|                              |               |                                                         |
| ---------------------------- | ------------- | ------------------------------------------------------- |
| [NET_Address](NET_Address) * | **address**   | The [NET_Address](NET_Address) to query.                |
| int *                        | **num_bytes** | on return, will be set to the number of bytes returned. |

## Return Value

(const void *) Returns a pointer to bytes, or NULL on error; call
SDL_GetError() for details.

## Remarks

This data is not human-readable, is protocol-specific, and might not even
be in a specific byte order.

This is only useful for possibly hashing, to map a address to a specific
player in a game, or possibly for handing to a system-level networking API
(which is _not_ recommended; an app does this at their own risk).

Do not store these bytes for future runs of the program; there is no
promise the format won't change.

On return `*num_bytes` will hold the number of bytes provided with the
address. Since the data is not NULL-terminated, this is the only way to
determine its size; as such, this parameter must not be NULL.

Do not free or modify the returned data; it belongs to the
[NET_Address](NET_Address) that was queried, and is valid as long as the
object lives. Either make sure the address has a reference as long as you
need this or make a copy of the bytes.

This will return NULL if resolution is still in progress, or if resolution
failed. You can use [NET_GetAddressStatus](NET_GetAddressStatus)() or
[NET_WaitUntilResolved](NET_WaitUntilResolved)() to make sure resolution
has successfully completed before calling this.

A human-readable version is available in
[NET_GetAddressString](NET_GetAddressString)() and isn't any less efficient
to query than the raw bytes.

## Thread Safety

It is safe to call this function from any thread.

## Version

This function is available since SDL_net 3.0.0.

## See Also

- [NET_GetAddressString](NET_GetAddressString)
- [NET_GetAddressStatus](NET_GetAddressStatus)
- [NET_WaitUntilResolved](NET_WaitUntilResolved)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategorySDLNet](CategorySDLNet)

