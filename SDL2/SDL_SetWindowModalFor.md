# SDL_SetWindowModalFor

Set the window as a modal for another window.

## Header File

Defined in [SDL_video.h](https://github.com/libsdl-org/SDL/blob/SDL2/include/SDL_video.h)

## Syntax

```c
int SDL_SetWindowModalFor(SDL_Window * modal_window, SDL_Window * parent_window);
```

## Function Parameters

|                            |                   |                                         |
| -------------------------- | ----------------- | --------------------------------------- |
| [SDL_Window](SDL_Window) * | **modal_window**  | the window that should be set modal.    |
| [SDL_Window](SDL_Window) * | **parent_window** | the parent window for the modal window. |

## Return Value

(int) Returns 0 on success or a negative error code on failure; call
[SDL_GetError](SDL_GetError)() for more information.

## Version

This function is available since SDL 2.0.5.

## (This is the legacy documentation for SDL2, the previous stable version; [SDL3](https://wiki.libsdl.org/SDL3/) is the current stable version.)



----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryVideo](CategoryVideo)

