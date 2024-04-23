###### (This is the legacy documentation for stable SDL2, the current stable version; [SDL3](https://wiki.libsdl.org/SDL3/) is the current development version.)
# SDL_MessageBoxFlags

[SDL_MessageBox](SDL_MessageBox) flags.

## Header File

Defined in [SDL_messagebox.h](https://github.com/libsdl-org/SDL/blob/SDL2/include/SDL_messagebox.h)

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

----
[CategoryAPI](CategoryAPI), [CategoryAPIEnum](CategoryAPIEnum), [CategoryEnum](CategoryEnum), [CategoryVideo](CategoryVideo)


