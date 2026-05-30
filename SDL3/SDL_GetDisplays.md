# SDL_GetDisplays

Get a list of currently connected displays.

## Header File

Defined in [<SDL3/SDL_video.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_video.h)

## Syntax

```c
SDL_DisplayID * SDL_GetDisplays(int *count);
```

## Function Parameters

|       |           |                                                                        |
| ----- | --------- | ---------------------------------------------------------------------- |
| int * | **count** | a pointer filled in with the number of displays returned, may be NULL. |

## Return Value

([SDL_DisplayID](SDL_DisplayID) *) Returns a 0 terminated array of display
instance IDs or NULL on failure; call [SDL_GetError](SDL_GetError)() for
more information. This should be freed with [SDL_free](SDL_free)() when it
is no longer needed.

## Thread Safety

This function should only be called on the main thread.

## Version

This function is available since SDL 3.2.0.

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryVideo](CategoryVideo)

