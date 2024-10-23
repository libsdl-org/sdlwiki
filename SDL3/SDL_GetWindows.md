###### (This is the documentation for SDL3, which is the current stable version. [SDL2](https://wiki.libsdl.org/SDL2/) was the previous version!)
# SDL_GetWindows

Get a list of valid windows.

## Header File

Defined in [<SDL3/SDL_video.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_video.h)

## Syntax

```c
SDL_Window ** SDL_GetWindows(int *count);
```

## Function Parameters

|       |           |                                                                       |
| ----- | --------- | --------------------------------------------------------------------- |
| int * | **count** | a pointer filled in with the number of windows returned, may be NULL. |

## Return Value

([SDL_Window](SDL_Window) **) Returns a NULL terminated array of
[SDL_Window](SDL_Window) pointers or NULL on failure; call
[SDL_GetError](SDL_GetError)() for more information. This is a single
allocation that should be freed with [SDL_free](SDL_free)() when it is no
longer needed.

## Version

This function is available since SDL 3.1.3.

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryVideo](CategoryVideo)

