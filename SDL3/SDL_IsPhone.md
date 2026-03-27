# SDL_IsPhone

Query if the current device is a phone.

## Header File

Defined in [<SDL3/SDL_system.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_system.h)

## Syntax

```c
bool SDL_IsPhone(void);
```

## Return Value

(bool) Returns true if the device is a phone, false otherwise.

## Remarks

If SDL can't determine this, it will return false.

## Thread Safety

It is safe to call this function from any thread.

## Version

This function is available since SDL 3.6.0.

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategorySystem](CategorySystem)

