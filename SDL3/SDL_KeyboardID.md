# SDL_KeyboardID

This is a unique ID for a keyboard for the time it is connected to the system, and is never reused for the lifetime of the application.

## Header File

Defined in [<SDL3/SDL_keyboard.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_keyboard.h)

## Syntax

```c
typedef Uint32 SDL_KeyboardID;
```

## Remarks

If the keyboard is disconnected and reconnected, it will get a new ID.

The value 0 is an invalid ID.

## Version

This datatype is available since SDL 3.2.0.





----
[CategoryAPI](CategoryAPI), [CategoryAPIDatatype](CategoryAPIDatatype), [CategoryKeyboard](CategoryKeyboard)

