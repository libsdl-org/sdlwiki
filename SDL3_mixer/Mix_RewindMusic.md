###### (This function is part of SDL_mixer, a separate library from SDL.)
# Mix_RewindMusic

Rewind the music stream.

## Header File

Defined in SDL_mixer.h

## Syntax

```c
void Mix_RewindMusic(void);

```

## Remarks

This causes the currently-playing music to start mixing from the beginning
of the music, as if it were just started.

It's a legal no-op to rewind the music stream when not playing.

## Version

This function is available since SDL_mixer 3.0.0.

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction)

