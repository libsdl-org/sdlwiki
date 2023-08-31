###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_SetWindowFocusable

Set whether the window may have input focus.

## Syntax

```c
int SDL_SetWindowFocusable(SDL_Window *window, SDL_bool focusable);

```

## Function Parameters

|                   |                                                                                            |
| ----------------- | ------------------------------------------------------------------------------------------ |
| **window**        | the window to set focusable state                                                          |
| **focusable**     | [SDL_TRUE](SDL_TRUE) to allow input focus, [SDL_FALSE](SDL_FALSE) to not allow input focus |

## Return Value

Returns 0 on success or a negative error code on failure; call
[SDL_GetError](SDL_GetError)() for more information.

## Version

This function is available since SDL 3.0.0.

----
[CategoryAPI](CategoryAPI)

