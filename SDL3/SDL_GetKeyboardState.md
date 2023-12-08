###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)

## Draft

**THIS PAGE IS A WORK IN PROGRESS** ... Please make edits to this page to improve it!
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

This function is available since SDL 3.0.0.

## Code Examples

```c++
const Uint8 *state = SDL_GetKeyboardState(NULL);
if (state[SDL_SCANCODE_RETURN]) {
    printf("<RETURN> is pressed.\n");
}
if (state[SDL_SCANCODE_RIGHT] && state[SDL_SCANCODE_UP]) {
    printf("Right and Up Keys Pressed.\n");
}
```

## Related Functions

* [SDL_PumpEvents](SDL_PumpEvents.md)
* [SDL_ResetKeyboard](SDL_ResetKeyboard.md)

----
[CategoryAPI](CategoryAPI.md), [CategoryKeyboard](CategoryKeyboard.md), [CategoryDraft](CategoryDraft.md)
