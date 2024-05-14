###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_isprint

Report if a character is "printable".

## Header File

Defined in [<SDL3/SDL_stdinc.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_stdinc.h)

## Syntax

```c
int SDL_isprint(int x);

```

## Function Parameters

|           |                           |
| --------- | ------------------------- |
| **x**     | character value to check. |

## Return Value

Returns non-zero if x falls within the character class, zero otherwise.

## Remarks

Be advised that "printable" has a definition that goes back to text
terminals from the dawn of computing, making this a sort of special case
function that is not suitable for Unicode (or most any) text management.

**WARNING**: Regardless of system locale, this will only treat ASCII values
' ' (0x20) through '~' (0x7E) as true.

## Thread Safety

It is safe to call this function from any thread.

## Version

This function is available since SDL 3.0.0.

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryStdinc](CategoryStdinc)

