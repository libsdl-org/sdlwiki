# SDL_GetTrayEntryChecked

Gets whether or not an entry is checked.

## Header File

Defined in [<SDL3/SDL_tray.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_tray.h)

## Syntax

```c
bool SDL_GetTrayEntryChecked(SDL_TrayEntry *entry);
```

## Function Parameters

|                                  |           |                       |
| -------------------------------- | --------- | --------------------- |
| [SDL_TrayEntry](SDL_TrayEntry) * | **entry** | the entry to be read. |

## Return Value

(bool) Returns true if the entry is checked; false otherwise.

## Remarks

The entry must have been created with the
[SDL_TRAYENTRY_CHECKBOX](SDL_TRAYENTRY_CHECKBOX) flag.

## Thread Safety

This function should be called on the thread that created the tray.

## Version

This function is available since SDL 3.2.0.

## See Also

- [SDL_GetTrayEntries](SDL_GetTrayEntries)
- [SDL_InsertTrayEntryAt](SDL_InsertTrayEntryAt)
- [SDL_SetTrayEntryChecked](SDL_SetTrayEntryChecked)


## (This is the documentation for SDL3, which is the current stable version. [SDL2](https://wiki.libsdl.org/SDL2/) was the previous version!)



----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryTray](CategoryTray)

