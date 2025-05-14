###### (This function is part of SDL_net, a separate library from SDL.)
# NET_CompareAddresses

Compare two [NET_Address](NET_Address) objects.

## Header File

Defined in [<SDL3_net/SDL_net.h>](https://github.com/libsdl-org/SDL_net/blob/main/include/SDL3_net/SDL_net.h)

## Syntax

```c
int NET_CompareAddresses(const NET_Address *a, const NET_Address *b);
```

## Function Parameters

|                                    |       |                            |
| ---------------------------------- | ----- | -------------------------- |
| const [NET_Address](NET_Address) * | **a** | first address to compare.  |
| const [NET_Address](NET_Address) * | **b** | second address to compare. |

## Return Value

(int) Returns -1 if `a` is "less than" `b`, 1 if "greater than", 0 if
equal.

## Remarks

This compares two addresses, returning a value that is useful for qsort (or
SDL_qsort).

## Thread Safety

It is safe to call this function from any thread.

## Version

This function is available since SDL_net 3.0.0.

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategorySDLNet](CategorySDLNet)

