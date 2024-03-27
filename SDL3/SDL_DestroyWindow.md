###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_DestroyWindow

Destroy a window.

## Syntax

```c
void SDL_DestroyWindow(SDL_Window *window);

```

## Function Parameters

|                |                       |
| -------------- | --------------------- |
| **window**     | the window to destroy |

## Remarks

If the window has an associated [SDL_Renderer](SDL_Renderer), it will be
implicitly destroyed as well.

If `window` is NULL, this function will return immediately after setting
the SDL error message to "Invalid window". See
[SDL_GetError](SDL_GetError)().

## Version

This function is available since SDL 3.0.0.

## Related Functions

* [SDL_CreatePopupWindow](SDL_CreatePopupWindow)
* [SDL_CreateWindow](SDL_CreateWindow)
* [SDL_CreateWindowWithProperties](SDL_CreateWindowWithProperties)

----
[CategoryAPI](CategoryAPI), [CategoryVideo](CategoryVideo)


