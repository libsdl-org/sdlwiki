###### (This function is part of SDL_mixer, a separate library from SDL.)
# Mix_FadeInChannelTimed

Play an audio chunk on a specific channel, fading in the audio, for a maximum time.

## Syntax

```c
int Mix_FadeInChannelTimed(int channel, Mix_Chunk *chunk, int loops, int ms, int ticks);

```

## Function Parameters

|                 |                                                                                  |
| --------------- | -------------------------------------------------------------------------------- |
| **channel**     | the channel on which to play the new chunk, or -1 to find any available.         |
| **chunk**       | the new chunk to play.                                                           |
| **loops**       | the number of times the chunk should loop, -1 to loop (not actually) infinitely. |
| **ms**          | the number of milliseconds to spend fading in.                                   |
| **ticks**       | the maximum number of milliseconds of this chunk to mix for playback.            |

## Return Value

Returns which channel was used to play the sound, or -1 if sound could not
be played.

## Remarks

This will start the new sound playing, much like
[Mix_PlayChannel](Mix_PlayChannel.md)() will, but will start the sound playing
at silence and fade in to its normal volume over the specified number of
milliseconds.

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

A fading channel will change it's volume progressively, as if
[Mix_Volume](Mix_Volume.md)() was called on it (which is to say: you probably
shouldn't call [Mix_Volume](Mix_Volume.md)() on a fading channel).

## Version

This function is available since SDL_mixer 3.0.0.

----
[CategoryAPI](CategoryAPI.md)
