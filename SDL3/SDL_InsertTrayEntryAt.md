###### (This is the documentation for SDL3, which is the current stable version. [SDL2](https://wiki.libsdl.org/SDL2/) was the previous version!)
# SDL_InsertTrayEntryAt

Insert a tray entry at a given position.

## Header File

Defined in [<SDL3/SDL_tray.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_tray.h)

## Syntax

```c
SDL_TrayEntry* SDL_InsertTrayEntryAt(SDL_TrayMenu *menu, int pos, const char *label, SDL_TrayEntryFlags flags);
```

## Function Parameters

|                                          |           |                                                                                                                                |
| ---------------------------------------- | --------- | ------------------------------------------------------------------------------------------------------------------------------ |
| [SDL_TrayMenu](SDL_TrayMenu) *           | **menu**  | the menu to append the entry to.                                                                                               |
| int                                      | **pos**   | the desired position for the new entry. Entries at or following this place will be moved. If pos is -1, the entry is appended. |
| const char *                             | **label** | the text to be displayed on the entry, in UTF-8 encoding, or NULL for a separator.                                             |
| [SDL_TrayEntryFlags](SDL_TrayEntryFlags) | **flags** | a combination of flags, some of which are mandatory.                                                                           |

## Return Value

([SDL_TrayEntry](SDL_TrayEntry) *) Returns the newly created entry, or NULL
if pos is out of bounds.

## Remarks

If label is NULL, the entry will be a separator. Many functions won't work
for an entry that is a separator.

An entry does not need to be destroyed; it will be destroyed with the tray.

## Version

This function is available since SDL 3.1.8.

## See Also

- [SDL_TrayEntryFlags](SDL_TrayEntryFlags)
- [SDL_GetTrayEntries](SDL_GetTrayEntries)
- [SDL_RemoveTrayEntry](SDL_RemoveTrayEntry)
- [SDL_GetTrayEntryParent](SDL_GetTrayEntryParent)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryTray](CategoryTray)

