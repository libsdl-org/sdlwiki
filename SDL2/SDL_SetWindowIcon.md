###### (This is the legacy documentation for stable SDL2, the current stable version; [SDL3](https://wiki.libsdl.org/SDL3/) is the current development version.)
# SDL_SetWindowIcon

Set the icon for a window.

## Syntax

```c
void SDL_SetWindowIcon(SDL_Window * window,
                       SDL_Surface * icon);

```

## Function Parameters

|                |                                                                            |
| -------------- | -------------------------------------------------------------------------- |
| **window**     | the window to change                                                       |
| **icon**       | an [SDL_Surface](SDL_Surface.md) structure containing the icon for the window |

## Version

This function is available since SDL 2.0.0.

----
[CategoryAPI](CategoryAPI.md)
