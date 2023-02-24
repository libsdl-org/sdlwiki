###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_GetWindowData

Retrieve the data pointer associated with a window.

## Syntax

```c
void* SDL_GetWindowData(SDL_Window *window, const char *name);

```

## Function Parameters

|                |                         |
| -------------- | ----------------------- |
| **window**     | the window to query     |
| **name**       | the name of the pointer |

## Return Value

Returns the value associated with `name`.

## Version

This function is available since SDL 3.0.0.

## Related Functions

* [SDL_SetWindowData](SDL_SetWindowData)

----
[CategoryAPI](CategoryAPI), [CategoryVideo](CategoryVideo)


