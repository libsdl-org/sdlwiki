###### (This is the legacy documentation for stable SDL2, the current stable version; [SDL3](https://wiki.libsdl.org/SDL3/) is the current development version.)
# SDL_ShowCursor

Toggle whether or not the cursor is shown.

## Header File

Defined in [SDL_mouse.h](https://github.com/libsdl-org/SDL/blob/SDL2/include/SDL_mouse.h)

## Syntax

```c
int SDL_ShowCursor(int toggle);

```

## Function Parameters

|                |                                                                                                                                                                  |
| -------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **toggle**     | [`SDL_ENABLE`](SDL_ENABLE) to show the cursor, [`SDL_DISABLE`](SDL_DISABLE) to hide it, [`SDL_QUERY`](SDL_QUERY) to query the current state without changing it. |

## Return Value

Returns [`SDL_ENABLE`](SDL_ENABLE) if the cursor is shown, or
[`SDL_DISABLE`](SDL_DISABLE) if the cursor is hidden, or a negative error
code on failure; call [SDL_GetError](SDL_GetError)() for more information.

## Remarks

The cursor starts off displayed but can be turned off. Passing
[`SDL_ENABLE`](SDL_ENABLE) displays the cursor and passing
[`SDL_DISABLE`](SDL_DISABLE) hides it.

The current state of the mouse cursor can be queried by passing
[`SDL_QUERY`](SDL_QUERY); either [`SDL_DISABLE`](SDL_DISABLE) or
[`SDL_ENABLE`](SDL_ENABLE) will be returned.

## Version

This function is available since SDL 2.0.0.

## See Also

- [SDL_CreateCursor](SDL_CreateCursor)
- [SDL_SetCursor](SDL_SetCursor)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryMouse](CategoryMouse)

