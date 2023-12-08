###### (This is the legacy documentation for stable SDL2, the current stable version; [SDL3](https://wiki.libsdl.org/SDL3/) is the current development version.)
# SDL_GetKeyboardState

Get a snapshot of the current state of the keyboard.

## Syntax

```c
const Uint8* SDL_GetKeyboardState(int *numkeys);

```

## Function Parameters

|                 |                                                        |
| --------------- | ------------------------------------------------------ |
| **numkeys**     | if non-NULL, receives the length of the returned array |

## Return Value

Returns a pointer to an array of key states.

## Remarks

The pointer returned is a pointer to an internal SDL array. It will be
valid for the whole lifetime of the application and should not be freed by
the caller.

A array element with a value of 1 means that the key is pressed and a value
of 0 means that it is not. Indexes into this array are obtained by using
[SDL_Scancode](SDL_Scancode.md) values.

Use [SDL_PumpEvents](SDL_PumpEvents.md)() to update the state array.

This function gives you the current state after all events have been
processed, so if a key or button has been pressed and released before you
process events, then the pressed state will never show up in the
[SDL_GetKeyboardState](SDL_GetKeyboardState.md)() calls.

Note: This function doesn't take into account whether shift has been
pressed or not.

## Version

This function is available since SDL 2.0.0.

## Related Functions

* [SDL_PumpEvents](SDL_PumpEvents.md)
* [SDL_ResetKeyboard](SDL_ResetKeyboard.md)

----
[CategoryAPI](CategoryAPI.md)
