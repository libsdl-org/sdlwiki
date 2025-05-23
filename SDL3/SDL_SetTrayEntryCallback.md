# SDL_SetTrayEntryCallback

Sets a callback to be invoked when the entry is selected.

## Header File

Defined in [<SDL3/SDL_tray.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_tray.h)

## Syntax

```c
void SDL_SetTrayEntryCallback(SDL_TrayEntry *entry, SDL_TrayCallback callback, void *userdata);
```

## Function Parameters

|                                      |              |                                                                                 |
| ------------------------------------ | ------------ | ------------------------------------------------------------------------------- |
| [SDL_TrayEntry](SDL_TrayEntry) *     | **entry**    | the entry to be updated.                                                        |
| [SDL_TrayCallback](SDL_TrayCallback) | **callback** | a callback to be invoked when the entry is selected.                            |
| void *                               | **userdata** | an optional pointer to pass extra data to the callback when it will be invoked. |

## Thread Safety

This function should be called on the thread that created the tray.

## Version

This function is available since SDL 3.2.0.

## See Also

- [SDL_GetTrayEntries](SDL_GetTrayEntries)
- [SDL_InsertTrayEntryAt](SDL_InsertTrayEntryAt)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryTray](CategoryTray)

