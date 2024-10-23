###### (This is the documentation for SDL3, which is the current stable version. [SDL2](https://wiki.libsdl.org/SDL2/) was the previous version!)
# SDL_SetWindowParent

Set the window as a child of a parent window.

## Header File

Defined in [<SDL3/SDL_video.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_video.h)

## Syntax

```c
bool SDL_SetWindowParent(SDL_Window *window, SDL_Window *parent);
```

## Function Parameters

|                            |            |                                                      |
| -------------------------- | ---------- | ---------------------------------------------------- |
| [SDL_Window](SDL_Window) * | **window** | the window that should become the child of a parent. |
| [SDL_Window](SDL_Window) * | **parent** | the new parent window for the child window.          |

## Return Value

(bool) Returns true on success or false on failure; call
[SDL_GetError](SDL_GetError)() for more information.

## Remarks

If the window is already the child of an existing window, it will be
reparented to the new owner. Setting the parent window to NULL unparents
the window and removes child window status.

If a parent window is hidden or destroyed, the operation will be
recursively applied to child windows. Child windows hidden with the parent
that did not have their hidden status explicitly set will be restored when
the parent is shown.

Attempting to set the parent of a window that is currently in the modal
state will fail. Use [SDL_SetWindowModal](SDL_SetWindowModal)() to cancel
the modal status before attempting to change the parent.

Popup windows cannot change parents and attempts to do so will fail.

Setting a parent window that is currently the sibling or descendent of the
child window results in undefined behavior.

## Version

This function is available since SDL 3.1.3.

## See Also

- [SDL_SetWindowModal](SDL_SetWindowModal)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryVideo](CategoryVideo)

