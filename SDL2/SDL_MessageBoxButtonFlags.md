###### (This is the legacy documentation for stable SDL2, the current stable version; [SDL3](https://wiki.libsdl.org/SDL3/) is the current development version.)
# SDL_MessageBoxButtonFlags

Flags for [SDL_MessageBoxButtonData](SDL_MessageBoxButtonData).

## Header File

Defined in [SDL_messagebox.h](https://github.com/libsdl-org/SDL/blob/SDL2/include/SDL_messagebox.h)

## Syntax

```c
typedef enum SDL_MessageBoxButtonFlags
{
    SDL_MESSAGEBOX_BUTTON_RETURNKEY_DEFAULT = 0x00000001,  /**< Marks the default button when return is hit */
    SDL_MESSAGEBOX_BUTTON_ESCAPEKEY_DEFAULT = 0x00000002   /**< Marks the default button when escape is hit */
} SDL_MessageBoxButtonFlags;
```

----
[CategoryAPI](CategoryAPI), [CategoryAPIEnum](CategoryAPIEnum), [CategoryMessagebox](CategoryMessagebox), [CategoryVideo](CategoryVideo)


