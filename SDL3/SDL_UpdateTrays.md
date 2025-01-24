# SDL_UpdateTrays

Update the trays.

## Header File

Defined in [<SDL3/SDL_tray.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_tray.h)

## Syntax

```c
void SDL_UpdateTrays(void);
```

## Remarks

This is called automatically by the event loop and is only needed if you're
using trays but aren't handling SDL events.

## Thread Safety

This function should only be called on the main thread.

## Version

This function is available since SDL 3.2.0.





----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryTray](CategoryTray)

