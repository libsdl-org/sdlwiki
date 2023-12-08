###### (This is the legacy documentation for stable SDL2, the current stable version; [SDL3](https://wiki.libsdl.org/SDL3/) is the current development version.)
# SDL_CreateSystemCursor

Create a system cursor.

## Syntax

```c
SDL_Cursor* SDL_CreateSystemCursor(SDL_SystemCursor id);

```

## Function Parameters

|            |                                                    |
| ---------- | -------------------------------------------------- |
| **id**     | an [SDL_SystemCursor](SDL_SystemCursor.md) enum value |

## Return Value

Returns a cursor on success or NULL on failure; call
[SDL_GetError](SDL_GetError.md)() for more information.

## Version

This function is available since SDL 2.0.0.

## Related Functions

* [SDL_FreeCursor](SDL_FreeCursor.md)

----
[CategoryAPI](CategoryAPI.md)
