###### (This is the legacy documentation for stable SDL2, the current stable version; [SDL3](https://wiki.libsdl.org/SDL3/) is the current development version.)
# SDL_GetWindowFromID

Get a window from a stored ID.

## Syntax

```c
SDL_Window * SDL_GetWindowFromID(Uint32 id);

```

## Function Parameters

|            |                      |
| ---------- | -------------------- |
| **id**     | the ID of the window |

## Return Value

Returns the window associated with `id` or NULL if it doesn't exist; call
[SDL_GetError](SDL_GetError.md)() for more information.

## Remarks

The numeric ID is what [SDL_WindowEvent](SDL_WindowEvent.md) references, and
is necessary to map these events to specific [SDL_Window](SDL_Window.md)
objects.

## Version

This function is available since SDL 2.0.0.

## Related Functions

* [SDL_GetWindowID](SDL_GetWindowID.md)

----
[CategoryAPI](CategoryAPI.md)
