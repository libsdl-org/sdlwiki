# SDL_ClickTrayEntry

Simulate a click on a tray entry.

## Header File

Defined in [<SDL3/SDL_tray.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_tray.h)

## Syntax

```c
void SDL_ClickTrayEntry(SDL_TrayEntry *entry);
```

## Function Parameters

|                                  |           |                        |
| -------------------------------- | --------- | ---------------------- |
| [SDL_TrayEntry](SDL_TrayEntry) * | **entry** | The entry to activate. |

## Thread Safety

This function should be called on the thread that created the tray.

## Version

This function is available since SDL 3.2.0.

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryTray](CategoryTray)

