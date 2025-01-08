###### (This is the documentation for SDL3, which is the current stable version. [SDL2](https://wiki.libsdl.org/SDL2/) was the previous version!)
# SDL_CreateTrayMenu

Create a menu for a system tray.

## Header File

Defined in [<SDL3/SDL_tray.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_tray.h)

## Syntax

```c
SDL_TrayMenu* SDL_CreateTrayMenu(SDL_Tray *tray);
```

## Function Parameters

|                        |          |                               |
| ---------------------- | -------- | ----------------------------- |
| [SDL_Tray](SDL_Tray) * | **tray** | the tray to bind the menu to. |

## Return Value

([SDL_TrayMenu](SDL_TrayMenu) *) Returns the newly created menu.

## Remarks

This should be called at most once per tray icon.

This function does the same thing as
[SDL_CreateTraySubmenu](SDL_CreateTraySubmenu)(), except that it takes a
[SDL_Tray](SDL_Tray) instead of a [SDL_TrayEntry](SDL_TrayEntry).

A menu does not need to be destroyed; it will be destroyed with the tray.

## Version

This function is available since SDL 3.1.8.

## See Also

- [SDL_CreateTray](SDL_CreateTray)
- [SDL_GetTrayMenu](SDL_GetTrayMenu)
- [SDL_GetTrayMenuParentTray](SDL_GetTrayMenuParentTray)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryTray](CategoryTray)

