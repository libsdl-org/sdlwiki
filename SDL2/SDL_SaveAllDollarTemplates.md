###### (This is the legacy documentation for stable SDL2, the current stable version; [SDL3](https://wiki.libsdl.org/SDL3/) is the current development version.)
# SDL_SaveAllDollarTemplates

Save all currently loaded Dollar Gesture templates.

## Header File

Defined in [SDL_gesture.h](https://github.com/libsdl-org/SDL/blob/SDL2/include/SDL_gesture.h)

## Syntax

```c
int SDL_SaveAllDollarTemplates(SDL_RWops *dst);

```

## Function Parameters

|             |                                     |
| ----------- | ----------------------------------- |
| **dst**     | a [SDL_RWops](SDL_RWops) to save to |

## Return Value

Returns the number of saved templates on success or 0 on failure; call
[SDL_GetError](SDL_GetError)() for more information.

## Version

This function is available since SDL 2.0.0.

## See Also

* [SDL_LoadDollarTemplates](SDL_LoadDollarTemplates)
* [SDL_SaveDollarTemplate](SDL_SaveDollarTemplate)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction)

