###### (This is the documentation for SDL3, which is the current stable version. [SDL2](https://wiki.libsdl.org/SDL2/) was the previous version!)
# SDL_GetTrayEntryParent

Gets the menu contianing a certain tray entry.

## Header File

Defined in [<SDL3/SDL_tray.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_tray.h)

## Syntax

```c
SDL_TrayMenu* SDL_GetTrayEntryParent(SDL_TrayEntry *entry);
```

## Function Parameters

|                                  |           |                                             |
| -------------------------------- | --------- | ------------------------------------------- |
| [SDL_TrayEntry](SDL_TrayEntry) * | **entry** | the entry for which to get the parent menu. |

## Return Value

([SDL_TrayMenu](SDL_TrayMenu) *) Returns the parent menu.

## Version

This function is available since SDL 3.1.8.

## See Also

- [SDL_InsertTrayEntryAt](SDL_InsertTrayEntryAt)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryTray](CategoryTray)

