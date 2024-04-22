###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_MessageBoxFlags

[SDL_MessageBox](SDL_MessageBox) flags.

## Header File

Defined in [SDL_messagebox.h](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_messagebox.h)

## Syntax

```c
typedef enum SDL_MessageBoxFlags
{
    SDL_MESSAGEBOX_ERROR                 = 0x00000010,   /**< error dialog */
    SDL_MESSAGEBOX_WARNING               = 0x00000020,   /**< warning dialog */
    SDL_MESSAGEBOX_INFORMATION           = 0x00000040,   /**< informational dialog */
    SDL_MESSAGEBOX_BUTTONS_LEFT_TO_RIGHT = 0x00000080,   /**< buttons placed left to right */
    SDL_MESSAGEBOX_BUTTONS_RIGHT_TO_LEFT = 0x00000100    /**< buttons placed right to left */
} SDL_MessageBoxFlags;
```

## Remarks

If supported will display warning icon, etc.

## Version

This enum is available since SDL 3.0.0.

----
[CategoryAPI](CategoryAPI), [CategoryAPIEnum](CategoryAPIEnum)

