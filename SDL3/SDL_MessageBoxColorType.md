###### (This is the documentation for SDL3, which is the current stable version. [SDL2](https://wiki.libsdl.org/SDL2/) was the previous version!)
# SDL_MessageBoxColorType

An enumeration of indices inside the colors array of [SDL_MessageBoxColorScheme](SDL_MessageBoxColorScheme).

## Header File

Defined in [<SDL3/SDL_messagebox.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_messagebox.h)

## Syntax

```c
typedef enum SDL_MessageBoxColorType
{
    SDL_MESSAGEBOX_COLOR_BACKGROUND,
    SDL_MESSAGEBOX_COLOR_TEXT,
    SDL_MESSAGEBOX_COLOR_BUTTON_BORDER,
    SDL_MESSAGEBOX_COLOR_BUTTON_BACKGROUND,
    SDL_MESSAGEBOX_COLOR_BUTTON_SELECTED,
    SDL_MESSAGEBOX_COLOR_COUNT                    /**< Size of the colors array of SDL_MessageBoxColorScheme. */
} SDL_MessageBoxColorType;
```

----
[CategoryAPI](CategoryAPI), [CategoryAPIEnum](CategoryAPIEnum), [CategoryMessagebox](CategoryMessagebox)

