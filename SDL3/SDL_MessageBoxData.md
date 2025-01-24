# SDL_MessageBoxData

MessageBox structure containing title, text, window, etc.

## Header File

Defined in [<SDL3/SDL_messagebox.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_messagebox.h)

## Syntax

```c
typedef struct SDL_MessageBoxData
{
    SDL_MessageBoxFlags flags;
    SDL_Window *window;                 /**< Parent window, can be NULL */
    const char *title;                  /**< UTF-8 title */
    const char *message;                /**< UTF-8 message text */

    int numbuttons;
    const SDL_MessageBoxButtonData *buttons;

    const SDL_MessageBoxColorScheme *colorScheme;   /**< SDL_MessageBoxColorScheme, can be NULL to use system settings */
} SDL_MessageBoxData;
```

## Version

This struct is available since SDL 3.2.0.





----
[CategoryAPI](CategoryAPI), [CategoryAPIStruct](CategoryAPIStruct), [CategoryMessagebox](CategoryMessagebox)

