###### (This function is part of SDL_mixer, a separate library from SDL.)
# MIX_Init

Initialize the SDL_mixer library.

## Header File

Defined in [<SDL3_mixer/SDL_mixer.h>](https://github.com/libsdl-org/SDL_mixer/blob/main/include/SDL3_mixer/SDL_mixer.h)

## Syntax

```c
bool MIX_Init(void);
```

## Return Value

(bool) Returns true on success, false on error; call SDL_GetError() for
details.

## Remarks

This must be successfully called once before (almost) any other SDL_mixer
function can be used.

It is safe to call this multiple times; the library will only initialize
once, and won't deinitialize until [MIX_Quit](MIX_Quit)() has been called a
matching number of times. Extra attempts to init report success.

## Thread Safety

It is safe to call this function from any thread.

## Version

This function is available since SDL_mixer 3.0.0.

## See Also

- [MIX_Quit](MIX_Quit)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategorySDLMixer](CategorySDLMixer)

