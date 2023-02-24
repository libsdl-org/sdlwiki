###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_SetTextureUserData

Associate a user-specified pointer with a texture.

## Syntax

```c
int SDL_SetTextureUserData(SDL_Texture *texture, void *userdata);

```

## Function Parameters

|                  |                                            |
| ---------------- | ------------------------------------------ |
| **texture**      | the texture to update.                     |
| **userdata**     | the pointer to associate with the texture. |

## Return Value

Returns 0 on success or a negative error code on failure; call
[SDL_GetError](SDL_GetError)() for more information.

## Version

This function is available since SDL 3.0.0.

## Related Functions

* [SDL_GetTextureUserData](SDL_GetTextureUserData)

----
[CategoryAPI](CategoryAPI)

