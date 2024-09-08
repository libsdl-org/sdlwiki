###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_SetWindowParent

Set the window as a child of a parent window.

## Header File

Defined in [<SDL3/SDL_video.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_video.h)

## Syntax

```c
SDL_bool SDL_SetWindowParent(SDL_Window *window, SDL_Window *parent);
```

## Function Parameters

|                            |            |                                                      |
| -------------------------- | ---------- | ---------------------------------------------------- |
| [SDL_Window](SDL_Window) * | **window** | the window that should become the child of a parent. |
| [SDL_Window](SDL_Window) * | **parent** | the new parent window for the child window.          |

## Return Value

([SDL_bool](SDL_bool)) Returns [SDL_TRUE](SDL_TRUE) on success or
[SDL_FALSE](SDL_FALSE) on failure; call [SDL_GetError](SDL_GetError)() for
more information.

## Remarks

If the window is already the child of an existing window, it will be
reparented to the new owner. Setting the parent window to null unparents
the window and removes child window status.

Attempting to set the parent of a window that is currently in the modal
state will fail. Use [SDL_SetWindowModalFor](SDL_SetWindowModalFor)() to
cancel the modal status before attempting to change the parent.

Setting a parent window that is currently the sibling or descendent of the
child window results in undefined behavior.

## Version

This function is available since SDL 3.0.0.

## See Also

- [SDL_SetWindowModal](SDL_SetWindowModal)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryVideo](CategoryVideo)

