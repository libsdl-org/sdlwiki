###### (This is the legacy documentation for stable SDL2, the current stable version; [SDL3](https://wiki.libsdl.org/SDL3/) is the current development version.)
# SDL_SetWindowsMessageHook

Set a callback for every Windows message, run before TranslateMessage().

## Header File

Defined in [SDL_system.h](https://github.com/libsdl-org/SDL/blob/SDL2/include/SDL_system.h)

## Syntax

```c
void SDL_SetWindowsMessageHook(SDL_WindowsMessageHook callback, void *userdata);

```

## Function Parameters

|                  |                                                                        |
| ---------------- | ---------------------------------------------------------------------- |
| **callback**     | The [SDL_WindowsMessageHook](SDL_WindowsMessageHook) function to call. |
| **userdata**     | a pointer to pass to every iteration of `callback`                     |

## Version

This function is available since SDL 2.0.4.

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction)

