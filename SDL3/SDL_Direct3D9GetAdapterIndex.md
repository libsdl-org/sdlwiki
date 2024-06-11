###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_Direct3D9GetAdapterIndex

Get the D3D9 adapter index that matches the specified display.

## Header File

Defined in [<SDL3/SDL_system.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_system.h)

## Syntax

```c
int SDL_Direct3D9GetAdapterIndex(SDL_DisplayID displayID);
```

## Function Parameters

|                   |                                      |
| ----------------- | ------------------------------------ |
| **displayID**     | the instance of the display to query |

## Return Value

Returns the D3D9 adapter index on success or a negative error code on
failure; call [SDL_GetError](SDL_GetError)() for more information.

## Remarks

The returned adapter index can be passed to `IDirect3D9::CreateDevice` and
controls on which monitor a full screen application will appear.

## Version

This function is available since SDL 3.0.0.

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategorySystem](CategorySystem)

