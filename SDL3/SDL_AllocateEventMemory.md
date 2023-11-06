###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_AllocateEventMemory

Allocate dynamic memory for an SDL event 

## Syntax

```c
void * SDL_AllocateEventMemory(size_t size);

```

## Function Parameters

|              |                                  |
| ------------ | -------------------------------- |
| **size**     | the amount of memory to allocate |

## Return Value

Returns a pointer to the memory allocated or NULL on failure; call
[SDL_GetError](SDL_GetError)() for more information.

## Remarks

You can use this to allocate memory for user events that will be
automatically freed after the event is processed.

## Version

This function is available since SDL 3.0.0.

----
[CategoryAPI](CategoryAPI)

