###### (This is the legacy documentation for stable SDL2, the current stable version; [SDL3](https://wiki.libsdl.org/SDL3/) is the current development version.)
# SDL_HintCallback

Type definition of the hint callback function.

## Header File

Defined in [SDL_hints.h](https://github.com/libsdl-org/SDL/blob/SDL2/include/SDL_hints.h)

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
[CategoryAPI](CategoryAPI), [CategoryAPIDatatype](CategoryAPIDatatype), [CategoryHints](CategoryHints)

