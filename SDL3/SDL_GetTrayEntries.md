###### (This is the documentation for SDL3, which is the current stable version. [SDL2](https://wiki.libsdl.org/SDL2/) was the previous version!)
# SDL_GetTrayEntries

Returns a list of entries in the menu, in order.

## Header File

Defined in [<SDL3/SDL_tray.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_tray.h)

## Syntax

```c
extern SDL_DECLSPEC const SDL_TrayEntry **SDLCALL SDL_GetTrayEntries(SDL_TrayMenu *menu, int *size);
```

## Function Parameters

|                                |          |                                                                  |
| ------------------------------ | -------- | ---------------------------------------------------------------- |
| [SDL_TrayMenu](SDL_TrayMenu) * | **menu** | The menu to get entries from.                                    |
| int *                          | **size** | An optional pointer to obtain the number of entries in the menu. |

## Return Value

(const [SDL_TrayEntry](SDL_TrayEntry) **) Returns a NULL-terminated list of
entries within the given menu. The pointer becomes invalid when any
function that inserts or deletes entries in the menu is called.

## Thread Safety

This function should be called on the thread that created the tray.

## Version

This function is available since SDL 3.2.0.

## See Also

- [SDL_RemoveTrayEntry](SDL_RemoveTrayEntry)
- [SDL_InsertTrayEntryAt](SDL_InsertTrayEntryAt)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryTray](CategoryTray)

