# SDL_GetTrayEntryLabel

Gets the label of an entry.

## Header File

Defined in [<SDL3/SDL_tray.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_tray.h)

## Syntax

```c
const char* SDL_GetTrayEntryLabel(SDL_TrayEntry *entry);
```

## Function Parameters

|                                  |           |                       |
| -------------------------------- | --------- | --------------------- |
| [SDL_TrayEntry](SDL_TrayEntry) * | **entry** | the entry to be read. |

## Return Value

(const char *) Returns the label of the entry in UTF-8 encoding.

## Remarks

If the returned value is NULL, the entry is a separator.

## Thread Safety

This function should be called on the thread that created the tray.

## Version

This function is available since SDL 3.2.0.

## See Also

- [SDL_GetTrayEntries](SDL_GetTrayEntries)
- [SDL_InsertTrayEntryAt](SDL_InsertTrayEntryAt)
- [SDL_SetTrayEntryLabel](SDL_SetTrayEntryLabel)


## (This is the documentation for SDL3, which is the current stable version. [SDL2](https://wiki.libsdl.org/SDL2/) was the previous version!)



----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryTray](CategoryTray)

