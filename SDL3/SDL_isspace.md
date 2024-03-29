###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_isspace

Report if a character is whitespace.

## Syntax

```c
int SDL_isspace(int x);

```

## Function Parameters

|           |                           |
| --------- | ------------------------- |
| **x**     | character value to check. |

## Return Value

Returns non-zero if x falls within the character class, zero otherwise.

## Remarks

**WARNING**: Regardless of system locale, this will only treat the
following ASCII values as true:

- space (0x20)
- tab (0x09)
- newline (0x0A)
- vertical tab (0x0B)
- form feed (0x0C)
- return (0x0D)

## Thread Safety

It is safe to call this function from any thread.

## Version

This function is available since SDL 3.0.0.

----
[CategoryAPI](CategoryAPI)

