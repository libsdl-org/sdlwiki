###### (This is the documentation for SDL3, which is the current stable version. [SDL2](https://wiki.libsdl.org/SDL2/) was the previous version!)
# SDL_SetTrayTooltip

Updates the system tray icon's tooltip.

## Header File

Defined in [<SDL3/SDL_tray.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_tray.h)

## Syntax

```c
void SDL_SetTrayTooltip(SDL_Tray *tray, const char *tooltip);
```

## Function Parameters

|                        |             |                                                 |
| ---------------------- | ----------- | ----------------------------------------------- |
| [SDL_Tray](SDL_Tray) * | **tray**    | the tray icon to be updated.                    |
| const char *           | **tooltip** | the new tooltip in UTF-8 encoding. May be NULL. |

## Version

This function is available since SDL 3.1.8.

## See Also

- [SDL_CreateTray](SDL_CreateTray)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryTray](CategoryTray)

