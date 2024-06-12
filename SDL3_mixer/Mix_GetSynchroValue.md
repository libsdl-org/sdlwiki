###### (This function is part of SDL_mixer, a separate library from SDL.)
# Mix_GetSynchroValue

This function does nothing, do not use.

## Header File

Defined in [<SDL3_mixer/SDL_mixer.h>](https://github.com/libsdl-org/SDL_mixer/blob/main/include/SDL3_mixer/SDL_mixer.h)

## Syntax

```c
int Mix_GetSynchroValue(void);
```

## Return Value

(int) Returns -1.

## Remarks

This was probably meant to expose a feature, but no codecs support it, so
it only remains for binary compatibility.

Calling this function is a legal no-op that returns -1.

## Version

This function is available since SDL_mixer 3.0.0.

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction)

