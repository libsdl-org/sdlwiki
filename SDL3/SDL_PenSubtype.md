###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_PenSubtype

Pen types

## Header File

Defined in [SDL_pen.h](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_pen.h), but apps should use `#include <SDL3/SDL.h>`

## Syntax

```c
typedef enum SDL_PenSubtype
{
    SDL_PEN_TYPE_UNKNOWN = 0,
    SDL_PEN_TYPE_ERASER = 1,                  /**< Eraser */
    SDL_PEN_TYPE_PEN,                         /**< Generic pen; this is the default. */
    SDL_PEN_TYPE_PENCIL,                      /**< Pencil */
    SDL_PEN_TYPE_BRUSH,                       /**< Brush-like device */
    SDL_PEN_TYPE_AIRBRUSH,                    /**< Airbrush device that "sprays" ink */
    SDL_PEN_TYPE_LAST = SDL_PEN_TYPE_AIRBRUSH /**< Last valid pen type */
} SDL_PenSubtype;
```

## Remarks

Some pens identify as a particular type of drawing device (e.g., an
airbrush or a pencil).

## Version

This enum is available since SDL 3.0.0

----
[CategoryAPI](CategoryAPI), [CategoryAPIEnum](CategoryAPIEnum)

