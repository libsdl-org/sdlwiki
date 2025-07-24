###### (This function is part of SDL_mixer, a separate library from SDL.)
# MIX_Version

Get the version of SDL_mixer that is linked against your program.

## Header File

Defined in [<SDL3_mixer/SDL_mixer.h>](https://github.com/libsdl-org/SDL_mixer/blob/main/include/SDL3_mixer/SDL_mixer.h)

## Syntax

```c
int MIX_Version(void);
```

## Return Value

(int) Returns the version of the linked library.

## Remarks

If you are linking to SDL_mixer dynamically, then it is possible that the
current version will be different than the version you compiled against.
This function returns the current version, while
[SDL_MIXER_VERSION](SDL_MIXER_VERSION) is the version you compiled with.

This function may be called safely at any time, even before
[MIX_Init](MIX_Init)().

## Version

This function is available since SDL_mixer 3.0.0.

## See Also

- [SDL_MIXER_VERSION](SDL_MIXER_VERSION)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategorySDLMixer](CategorySDLMixer)

