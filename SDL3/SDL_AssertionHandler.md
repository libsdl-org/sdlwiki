###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_AssertionHandler

A callback that fires when an SDL assertion fails.

## Header File

Defined in [<SDL3/SDL_assert.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_assert.h)

## Syntax

```c
typedef SDL_AssertState (SDLCALL *SDL_AssertionHandler)( const SDL_AssertData* data, void* userdata);
```

## Function Parameters

|                  |                                                                                                    |
| ---------------- | -------------------------------------------------------------------------------------------------- |
| **data**         | a pointer to the [SDL_AssertData](SDL_AssertData) structure corresponding to the current assertion |
| **userdata**     | what was passed as `userdata` to [SDL_SetAssertionHandler](SDL_SetAssertionHandler)()              |

## Return Value

Returns an [SDL_AssertState](SDL_AssertState) value indicating how to
handle the failure.

## Version

This datatype is available since SDL 3.0.0.

----
[CategoryAPI](CategoryAPI), [CategoryAPIDatatype](CategoryAPIDatatype)

