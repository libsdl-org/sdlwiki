# SDL_GetTrayEntryEnabled

Gets whether or not an entry is enabled.

## Header File

Defined in [<SDL3/SDL_tray.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_tray.h)

## Syntax

```c
bool SDL_GetTrayEntryEnabled(SDL_TrayEntry *entry);
```

## Function Parameters

|                                  |           |                       |
| -------------------------------- | --------- | --------------------- |
| [SDL_TrayEntry](SDL_TrayEntry) * | **entry** | the entry to be read. |

## Return Value

(bool) Returns true if the entry is enabled; false otherwise.

## Thread Safety

This function should be called on the thread that created the tray.

## Version

This function is available since SDL 3.2.0.

## See Also

- [SDL_GetTrayEntries](SDL_GetTrayEntries)
- [SDL_InsertTrayEntryAt](SDL_InsertTrayEntryAt)
- [SDL_SetTrayEntryEnabled](SDL_SetTrayEntryEnabled)






----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryTray](CategoryTray)

