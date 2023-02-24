###### (This is the legacy documentation for stable SDL2, the current stable version; [SDL3](https://wiki.libsdl.org/SDL3/) is the current development version.)
# SDL_SetTextureUserData

Associate a user-specified pointer with a texture.

## Syntax

```c
int SDL_SetTextureUserData(SDL_Texture * texture,
                           void *userdata);

```

## Function Parameters

|                  |                                            |
| ---------------- | ------------------------------------------ |
| **texture**      | the texture to update.                     |
| **userdata**     | the pointer to associate with the texture. |

## Return Value

Returns 0 on success, or -1 if the texture is not valid.

## Version

This function is available since SDL 2.0.18.

## Related Functions

* [SDL_GetTextureUserData](SDL_GetTextureUserData)

----
[CategoryAPI](CategoryAPI)

