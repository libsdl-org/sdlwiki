###### (This is the legacy documentation for SDL2, the previous stable version; [SDL3](https://wiki.libsdl.org/SDL3/) is the current stable version.)
# SDL_GDKGetDefaultUser

Gets a reference to the default user handle for GDK.

## Header File

Defined in [SDL_system.h](https://github.com/libsdl-org/SDL/blob/SDL2/include/SDL_system.h)

## Syntax

```c
int SDL_GDKGetDefaultUser(XUserHandle * outUserHandle);
```

## Function Parameters

|               |                   |                                                         |
| ------------- | ----------------- | ------------------------------------------------------- |
| XUserHandle * | **outUserHandle** | a pointer to be filled in with the default user handle. |

## Return Value

(int) Returns 0 if success, -1 if any error occurs.

## Remarks

This is effectively a synchronous version of XUserAddAsync, which always
prefers the default user and allows a sign-in UI.

## Version

This function is available since SDL 2.28.0.

## (This is the legacy documentation for stable SDL2, the previous stable version; [SDL3](https://wiki.libsdl.org/SDL3/) is the current stable version.)



## (This is the legacy documentation for stable SDL2, the current stable version; [SDL3](https://wiki.libsdl.org/SDL3/) is the current development version.)



----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategorySystem](CategorySystem)

