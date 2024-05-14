###### (This is the legacy documentation for stable SDL2, the current stable version; [SDL3](https://wiki.libsdl.org/SDL3/) is the current development version.)
# SDL_CreateColorCursor

Create a color cursor.

## Header File

Defined in [SDL_mouse.h](https://github.com/libsdl-org/SDL/blob/SDL2/include/SDL_mouse.h)

## Syntax

```c
SDL_Cursor* SDL_CreateColorCursor(SDL_Surface *surface,
                                  int hot_x,
                                  int hot_y);

```

## Function Parameters

|                 |                                                                       |
| --------------- | --------------------------------------------------------------------- |
| **surface**     | an [SDL_Surface](SDL_Surface) structure representing the cursor image |
| **hot_x**       | the x position of the cursor hot spot                                 |
| **hot_y**       | the y position of the cursor hot spot                                 |

## Return Value

Returns the new cursor on success or NULL on failure; call
[SDL_GetError](SDL_GetError)() for more information.

## Version

This function is available since SDL 2.0.0.

## See Also

- [SDL_CreateCursor](SDL_CreateCursor)
- [SDL_FreeCursor](SDL_FreeCursor)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryMouse](CategoryMouse)

