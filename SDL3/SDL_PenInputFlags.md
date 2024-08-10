###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_PenInputFlags

Pen input flags, as reported by various pen events' `pen_state` field.

## Header File

Defined in [<SDL3/SDL_pen.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_pen.h)

## Syntax

```c
typedef Uint32 SDL_PenInputFlags;
#define SDL_PEN_INPUT_DOWN       (1u << 0)  /**< & to see if pen is pressed down */
#define SDL_PEN_INPUT_BUTTON_1   (1u << 1)  /**< & to see if button 1 is pressed */
#define SDL_PEN_INPUT_BUTTON_2   (1u << 2)  /**< & to see if button 2 is pressed */
#define SDL_PEN_INPUT_BUTTON_3   (1u << 3)  /**< & to see if button 3 is pressed */
#define SDL_PEN_INPUT_BUTTON_4   (1u << 4)  /**< & to see if button 4 is pressed */
#define SDL_PEN_INPUT_BUTTON_5   (1u << 5)  /**< & to see if button 5 is pressed */
#define SDL_PEN_INPUT_ERASER_TIP (1u << 30) /**< & to see if eraser tip is used */
```

## Version

This datatype is available since SDL 3.0.0.

----
[CategoryAPI](CategoryAPI), [CategoryAPIDatatype](CategoryAPIDatatype), [CategoryPen](CategoryPen)

