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

## Thread Safety

This function should be called on the thread that created the tray.

## Version

This function is available since SDL 3.2.0.

## See Also

- [SDL_GetTrayEntries](SDL_GetTrayEntries)
- [SDL_InsertTrayEntryAt](SDL_InsertTrayEntryAt)
- [SDL_GetTrayEntryChecked](SDL_GetTrayEntryChecked)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryTray](CategoryTray)

