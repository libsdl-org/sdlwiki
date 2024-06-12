###### (This function is part of SDL_mixer, a separate library from SDL.)
# Mix_PlayChannelTimed

Play an audio chunk on a specific channel for a maximum time.

## Header File

Defined in [<SDL_mixer.h>](https://github.com/libsdl-org/SDL_mixer/blob/SDL2/include/SDL_mixer.h)

## Syntax

```c
int Mix_PlayChannelTimed(int channel, Mix_Chunk *chunk, int loops, int ticks);
```

## Function Parameters

|                          |             |                                                                                  |
| ------------------------ | ----------- | -------------------------------------------------------------------------------- |
| int                      | **channel** | the channel on which to play the new chunk.                                      |
| [Mix_Chunk](Mix_Chunk) * | **chunk**   | the new chunk to play.                                                           |
| int                      | **loops**   | the number of times the chunk should loop, -1 to loop (not actually) infinitely. |
| int                      | **ticks**   | the maximum number of milliseconds of this chunk to mix for playback.            |

## Return Value

(int) Returns which channel was used to play the sound, or -1 if sound
could not be played.

## Remarks

If the specified channel is -1, play on the first free channel (and return
-1 without playing anything new if no free channel was available).

If a specific channel was requested, and there is a chunk already playing
there, that chunk will be halted and the new chunk will take its place.

If `loops` is greater than zero, loop the sound that many times. If `loops`
is -1, loop "infinitely" (~65000 times).

`ticks` specifies the maximum number of milliseconds to play this chunk
before halting it. If you want the chunk to play until all data has been
mixed, specify -1.

Note that this function does not block for the number of ticks requested;
it just schedules the chunk to play and notes the maximum for the mixer to
manage later, and returns immediately.

## Version

This function is available since SDL_mixer 2.0.0.

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction)

