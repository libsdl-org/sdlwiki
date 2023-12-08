###### (This is the legacy documentation for stable SDL2, the current stable version; [SDL3](https://wiki.libsdl.org/SDL3/) is the current development version.)
# SDL_SaveAllDollarTemplates

Save all currently loaded Dollar Gesture templates.

## Syntax

```c
int SDL_SaveAllDollarTemplates(SDL_RWops *dst);

```

## Function Parameters

|             |                                     |
| ----------- | ----------------------------------- |
| **dst**     | a [SDL_RWops](SDL_RWops.md) to save to |

## Return Value

Returns the number of saved templates on success or 0 on failure; call
[SDL_GetError](SDL_GetError.md)() for more information.

## Version

This function is available since SDL 2.0.0.

## Related Functions

* [SDL_LoadDollarTemplates](SDL_LoadDollarTemplates.md)
* [SDL_SaveDollarTemplate](SDL_SaveDollarTemplate.md)

----
[CategoryAPI](CategoryAPI.md)
