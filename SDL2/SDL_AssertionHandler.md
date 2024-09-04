###### (This is the legacy documentation for stable SDL2, the current stable version; [SDL3](https://wiki.libsdl.org/SDL3/) is the current development version.)
# SDL_AssertionHandler

A callback that fires when an SDL assertion fails.

## Header File

Defined in [SDL_assert.h](https://github.com/libsdl-org/SDL/blob/SDL2/include/SDL_assert.h)

## Syntax

```c
typedef SDL_AssertState (SDLCALL *SDL_AssertionHandler)( const SDL_AssertData* data, void* userdata);
```

## Function Parameters

|              |                                                                                                     |
| ------------ | --------------------------------------------------------------------------------------------------- |
| **data**     | a pointer to the [SDL_AssertData](SDL_AssertData) structure corresponding to the current assertion. |
| **userdata** | what was passed as `userdata` to [SDL_SetAssertionHandler](SDL_SetAssertionHandler)().              |

## Return Value

Returns an [SDL_AssertState](SDL_AssertState) value indicating how to
handle the failure.

----
[CategoryAPI](CategoryAPI), [CategoryAPIDatatype](CategoryAPIDatatype), [CategoryAssert](CategoryAssert)

