###### (This is the legacy documentation for stable SDL2, the current stable version; [SDL3](https://wiki.libsdl.org/SDL3/) is the current development version.)
# SDL_FreeCursor

Free a previously-created cursor.

## Syntax

```c
void SDL_FreeCursor(SDL_Cursor * cursor);

```

## Function Parameters

|                |                    |
| -------------- | ------------------ |
| **cursor**     | the cursor to free |

## Remarks

Use this function to free cursor resources created with
[SDL_CreateCursor](SDL_CreateCursor.md)(),
[SDL_CreateColorCursor](SDL_CreateColorCursor.md)() or
[SDL_CreateSystemCursor](SDL_CreateSystemCursor.md)().

## Version

This function is available since SDL 2.0.0.

## Related Functions

* [SDL_CreateColorCursor](SDL_CreateColorCursor.md)
* [SDL_CreateCursor](SDL_CreateCursor.md)
* [SDL_CreateSystemCursor](SDL_CreateSystemCursor.md)

----
[CategoryAPI](CategoryAPI.md)
