###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_DXGIGetOutputInfo

Get the DXGI Adapter and Output indices for the specified display.

## Header File

Defined in [<SDL3/SDL_system.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_system.h)

## Syntax

```c
SDL_bool SDL_DXGIGetOutputInfo(SDL_DisplayID displayID, int *adapterIndex, int *outputIndex);

```

## Function Parameters

|                      |                                                  |
| -------------------- | ------------------------------------------------ |
| **displayID**        | the instance of the display to query             |
| **adapterIndex**     | a pointer to be filled in with the adapter index |
| **outputIndex**      | a pointer to be filled in with the output index  |

## Return Value

Returns [SDL_TRUE](SDL_TRUE) on success or [SDL_FALSE](SDL_FALSE) on
failure; call [SDL_GetError](SDL_GetError)() for more information.

## Remarks

The DXGI Adapter and Output indices can be passed to `EnumAdapters` and
`EnumOutputs` respectively to get the objects required to create a DX10 or
DX11 device and swap chain.

## Version

This function is available since SDL 3.0.0.

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategorySystem](CategorySystem)

