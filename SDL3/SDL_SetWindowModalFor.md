###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_SetWindowModalFor

Set the window as a modal to a parent window.

## Header File

Defined in [<SDL3/SDL_video.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_video.h)

## Syntax

```c
int SDL_SetWindowModalFor(SDL_Window *modal_window, SDL_Window *parent_window);
```

## Function Parameters

|                            |                   |                                        |
| -------------------------- | ----------------- | -------------------------------------- |
| [SDL_Window](SDL_Window) * | **modal_window**  | the window that should be set modal    |
| [SDL_Window](SDL_Window) * | **parent_window** | the parent window for the modal window |

## Return Value

(int) Returns 0 on success or a negative error code on failure; call
[SDL_GetError](SDL_GetError)() for more information.

## Remarks

If the window is already modal to an existing window, it will be reparented
to the new owner. Setting the parent window to null unparents the modal
window and removes modal status.

Setting a window as modal to a parent that is a descendent of the modal
window results in undefined behavior.

## Version

This function is available since SDL 3.0.0.

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryVideo](CategoryVideo)

