###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_GetWindowICCProfile

Get the raw ICC profile data for the screen the window is currently on.

## Syntax

```c
void* SDL_GetWindowICCProfile(SDL_Window *window, size_t *size);

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

This function is available since SDL 3.0.0.

----
[CategoryAPI](CategoryAPI)

