###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_GetTextureUserData

Get the user-specified pointer associated with a texture 

## Syntax

```c
void* SDL_GetTextureUserData(SDL_Texture *texture);

```

## Function Parameters

|                 |                       |
| --------------- | --------------------- |
| **texture**     | the texture to query. |

## Return Value

Returns the pointer associated with the texture, or NULL if the texture is
not valid.

## Version

This function is available since SDL 3.0.0.

## Related Functions

* [SDL_SetTextureUserData](SDL_SetTextureUserData)

----
[CategoryAPI](CategoryAPI)

