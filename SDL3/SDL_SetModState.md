###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)

## Draft

**THIS PAGE IS A WORK IN PROGRESS** ... Please make edits to this page to improve it!
# SDL_SetModState

Set the current key modifier state for the keyboard.

## Syntax

```c
void SDL_SetModState(SDL_Keymod modstate);

```

## Function Parameters

|                  |                                                       |
| ---------------- | ----------------------------------------------------- |
| **modstate**     | the desired [SDL_Keymod](SDL_Keymod.md) for the keyboard |

## Remarks

The inverse of [SDL_GetModState](SDL_GetModState.md)(),
[SDL_SetModState](SDL_SetModState.md)() allows you to impose modifier key
states on your application. Simply pass your desired modifier states into
`modstate`. This value may be a bitwise, OR'd combination of
[SDL_Keymod](SDL_Keymod.md) values.

This does not change the keyboard state, only the key modifier flags that
SDL reports.

## Version

This function is available since SDL 3.0.0.

## Related Functions

* [SDL_GetModState](SDL_GetModState.md)

----
[CategoryAPI](CategoryAPI.md), [CategoryKeyboard](CategoryKeyboard.md), [CategoryDraft](CategoryDraft.md)
