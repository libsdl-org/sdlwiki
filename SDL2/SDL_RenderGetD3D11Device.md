###### (This is the legacy documentation for stable SDL2, the current stable version; [SDL3](https://wiki.libsdl.org/SDL3/) is the current development version.)
# SDL_RenderGetD3D11Device

Get the D3D11 device associated with a renderer.

## Header File

Defined in [SDL_system.h](https://github.com/libsdl-org/SDL/blob/SDL2/include/SDL_system.h)

## Syntax

```c
ID3D11Device* SDL_RenderGetD3D11Device(SDL_Renderer * renderer);

```

## Function Parameters

|                  |                                                            |
| ---------------- | ---------------------------------------------------------- |
| **renderer**     | the renderer from which to get the associated D3D11 device |

## Return Value

Returns the D3D11 device associated with given renderer or NULL if it is
not a D3D11 renderer; call [SDL_GetError](SDL_GetError)() for more
information.

## Remarks

Once you are done using the device, you should release it to avoid a
resource leak.

## Version

This function is available since SDL 2.0.16.

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction)


