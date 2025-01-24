# SDL_GetKeyboardState

Get a snapshot of the current state of the keyboard.

## Header File

Defined in [<SDL3/SDL_keyboard.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_keyboard.h)

## Syntax

```c
const bool * SDL_GetKeyboardState(int *numkeys);
```

## Function Parameters

|       |             |                                                         |
| ----- | ----------- | ------------------------------------------------------- |
| int * | **numkeys** | if non-NULL, receives the length of the returned array. |

## Return Value

(const bool *) Returns a pointer to an array of key states.

## Remarks

The pointer returned is a pointer to an internal SDL array. It will be
valid for the whole lifetime of the application and should not be freed by
the caller.

A array element with a value of true means that the key is pressed and a
value of false means that it is not. Indexes into this array are obtained
by using [SDL_Scancode](SDL_Scancode) values.

Use [SDL_PumpEvents](SDL_PumpEvents)() to update the state array.

This function gives you the current state after all events have been
processed, so if a key or button has been pressed and released before you
process events, then the pressed state will never show up in the
[SDL_GetKeyboardState](SDL_GetKeyboardState)() calls.

Note: This function doesn't take into account whether shift has been
pressed or not.

## Thread Safety

It is safe to call this function from any thread.

## Version

This function is available since SDL 3.2.0.

## See Also

- [SDL_PumpEvents](SDL_PumpEvents)
- [SDL_ResetKeyboard](SDL_ResetKeyboard)


## (This is the documentation for SDL3, which is the current stable version. [SDL2](https://wiki.libsdl.org/SDL2/) was the previous version!)



----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryKeyboard](CategoryKeyboard)

