###### (This is the legacy documentation for stable SDL2, the current stable version; [SDL3](https://wiki.libsdl.org/SDL3/) is the current development version.)
# SDL_SaveDollarTemplate

Save a currently loaded Dollar Gesture template.

## Syntax

```c
int SDL_SaveDollarTemplate(SDL_GestureID gestureId,SDL_RWops *dst);

```

## Function Parameters

|                   |                                     |
| ----------------- | ----------------------------------- |
| **gestureId**     | a gesture id                        |
| **dst**           | a [SDL_RWops](SDL_RWops.md) to save to |

## Return Value

Returns 1 on success or 0 on failure; call [SDL_GetError](SDL_GetError.md)()
for more information.

## Version

This function is available since SDL 2.0.0.

## Related Functions

* [SDL_LoadDollarTemplates](SDL_LoadDollarTemplates.md)
* [SDL_SaveAllDollarTemplates](SDL_SaveAllDollarTemplates.md)

----
[CategoryAPI](CategoryAPI.md)
