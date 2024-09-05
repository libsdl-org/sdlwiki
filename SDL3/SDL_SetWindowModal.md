###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_SetWindowModal

Toggle the state of the window as modal.

## Header File

Defined in [<SDL3/SDL_video.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_video.h)

## Syntax

```c
SDL_bool SDL_SetWindowModal(SDL_Window *window, SDL_bool modal);
```

## Function Parameters

|                            |            |                                                                                          |
| -------------------------- | ---------- | ---------------------------------------------------------------------------------------- |
| [SDL_Window](SDL_Window) * | **window** | the window on which to set the modal state.                                              |
| [SDL_bool](SDL_bool)       | **modal**  | [SDL_TRUE](SDL_TRUE) to toggle modal status on, [SDL_FALSE](SDL_FALSE) to toggle it off. |

## Return Value

([SDL_bool](SDL_bool)) Returns [SDL_TRUE](SDL_TRUE) on success or
[SDL_FALSE](SDL_FALSE) on failure; call [SDL_GetError](SDL_GetError)() for
more information.

## Remarks

To enable modal status on a window, the window must currently be the child
window of a parent, or toggling modal status on will fail.

## Version

This function is available since SDL 3.0.0.

## See Also

- [SDL_SetWindowParent](SDL_SetWindowParent)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryVideo](CategoryVideo)

