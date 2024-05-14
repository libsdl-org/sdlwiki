###### (This is the legacy documentation for stable SDL2, the current stable version; [SDL3](https://wiki.libsdl.org/SDL3/) is the current development version.)
# SDL_MessageBoxData

MessageBox structure containing title, text, window, etc.

## Header File

Defined in [SDL_messagebox.h](https://github.com/libsdl-org/SDL/blob/SDL2/include/SDL_messagebox.h)

## Syntax

```c
typedef struct SDL_MessageBoxData
{
    Uint32 flags;                       /**< SDL_MessageBoxFlags */
    SDL_Window *window;                 /**< Parent window, can be NULL */
    const char *title;                  /**< UTF-8 title */
    const char *message;                /**< UTF-8 message text */

    int numbuttons;
    const SDL_MessageBoxButtonData *buttons;

    const SDL_MessageBoxColorScheme *colorScheme;   /**< SDL_MessageBoxColorScheme, can be NULL to use system settings */
} SDL_MessageBoxData;
```

----
[CategoryAPI](CategoryAPI), [CategoryAPIStruct](CategoryAPIStruct), [CategoryMessagebox](CategoryMessagebox), [CategoryAPIStruct](CategoryAPIStruct), [CategoryVideo](CategoryVideo)


