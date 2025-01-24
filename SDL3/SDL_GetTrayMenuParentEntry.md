# SDL_GetTrayMenuParentEntry

Gets the entry for which the menu is a submenu, if the current menu is a submenu.

## Header File

Defined in [<SDL3/SDL_tray.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_tray.h)

## Syntax

```c
SDL_TrayEntry* SDL_GetTrayMenuParentEntry(SDL_TrayMenu *menu);
```

## Function Parameters

|                                |          |                                             |
| ------------------------------ | -------- | ------------------------------------------- |
| [SDL_TrayMenu](SDL_TrayMenu) * | **menu** | the menu for which to get the parent entry. |

## Return Value

([SDL_TrayEntry](SDL_TrayEntry) *) Returns the parent entry, or NULL if
this menu is not a submenu.

## Remarks

Either this function or
[SDL_GetTrayMenuParentTray](SDL_GetTrayMenuParentTray)() will return
non-NULL for any given menu.

## Thread Safety

This function should be called on the thread that created the tray.

## Version

This function is available since SDL 3.2.0.

## See Also

- [SDL_CreateTraySubmenu](SDL_CreateTraySubmenu)
- [SDL_GetTrayMenuParentTray](SDL_GetTrayMenuParentTray)


## (This is the documentation for SDL3, which is the current stable version. [SDL2](https://wiki.libsdl.org/SDL2/) was the previous version!)



----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryTray](CategoryTray)

