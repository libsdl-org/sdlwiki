###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_ScreenKeyboardShown

Check whether the screen keyboard is shown for given window.

## Syntax

```c
SDL_bool SDL_ScreenKeyboardShown(SDL_Window *window);

```

## Function Parameters

|                |                                                        |
| -------------- | ------------------------------------------------------ |
| **window**     | the window for which screen keyboard should be queried |

## Return Value

Returns [SDL_TRUE](SDL_TRUE) if screen keyboard is shown or
[SDL_FALSE](SDL_FALSE) if not.

## Version

This function is available since SDL 3.0.0.

## Related Functions

* [SDL_HasScreenKeyboardSupport](SDL_HasScreenKeyboardSupport)

----
[CategoryAPI](CategoryAPI)

