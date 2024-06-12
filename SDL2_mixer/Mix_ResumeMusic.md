###### (This function is part of SDL_mixer, a separate library from SDL.)
# Mix_ResumeMusic

Resume the music stream.

## Header File

Defined in [<SDL_mixer.h>](https://github.com/libsdl-org/SDL_mixer/blob/SDL2/include/SDL_mixer.h)

## Syntax

```c
void Mix_ResumeMusic(void);
```

## Remarks

It is legal to resume an unpaused music stream; it causes no effect and
reports no error.

## Version

This function is available since SDL_mixer 2.0.0.

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction)

