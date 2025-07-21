# SDL_IsTraySupported

Check whether or not tray icons can be created.

## Header File

Defined in [<SDL3/SDL_tray.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_tray.h)

## Syntax

```c
bool SDL_IsTraySupported(void);
```

## Return Value

(bool) Returns true if trays are available, false otherwise.

## Remarks

Note that this function does not guarantee that
[SDL_CreateTray](SDL_CreateTray)() will or will not work; you should still
check [SDL_CreateTray](SDL_CreateTray)() for errors.

Using tray icons require the video subsystem.

## Thread Safety

This function should only be called on the main thread. It will return
false if not called on the main thread.

## Version

This function is available since SDL 3.4.0.

## See Also

- [SDL_CreateTray](SDL_CreateTray)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryTray](CategoryTray)

