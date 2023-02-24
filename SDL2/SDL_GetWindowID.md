###### (This is the legacy documentation for stable SDL2, the current stable version; [SDL3](https://wiki.libsdl.org/SDL3/) is the current development version.)
# SDL_GetWindowID

Get the numeric ID of a window.

## Syntax

```c
Uint32 SDL_GetWindowID(SDL_Window * window);

```

## Function Parameters

|                |                     |
| -------------- | ------------------- |
| **window**     | the window to query |

## Return Value

Returns the ID of the window on success or 0 on failure; call
[SDL_GetError](SDL_GetError)() for more information.

## Remarks

The numeric ID is what [SDL_WindowEvent](SDL_WindowEvent) references, and
is necessary to map these events to specific [SDL_Window](SDL_Window)
objects.

## Version

This function is available since SDL 2.0.0.

## Related Functions

* [SDL_GetWindowFromID](SDL_GetWindowFromID)

----
[CategoryAPI](CategoryAPI)

