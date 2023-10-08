###### (This function is part of SDL_mixer, a separate library from SDL.)
# Mix_FadeInMusicPos

Play a new music object, fading in the audio, from a starting position.

## Syntax

```c
int Mix_FadeInMusicPos(Mix_Music *music, int loops, int ms, double position);

```

## Function Parameters

|                  |                                                                                  |
| ---------------- | -------------------------------------------------------------------------------- |
| **music**        | the new music object to play.                                                    |
| **loops**        | the number of times the chunk should loop, -1 to loop (not actually) infinitely. |
| **ms**           | the number of milliseconds to spend fading in.                                   |
| **position**     | the start position within the music, in seconds, where playback should start.    |

## Return Value

Returns zero on success, -1 on error.

## Remarks

This will start the new music playing, much like
[Mix_PlayMusic](Mix_PlayMusic)() will, but will start the music playing at
silence and fade in to its normal volume over the specified number of
milliseconds.

If there is already music playing, that music will be halted and the new
music object will take its place.

If `loops` is greater than zero, loop the music that many times. If `loops`
is -1, loop "infinitely" (~65000 times).

Fading music will change it's volume progressively, as if
[Mix_VolumeMusic](Mix_VolumeMusic)() was called on it (which is to say: you
probably shouldn't call [Mix_VolumeMusic](Mix_VolumeMusic)() on fading
music).

This function allows the caller to start the music playback past the
beginning of its audio data. You may specify a start position, in seconds,
and the playback and fade-in will start there instead of with the first
samples of the music.

An app can specify a `position` of 0.0 to start at the beginning of the
music (or just call [Mix_FadeInMusic](Mix_FadeInMusic)() instead).

To convert from milliseconds, divide by 1000.0.

## Version

This function is available since SDL_mixer 2.0.0.

----
[CategoryAPI](CategoryAPI)

