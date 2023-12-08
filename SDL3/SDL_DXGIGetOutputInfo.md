###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)

## Draft

**THIS PAGE IS A WORK IN PROGRESS** ... Please make edits to this page to improve it!


<!-- #*^*^*^*^*See https://wiki.libsdl.org/SGFunctions for details on editing this page*^*^*^*^* -->
# SDL_DXGIGetOutputInfo

Get the DXGI Adapter and Output indices for the specified display.

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

Returns [SDL_TRUE](SDL_TRUE.md) on success or [SDL_FALSE](SDL_FALSE.md) on
failure; call [SDL_GetError](SDL_GetError.md)() for more information.

## Remarks

The DXGI Adapter and Output indices can be passed to `EnumAdapters` and
`EnumOutputs` respectively to get the objects required to create a DX10 or
DX11 device and swap chain.

## Version

This function is available since SDL 3.0.0.

----
[CategoryAPI](CategoryAPI.md), [CategorySystem](CategorySystem.md), [CategoryDraft](CategoryDraft.md)
<!-- #See the Style Guide for instructions on editing the footer. -->
