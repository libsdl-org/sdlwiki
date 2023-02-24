###### (This is the legacy documentation for stable SDL2, the current stable version; [SDL3](https://wiki.libsdl.org/SDL3/) is the current development version.)
# SDL_GetWindowICCProfile

Get the raw ICC profile data for the screen the window is currently on.

## Syntax

```c
void* SDL_GetWindowICCProfile(SDL_Window * window, size_t* size);

```

## Function Parameters

|                |                             |
| -------------- | --------------------------- |
| **window**     | the window to query         |
| **size**       | the size of the ICC profile |

## Return Value

Returns the raw ICC profile data on success or NULL on failure; call
[SDL_GetError](SDL_GetError)() for more information.

## Remarks

Data returned should be freed with [SDL_free](SDL_free).

## Version

This function is available since SDL 2.0.18.

----
[CategoryAPI](CategoryAPI)

