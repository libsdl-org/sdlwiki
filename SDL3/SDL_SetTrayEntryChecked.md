###### (This is the documentation for SDL3, which is the current stable version. [SDL2](https://wiki.libsdl.org/SDL2/) was the previous version!)
# SDL_SetTrayEntryChecked

Sets whether or not an entry is checked.

## Header File

Defined in [<SDL3/SDL_tray.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_tray.h)

## Syntax

```c
void SDL_SetTrayEntryChecked(SDL_TrayEntry *entry, bool checked);
```

## Function Parameters

|                                  |             |                                                       |
| -------------------------------- | ----------- | ----------------------------------------------------- |
| [SDL_TrayEntry](SDL_TrayEntry) * | **entry**   | the entry to be updated.                              |
| bool                             | **checked** | true if the entry should be checked; false otherwise. |

## Remarks

The entry must have been created with the
[SDL_TRAYENTRY_CHECKBOX](SDL_TRAYENTRY_CHECKBOX) flag.

## Version

This function is available since SDL 3.1.8.

## See Also

- [SDL_GetTrayEntries](SDL_GetTrayEntries)
- [SDL_InsertTrayEntryAt](SDL_InsertTrayEntryAt)
- [SDL_GetTrayEntryChecked](SDL_GetTrayEntryChecked)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryTray](CategoryTray)

