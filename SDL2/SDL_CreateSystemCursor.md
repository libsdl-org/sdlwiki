###### (This is the legacy documentation for stable SDL2, the current stable version; [SDL3](https://wiki.libsdl.org/SDL3/) is the current development version.)
# SDL_CreateSystemCursor

Create a system cursor.

## Header File

Defined in [SDL_mouse.h](https://github.com/libsdl-org/SDL/blob/SDL2/include/SDL_mouse.h)

## Syntax

```c
SDL_Cursor* SDL_CreateSystemCursor(SDL_SystemCursor id);
```

## Function Parameters

|                                      |        |                                                     |
| ------------------------------------ | ------ | --------------------------------------------------- |
| [SDL_SystemCursor](SDL_SystemCursor) | **id** | an [SDL_SystemCursor](SDL_SystemCursor) enum value. |

## Return Value

([SDL_Cursor](SDL_Cursor) *) Returns a cursor on success or NULL on
failure; call [SDL_GetError](SDL_GetError)() for more information.

## Version

This function is available since SDL 2.0.0.

## See Also

- [SDL_FreeCursor](SDL_FreeCursor)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryMouse](CategoryMouse)

