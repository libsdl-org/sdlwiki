###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_CursorVisible

Return whether the cursor is currently being shown.

## Syntax

```c
SDL_bool SDL_CursorVisible(void);

```

## Return Value

Returns [`SDL_TRUE`](SDL_TRUE) if the cursor is being shown, or
[`SDL_FALSE`](SDL_FALSE) if the cursor is hidden.

## Version

This function is available since SDL 3.0.0.

## Related Functions

* [SDL_HideCursor](SDL_HideCursor)
* [SDL_ShowCursor](SDL_ShowCursor)

----
[CategoryAPI](CategoryAPI)

