###### (This is the legacy documentation for stable SDL2, the current stable version; [SDL3](https://wiki.libsdl.org/SDL3/) is the current development version.)
# SDL_GetModState

Get the current key modifier state for the keyboard.

## Syntax

```c
SDL_Keymod SDL_GetModState(void);

```

## Return Value

Returns an OR'd combination of the modifier keys for the keyboard. See
[SDL_Keymod](SDL_Keymod.md) for details.

## Version

This function is available since SDL 2.0.0.

## Related Functions

* [SDL_GetKeyboardState](SDL_GetKeyboardState.md)
* [SDL_SetModState](SDL_SetModState.md)

----
[CategoryAPI](CategoryAPI.md)
