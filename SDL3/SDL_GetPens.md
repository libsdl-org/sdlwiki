###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_GetPens

Retrieves all pens that are connected to the system.

## Syntax

```c
SDL_PenID* SDL_GetPens(int *count);

```

## Function Parameters

|               |                                                                                                          |
| ------------- | -------------------------------------------------------------------------------------------------------- |
| **count**     | The number of pens in the array (number of array elements minus 1, i.e., not counting the terminator 0). |

## Return Value

Returns A 0 terminated array of ::[SDL_PenID](SDL_PenID) values, or NULL on
error. The array must be freed with ::[SDL_free](SDL_free)(). On a NULL
return, ::[SDL_GetError](SDL_GetError)() is set.

## Remarks

Yields an array of ::[SDL_PenID](SDL_PenID) values. These identify and
track pens throughout a session. To track pens across sessions (program
restart), use ::[SDL_GUID](SDL_GUID) .

## Version

This function is available since SDL 3.0.0

----
[CategoryAPI](CategoryAPI)

