###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_CloseStorage

Closes and frees a storage container.

## Syntax

```c
int SDL_CloseStorage(SDL_Storage *storage);

```

## Function Parameters

|                 |                              |
| --------------- | ---------------------------- |
| **storage**     | a storage container to close |

## Return Value

Returns 0 if the container was freed with no errors, a negative value
otherwise; call [SDL_GetError](SDL_GetError)() for more information. Even
if the function returns an error, the container data will be freed; the
error is only for informational purposes.

## Version

This function is available since SDL 3.0.0.

## Related Functions

* [SDL_OpenFileStorage](SDL_OpenFileStorage)
* [SDL_OpenStorage](SDL_OpenStorage)
* [SDL_OpenTitleStorage](SDL_OpenTitleStorage)
* [SDL_OpenUserStorage](SDL_OpenUserStorage)

----
[CategoryAPI](CategoryAPI)

