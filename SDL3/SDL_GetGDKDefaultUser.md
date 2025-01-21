###### (This is the documentation for SDL3, which is the current stable version. [SDL2](https://wiki.libsdl.org/SDL2/) was the previous version!)
# SDL_GetGDKDefaultUser

Gets a reference to the default user handle for GDK.

## Header File

Defined in [<SDL3/SDL_system.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_system.h)

## Syntax

```c
bool SDL_GetGDKDefaultUser(XUserHandle *outUserHandle);
```

## Function Parameters

|               |                   |                                                         |
| ------------- | ----------------- | ------------------------------------------------------- |
| XUserHandle * | **outUserHandle** | a pointer to be filled in with the default user handle. |

## Return Value

(bool) Returns true if success or false on failure; call
[SDL_GetError](SDL_GetError)() for more information.

## Remarks

This is effectively a synchronous version of XUserAddAsync, which always
prefers the default user and allows a sign-in UI.

## Version

This function is available since SDL 3.2.0.

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategorySystem](CategorySystem)

