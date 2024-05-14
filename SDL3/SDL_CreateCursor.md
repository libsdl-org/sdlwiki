###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_CreateCursor

Create a cursor using the specified bitmap data and mask (in MSB format).

## Header File

Defined in [<SDL3/SDL_mouse.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_mouse.h)

## Syntax

```c
SDL_Cursor* SDL_CreateCursor(const Uint8 * data,
                             const Uint8 * mask,
                             int w, int h, int hot_x,
                             int hot_y);

```

## Function Parameters

|               |                                                                                                           |
| ------------- | --------------------------------------------------------------------------------------------------------- |
| **data**      | the color value for each pixel of the cursor                                                              |
| **mask**      | the mask value for each pixel of the cursor                                                               |
| **w**         | the width of the cursor                                                                                   |
| **h**         | the height of the cursor                                                                                  |
| **hot_x**     | the x-axis offset from the left of the cursor image to the mouse x position, in the range of 0 to `w` - 1 |
| **hot_y**     | the y-axis offset from the top of the cursor image to the mouse y position, in the range of 0 to `h` - 1  |

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
[SDL_DestroyCursor](SDL_DestroyCursor)().

If you want to have a color cursor, or create your cursor from an
[SDL_Surface](SDL_Surface), you should use
[SDL_CreateColorCursor](SDL_CreateColorCursor)(). Alternately, you can hide
the cursor and draw your own as part of your game's rendering, but it will
be bound to the framerate.

Also, [SDL_CreateSystemCursor](SDL_CreateSystemCursor)() is available,
which provides several readily-available system cursors to pick from.

## Version

This function is available since SDL 3.0.0.

## Code Examples

```c
/* Stolen from the mailing list */
/* Creates a new mouse cursor from an XPM */


/* XPM */
static const char *arrow[] = {
  /* width height num_colors chars_per_pixel */
  "    32    32        3            1",
  /* colors */
  "X c #000000",
  ". c #ffffff",
  "  c None",
  /* pixels */
  "X                               ",
  "XX                              ",
  "X.X                             ",
  "X..X                            ",
  "X...X                           ",
  "X....X                          ",
  "X.....X                         ",
  "X......X                        ",
  "X.......X                       ",
  "X........X                      ",
  "X.....XXXXX                     ",
  "X..X..X                         ",
  "X.X X..X                        ",
  "XX  X..X                        ",
  "X    X..X                       ",
  "     X..X                       ",
  "      X..X                      ",
  "      X..X                      ",
  "       XX                       ",
  "                                ",
  "                                ",
  "                                ",
  "                                ",
  "                                ",
  "                                ",
  "                                ",
  "                                ",
  "                                ",
  "                                ",
  "                                ",
  "                                ",
  "                                ",
  "0,0"
};

SDL_Cursor *init_system_cursor(const char *image[])
{
  int i, row, col;
  Uint8 data[4*32];
  Uint8 mask[4*32];
  int hot_x, hot_y;

  i = -1;
  for (row=0; row<32; ++row) {
    for (col=0; col<32; ++col) {
      if (col % 8) {
        data[i] <<= 1;
        mask[i] <<= 1;
      } else {
        ++i;
        data[i] = mask[i] = 0;
      }
      switch (image[4+row][col]) {
        case 'X':
          data[i] |= 0x01;
          mask[i] |= 0x01;
          break;
        case '.':
          mask[i] |= 0x01;
          break;
        case ' ':
          break;
      }
    }
  }
  sscanf(image[4+row], "%d,%d", &hot_x, &hot_y);
  return SDL_CreateCursor(data, mask, 32, 32, hot_x, hot_y);
}
```

## See Also

- [SDL_CreateColorCursor](SDL_CreateColorCursor)
- [SDL_CreateSystemCursor](SDL_CreateSystemCursor)
- [SDL_DestroyCursor](SDL_DestroyCursor)
- [SDL_SetCursor](SDL_SetCursor)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryMouse](CategoryMouse)

