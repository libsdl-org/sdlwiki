###### (This is the documentation for SDL3, which is the current stable version. [SDL2](https://wiki.libsdl.org/SDL2/) was the previous version!)
# SDL_SetTrayEntryLabel

Sets the label of an entry.

## Header File

Defined in [<SDL3/SDL_tray.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_tray.h)

## Syntax

```c
void SDL_SetTrayEntryLabel(SDL_TrayEntry *entry, const char *label);
```

## Function Parameters

|                                  |           |                                                |
| -------------------------------- | --------- | ---------------------------------------------- |
| [SDL_TrayEntry](SDL_TrayEntry) * | **entry** | the entry to be updated.                       |
| const char *                     | **label** | the new label for the entry in UTF-8 encoding. |

## Remarks

An entry cannot change between a separator and an ordinary entry; that is,
it is not possible to set a non-NULL label on an entry that has a NULL
label (separators), or to set a NULL label to an entry that has a non-NULL
label. The function will silently fail if that happens.

## Thread Safety

This function should be called on the thread that created the tray.

## Version

This function is available since SDL 3.2.0.

## See Also

- [SDL_GetTrayEntries](SDL_GetTrayEntries)
- [SDL_InsertTrayEntryAt](SDL_InsertTrayEntryAt)
- [SDL_GetTrayEntryLabel](SDL_GetTrayEntryLabel)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryTray](CategoryTray)

