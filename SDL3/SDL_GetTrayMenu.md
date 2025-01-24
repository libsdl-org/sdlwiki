# SDL_GetTrayMenu

Gets a previously created tray menu.

## Header File

Defined in [<SDL3/SDL_tray.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_tray.h)

## Syntax

```c
SDL_TrayMenu* SDL_GetTrayMenu(SDL_Tray *tray);
```

## Function Parameters

|                        |          |                                     |
| ---------------------- | -------- | ----------------------------------- |
| [SDL_Tray](SDL_Tray) * | **tray** | the tray entry to bind the menu to. |

## Return Value

([SDL_TrayMenu](SDL_TrayMenu) *) Returns the newly created menu.

## Remarks

You should have called [SDL_CreateTrayMenu](SDL_CreateTrayMenu)() on the
tray object. This function allows you to fetch it again later.

This function does the same thing as
[SDL_GetTraySubmenu](SDL_GetTraySubmenu)(), except that it takes a
[SDL_Tray](SDL_Tray) instead of a [SDL_TrayEntry](SDL_TrayEntry).

A menu does not need to be destroyed; it will be destroyed with the tray.

## Thread Safety

This function should be called on the thread that created the tray.

## Version

This function is available since SDL 3.2.0.

## See Also

- [SDL_CreateTray](SDL_CreateTray)
- [SDL_CreateTrayMenu](SDL_CreateTrayMenu)






----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryTray](CategoryTray)

