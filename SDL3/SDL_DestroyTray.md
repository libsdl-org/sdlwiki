# SDL_DestroyTray

Destroys a tray object.

## Header File

Defined in [<SDL3/SDL_tray.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_tray.h)

## Syntax

```c
void SDL_DestroyTray(SDL_Tray *tray);
```

## Function Parameters

|                        |          |                                |
| ---------------------- | -------- | ------------------------------ |
| [SDL_Tray](SDL_Tray) * | **tray** | the tray icon to be destroyed. |

## Remarks

This also destroys all associated menus and entries.

## Thread Safety

This function should be called on the thread that created the tray.

## Version

This function is available since SDL 3.2.0.

## See Also

- [SDL_CreateTray](SDL_CreateTray)


## (This is the documentation for SDL3, which is the current stable version. [SDL2](https://wiki.libsdl.org/SDL2/) was the previous version!)



----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryTray](CategoryTray)

