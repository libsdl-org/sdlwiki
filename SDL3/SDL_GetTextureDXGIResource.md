###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_GetTextureDXGIResource

Get the DXGI resource associated with a texture.

## Syntax

```c
IDXGIResource* SDL_GetTextureDXGIResource(SDL_Texture *texture);

```

## Function Parameters

|                 |                                                       |
| --------------- | ----------------------------------------------------- |
| **texture**     | the texture from which to get the associated resource |

## Return Value

Returns the DXGI resource associated with given texture or NULL if it is
not available; call [SDL_GetError](SDL_GetError)() for more information.

## Remarks

This is available when using the direct3d11 and direct3d12 renderers.

Once you are done using the resource, you should release it to avoid a
resource leak.

## Version

This function is available since SDL 3.0.0.

----
[CategoryAPI](CategoryAPI)

