###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_RenderGetD3D12Device

Get the D3D12 device associated with a renderer.

## Syntax

```c
ID3D12Device* SDL_RenderGetD3D12Device(SDL_Renderer* renderer);

```

## Function Parameters

|                  |                                                            |
| ---------------- | ---------------------------------------------------------- |
| **renderer**     | the renderer from which to get the associated D3D12 device |

## Return Value

Returns the D3D12 device associated with given renderer or NULL if it is
not a D3D12 renderer; call [SDL_GetError](SDL_GetError)() for more
information.

## Remarks

Once you are done using the device, you should release it to avoid a
resource leak.

## Version

This function is available since SDL 3.0.0.

----
[CategoryAPI](CategoryAPI)

