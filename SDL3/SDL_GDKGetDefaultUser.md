###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_GDKGetDefaultUser

Gets a reference to the default user handle for GDK.

## Header File

Defined in [<SDL3/SDL_system.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_system.h)

## Syntax

```c
int SDL_GDKGetDefaultUser(XUserHandle * outUserHandle);
```

## Function Parameters

|                       |                                                         |
| --------------------- | ------------------------------------------------------- |
| **outUserHandle**     | a pointer to be filled in with the default user handle. |

## Return Value

Returns 0 if success, -1 if any error occurs.

## Remarks

This is effectively a synchronous version of XUserAddAsync, which always
prefers the default user and allows a sign-in UI.

## Version

This function is available since SDL 3.0.0.

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategorySystem](CategorySystem)

