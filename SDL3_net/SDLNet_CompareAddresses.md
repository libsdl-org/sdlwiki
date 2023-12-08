###### (This function is part of SDL_net, a separate library from SDL.)
# SDLNet_CompareAddresses

Compare two [SDLNet_Address](SDLNet_Address.md) objects.

## Syntax

```c
int SDLNet_CompareAddresses(const SDLNet_Address *a, const SDLNet_Address *b);

```

## Function Parameters

|           |                            |
| --------- | -------------------------- |
| **a**     | first address to compare.  |
| **b**     | second address to compare. |

## Return Value

Returns -1 if `a` is "less than" `b`, 1 if "greater than", 0 if equal.

## Remarks

This compares two addresses, returning a value that is useful for qsort (or
SDL_qsort).

## Thread Safety

It is safe to call this function from any thread.

## Version

This function is available since SDL_Net 3.0.0.

----
[CategoryAPI](CategoryAPI.md)
