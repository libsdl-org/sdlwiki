###### (This is the legacy documentation for stable SDL2, the current stable version; [SDL3](https://wiki.libsdl.org/SDL3/) is the current development version.)
# SDL_CreateCursor

Create a cursor using the specified bitmap data and mask (in MSB format).

## Header File

Defined in [SDL_mouse.h](https://github.com/libsdl-org/SDL/blob/SDL2/include/SDL_mouse.h)

## Syntax

```c
SDL_Cursor* SDL_CreateCursor(const Uint8 * data,
                             const Uint8 * mask,
                             int w, int h, int hot_x,
                             int hot_y);

```

## Function Parameters

|               |                                                                                                  |
| ------------- | ------------------------------------------------------------------------------------------------ |
| **data**      | the color value for each pixel of the cursor                                                     |
| **mask**      | the mask value for each pixel of the cursor                                                      |
| **w**         | the width of the cursor                                                                          |
| **h**         | the height of the cursor                                                                         |
| **hot_x**     | the X-axis location of the upper left corner of the cursor relative to the actual mouse position |
| **hot_y**     | the Y-axis location of the upper left corner of the cursor relative to the actual mouse position |

## Return Value

Returns a new cursor with the specified parameters on success or NULL on
failure; call [SDL_GetError](SDL_GetError)() for more information.

## Remarks

`mask` has to be in MSB (Most Significant Bit) format.

The cursor width (`w`) must be a multiple of 8 bits.

The cursor is created in black and white according to the following:

- data=0, mask=1: white
- data=1, mask=1: black
- data=0, mask=0: transparent
- data=1, mask=0: inverted color if possible, black if not.

Cursors created with this function must be freed with
[SDL_FreeCursor](SDL_FreeCursor)().

If you want to have a color cursor, or create your cursor from an
[SDL_Surface](SDL_Surface), you should use
[SDL_CreateColorCursor](SDL_CreateColorCursor)(). Alternately, you can hide
the cursor and draw your own as part of your game's rendering, but it will
be bound to the framerate.

Also, since SDL 2.0.0, [SDL_CreateSystemCursor](SDL_CreateSystemCursor)()
is available, which provides twelve readily available system cursors to
pick from.

## Version

This function is available since SDL 2.0.0.

## See Also

- [SDL_FreeCursor](SDL_FreeCursor)
- [SDL_SetCursor](SDL_SetCursor)
- [SDL_ShowCursor](SDL_ShowCursor)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction)

