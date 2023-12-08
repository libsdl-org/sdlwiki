###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_SetWindowData

Associate an arbitrary named pointer with a window.

## Syntax

```c
void* SDL_SetWindowData(SDL_Window *window, const char *name, void *userdata);

```

## Function Parameters

|                  |                                          |
| ---------------- | ---------------------------------------- |
| **window**       | the window to associate with the pointer |
| **name**         | the name of the pointer                  |
| **userdata**     | the associated pointer                   |

## Return Value

Returns the previous value associated with `name`.

## Remarks

`name` is case-sensitive.

## Version

This function is available since SDL 3.0.0.

## Related Functions

* [SDL_GetWindowData](SDL_GetWindowData.md)

----
[CategoryAPI](CategoryAPI.md), [CategoryVideo](CategoryVideo.md)
