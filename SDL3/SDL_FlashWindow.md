###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_FlashWindow

Request a window to demand attention from the user.

## Header File

Defined in [<SDL3/SDL_video.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_video.h)

## Syntax

```c
SDL_bool SDL_FlashWindow(SDL_Window *window, SDL_FlashOperation operation);
```

## Function Parameters

|                                          |               |                           |
| ---------------------------------------- | ------------- | ------------------------- |
| [SDL_Window](SDL_Window) *               | **window**    | the window to be flashed. |
| [SDL_FlashOperation](SDL_FlashOperation) | **operation** | the operation to perform. |

## Return Value

([SDL_bool](SDL_bool)) Returns [SDL_TRUE](SDL_TRUE) on success or
[SDL_FALSE](SDL_FALSE) on failure; call [SDL_GetError](SDL_GetError)() for
more information.

## Version

This function is available since SDL 3.0.0.

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryVideo](CategoryVideo)

