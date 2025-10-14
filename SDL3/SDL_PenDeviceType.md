# SDL_PenDeviceType

An enum that describes the type of a pen device.

## Header File

Defined in [<SDL3/SDL_pen.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_pen.h)

## Syntax

```c
typedef enum SDL_PenDeviceType
{
    SDL_PEN_DEVICE_TYPE_INVALID = -1, /**< Not a valid pen device. */
    SDL_PEN_DEVICE_TYPE_UNKNOWN,      /**< Don't know specifics of this pen. */
    SDL_PEN_DEVICE_TYPE_DIRECT,       /**< Pen touches display. */
    SDL_PEN_DEVICE_TYPE_INDIRECT      /**< Pen touches something that isn't the display. */
} SDL_PenDeviceType;
```

## Remarks

A "direct" device is a pen that touches a graphic display (like an Apple
Pencil on an iPad's screen). "Indirect" devices touch an external tablet
surface that is connected to the machine but is not a display (like a
lower-end Wacom tablet connected over USB).

Apps may use this information to decide if they should draw a cursor; if
the pen is touching the screen directly, a cursor doesn't make sense and
can be in the way, but becomes necessary for indirect devices to know where
on the display they are interacting.

## Version

This enum is available since SDL 3.4.0.

----
[CategoryAPI](CategoryAPI), [CategoryAPIEnum](CategoryAPIEnum), [CategoryPen](CategoryPen)

