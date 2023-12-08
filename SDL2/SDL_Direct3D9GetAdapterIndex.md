###### (This is the legacy documentation for stable SDL2, the current stable version; [SDL3](https://wiki.libsdl.org/SDL3/) is the current development version.)
# SDL_Direct3D9GetAdapterIndex

Get the D3D9 adapter index that matches the specified display index.

## Syntax

```c
int SDL_Direct3D9GetAdapterIndex( int displayIndex );

```

## Function Parameters

|                      |                                                           |
| -------------------- | --------------------------------------------------------- |
| **displayIndex**     | the display index for which to get the D3D9 adapter index |

## Return Value

Returns the D3D9 adapter index on success or a negative error code on
failure; call [SDL_GetError](SDL_GetError.md)() for more information.

## Remarks

The returned adapter index can be passed to `IDirect3D9::CreateDevice` and
controls on which monitor a full screen application will appear.

## Version

This function is available since SDL 2.0.1.

----
[CategoryAPI](CategoryAPI.md)
