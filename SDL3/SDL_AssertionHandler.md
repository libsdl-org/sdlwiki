###### (This is the documentation for SDL3, which is the current stable version. [SDL2](https://wiki.libsdl.org/SDL2/) was the previous version!)
# SDL_AssertionHandler

A callback that fires when an SDL assertion fails.

## Header File

Defined in [<SDL3/SDL_assert.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_assert.h)

## Syntax

```c
typedef SDL_AssertState (SDLCALL *SDL_AssertionHandler)( const SDL_AssertData *data, void *userdata);
```

## Function Parameters

|              |                                                                                                     |
| ------------ | --------------------------------------------------------------------------------------------------- |
| **data**     | a pointer to the [SDL_AssertData](SDL_AssertData) structure corresponding to the current assertion. |
| **userdata** | what was passed as `userdata` to [SDL_SetAssertionHandler](SDL_SetAssertionHandler)().              |

## Return Value

Returns an [SDL_AssertState](SDL_AssertState) value indicating how to
handle the failure.

## Thread Safety

This callback may be called from any thread that triggers an assert at any
time.

## Version

This datatype is available since SDL 3.1.3.

----
[CategoryAPI](CategoryAPI), [CategoryAPIDatatype](CategoryAPIDatatype), [CategoryAssert](CategoryAssert)

