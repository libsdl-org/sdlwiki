# SDL_CreateTray

Create an icon to be placed in the operating system's tray, or equivalent.

## Header File

Defined in [<SDL3/SDL_tray.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_tray.h)

## Syntax

```c
SDL_Tray * SDL_CreateTray(SDL_Surface *icon, const char *tooltip);
```

## Function Parameters

|                              |             |                                                                                                                          |
| ---------------------------- | ----------- | ------------------------------------------------------------------------------------------------------------------------ |
| [SDL_Surface](SDL_Surface) * | **icon**    | a surface to be used as icon. May be NULL.                                                                               |
| const char *                 | **tooltip** | a tooltip to be displayed when the mouse hovers the icon in UTF-8 encoding. Not supported on all platforms. May be NULL. |

## Return Value

([SDL_Tray](SDL_Tray) *) Returns The newly created system tray icon.

## Remarks

Many platforms advise not using a system tray unless persistence is a
necessary feature. Avoid needlessly creating a tray icon, as the user may
feel like it clutters their interface.

Using tray icons require the video subsystem.

## Thread Safety

This function should only be called on the main thread.

## Version

This function is available since SDL 3.2.0.

## See Also

- [SDL_CreateTrayMenu](SDL_CreateTrayMenu)
- [SDL_GetTrayMenu](SDL_GetTrayMenu)
- [SDL_DestroyTray](SDL_DestroyTray)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryTray](CategoryTray)

