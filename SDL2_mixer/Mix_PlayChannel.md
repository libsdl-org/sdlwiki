###### (This function is part of SDL_mixer, a separate library from SDL.)
# Mix_PlayChannel

Play an audio chunk on a specific channel.

## Syntax

```c
int Mix_PlayChannel(int channel, Mix_Chunk *chunk, int loops);

```

## Function Parameters

|                 |                                                                                  |
| --------------- | -------------------------------------------------------------------------------- |
| **channel**     | the channel on which to play the new chunk.                                      |
| **chunk**       | the new chunk to play.                                                           |
| **loops**       | the number of times the chunk should loop, -1 to loop (not actually) infinitely. |

## Return Value

Returns which channel was used to play the sound, or -1 if sound could not
be played.

## Remarks

If the specified channel is -1, play on the first free channel (and return
-1 without playing anything new if no free channel was available).

If a specific channel was requested, and there is a chunk already playing
there, that chunk will be halted and the new chunk will take its place.

If `loops` is greater than zero, loop the sound that many times. If `loops`
is -1, loop "infinitely" (~65000 times).

Note that before SDL_mixer 2.6.0, this function was a macro that called
[Mix_PlayChannelTimed](Mix_PlayChannelTimed)() with a fourth parameter
("ticks") of -1. This function still does the same thing, but promotes it
to a proper API function. Older binaries linked against a newer SDL_mixer
will still call [Mix_PlayChannelTimed](Mix_PlayChannelTimed) directly, as
they are using the macro, which was available since the dawn of time.

## Version

This function is available since SDL_mixer 2.6.0 (and as a macro since
2.0.0).

----
[CategoryAPI](CategoryAPI)

