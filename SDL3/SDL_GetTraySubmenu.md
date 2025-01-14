###### (This is the documentation for SDL3, which is the current stable version. [SDL2](https://wiki.libsdl.org/SDL2/) was the previous version!)
# SDL_GetTraySubmenu

Gets a previously created tray entry submenu.

## Header File

Defined in [<SDL3/SDL_tray.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_tray.h)

## Syntax

```c
SDL_TrayMenu* SDL_GetTraySubmenu(SDL_TrayEntry *entry);
```

## Function Parameters

|                                  |           |                                     |
| -------------------------------- | --------- | ----------------------------------- |
| [SDL_TrayEntry](SDL_TrayEntry) * | **entry** | the tray entry to bind the menu to. |

## Return Value

([SDL_TrayMenu](SDL_TrayMenu) *) Returns the newly created menu.

## Remarks

You should have called [SDL_CreateTraySubmenu](SDL_CreateTraySubmenu)() on
the entry object. This function allows you to fetch it again later.

This function does the same thing as [SDL_GetTrayMenu](SDL_GetTrayMenu)(),
except that it takes a [SDL_TrayEntry](SDL_TrayEntry) instead of a
[SDL_Tray](SDL_Tray).

A menu does not need to be destroyed; it will be destroyed with the tray.

## Version

This function is available since SDL 3.1.8.

## See Also

- [SDL_InsertTrayEntryAt](SDL_InsertTrayEntryAt)
- [SDL_CreateTraySubmenu](SDL_CreateTraySubmenu)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryTray](CategoryTray)

