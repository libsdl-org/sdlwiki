###### (This is the documentation for SDL3, which is the current stable version. [SDL2](https://wiki.libsdl.org/SDL2/) was the previous version!)
# SDL_GetDisplayName

Get the name of a display in UTF-8 encoding.

## Header File

Defined in [<SDL3/SDL_video.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_video.h)

## Syntax

```c
const char * SDL_GetDisplayName(SDL_DisplayID displayID);
```

## Function Parameters

|                                |               |                                          |
| ------------------------------ | ------------- | ---------------------------------------- |
| [SDL_DisplayID](SDL_DisplayID) | **displayID** | the instance ID of the display to query. |

## Return Value

(const char *) Returns the name of a display or NULL on failure; call
[SDL_GetError](SDL_GetError)() for more information.

## Version

This function is available since SDL 3.0.0.

## See Also

- [SDL_GetDisplays](SDL_GetDisplays)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryVideo](CategoryVideo)

