###### (This is the documentation for SDL3, which is the current stable version. [SDL2](https://wiki.libsdl.org/SDL2/) was the previous version!)
# SDL_GetTrayMenuParentTray

Gets the tray for which this menu is the first-level menu, if the current menu isn't a submenu.

## Header File

Defined in [<SDL3/SDL_tray.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_tray.h)

## Syntax

```c
SDL_Tray* SDL_GetTrayMenuParentTray(SDL_TrayMenu *menu);
```

## Function Parameters

|                                |          |                                                 |
| ------------------------------ | -------- | ----------------------------------------------- |
| [SDL_TrayMenu](SDL_TrayMenu) * | **menu** | the menu for which to get the parent enttrayry. |

## Return Value

([SDL_Tray](SDL_Tray) *) Returns the parent tray, or NULL if this menu is a
submenu.

## Remarks

Either this function or
[SDL_GetTrayMenuParentEntry](SDL_GetTrayMenuParentEntry)() will return
non-NULL for any given menu.

## Thread Safety

This function should be called on the thread that created the tray.

## Version

This function is available since SDL 3.2.0.

## See Also

- [SDL_CreateTrayMenu](SDL_CreateTrayMenu)
- [SDL_GetTrayMenuParentEntry](SDL_GetTrayMenuParentEntry)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryTray](CategoryTray)

