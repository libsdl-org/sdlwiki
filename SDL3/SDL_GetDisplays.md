###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_GetDisplays

Get a list of currently connected displays.

## Header File

Defined in [<SDL3/SDL_video.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_video.h)

## Syntax

```c
const SDL_DisplayID * SDL_GetDisplays(int *count);
```

## Function Parameters

|       |           |                                                                        |
| ----- | --------- | ---------------------------------------------------------------------- |
| int * | **count** | a pointer filled in with the number of displays returned, may be NULL. |

## Return Value

(const [SDL_DisplayID](SDL_DisplayID) *) Returns a 0 terminated array of
display instance IDs or NULL on failure; call
[SDL_GetError](SDL_GetError)() for more information.

## Remarks

This returns temporary memory which will be automatically freed later, and
can be claimed with [SDL_ClaimTemporaryMemory](SDL_ClaimTemporaryMemory)().

## Version

This function is available since SDL 3.0.0.

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryVideo](CategoryVideo)

