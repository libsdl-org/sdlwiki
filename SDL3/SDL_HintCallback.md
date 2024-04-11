###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_HintCallback

Type definition of the hint callback function.

## Header File

Defined in [SDL_hints.h](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_hints.h), but apps should _only_ `#include <SDL3/SDL.h>`!

## Syntax

```c
typedef void (SDLCALL *SDL_HintCallback)(void *userdata, const char *name, const char *oldValue, const char *newValue);
```

## Function Parameters

|                  |                                                                               |
| ---------------- | ----------------------------------------------------------------------------- |
| **userdata**     | what was passed as `userdata` to [SDL_AddHintCallback](SDL_AddHintCallback)() |
| **name**         | what was passed as `name` to [SDL_AddHintCallback](SDL_AddHintCallback)()     |
| **oldValue**     | the previous hint value                                                       |
| **newValue**     | the new value hint is to be set to                                            |

----
[CategoryAPI](CategoryAPI), [CategoryAPIDatatype](CategoryAPIDatatype)

