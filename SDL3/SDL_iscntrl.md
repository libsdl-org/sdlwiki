###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_iscntrl

Report if a character is a control character.

## Syntax

```c
int SDL_iscntrl(int x);

```

## Function Parameters

|           |                           |
| --------- | ------------------------- |
| **x**     | character value to check. |

## Return Value

Returns non-zero if x falls within the character class, zero otherwise.

## Remarks

**WARNING**: Regardless of system locale, this will only treat ASCII values
0 through 0x1F, and 0x7F, as true.

## Thread Safety

It is safe to call this function from any thread.

## Version

This function is available since SDL 3.0.0.

----
[CategoryAPI](CategoryAPI)

