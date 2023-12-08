###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_DestroyCursor

Free a previously-created cursor.

## Syntax

```c
void SDL_DestroyCursor(SDL_Cursor * cursor);

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

This function is available since SDL 3.0.0.

## Related Functions

* [SDL_CreateColorCursor](SDL_CreateColorCursor.md)
* [SDL_CreateCursor](SDL_CreateCursor.md)
* [SDL_CreateSystemCursor](SDL_CreateSystemCursor.md)

----
[CategoryAPI](CategoryAPI.md)
