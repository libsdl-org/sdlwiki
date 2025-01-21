###### (This is the documentation for SDL3, which is the current stable version. [SDL2](https://wiki.libsdl.org/SDL2/) was the previous version!)
# SDL_SetTrayEntryEnabled

Sets whether or not an entry is enabled.

## Header File

Defined in [<SDL3/SDL_tray.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_tray.h)

## Syntax

```c
void SDL_SetTrayEntryEnabled(SDL_TrayEntry *entry, bool enabled);
```

## Function Parameters

|                                  |             |                                                       |
| -------------------------------- | ----------- | ----------------------------------------------------- |
| [SDL_TrayEntry](SDL_TrayEntry) * | **entry**   | the entry to be updated.                              |
| bool                             | **enabled** | true if the entry should be enabled; false otherwise. |

## Thread Safety

This function should be called on the thread that created the tray.

## Version

This function is available since SDL 3.2.0.

## See Also

- [SDL_GetTrayEntries](SDL_GetTrayEntries)
- [SDL_InsertTrayEntryAt](SDL_InsertTrayEntryAt)
- [SDL_GetTrayEntryEnabled](SDL_GetTrayEntryEnabled)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryTray](CategoryTray)

