###### (This is the legacy documentation for stable SDL2, the current stable version; [SDL3](https://wiki.libsdl.org/SDL3/) is the current development version.)
# SDL_FreeCursor

Free a previously-created cursor.

## Header File

Defined in [SDL_mouse.h](https://github.com/libsdl-org/SDL/blob/SDL2/include/SDL_mouse.h)

## Syntax

```c
void SDL_FreeCursor(SDL_Cursor * cursor);
```

## Function Parameters

|                            |            |                    |
| -------------------------- | ---------- | ------------------ |
| [SDL_Cursor](SDL_Cursor) * | **cursor** | the cursor to free |

## Remarks

Use this function to free cursor resources created with
[SDL_CreateCursor](SDL_CreateCursor)(),
[SDL_CreateColorCursor](SDL_CreateColorCursor)() or
[SDL_CreateSystemCursor](SDL_CreateSystemCursor)().

## Version

This function is available since SDL 2.0.0.

## See Also

- [SDL_CreateColorCursor](SDL_CreateColorCursor)
- [SDL_CreateCursor](SDL_CreateCursor)
- [SDL_CreateSystemCursor](SDL_CreateSystemCursor)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryMouse](CategoryMouse)

