###### (This function is part of SDL_mixer, a separate library from SDL.)
# Mix_Pause

Pause a particular channel.

## Syntax

```c
void Mix_Pause(int channel);

```

## Function Parameters

|                 |                                                    |
| --------------- | -------------------------------------------------- |
| **channel**     | the channel to pause, or -1 to pause all channels. |

## Remarks

Pausing a channel will prevent further playback of the assigned chunk but
will maintain the chunk's current mixing position. When resumed, this
channel will continue to mix the chunk where it left off.

A paused channel can be resumed by calling [Mix_Resume](Mix_Resume.md)().

A paused channel with an expiration will not expire while paused (the
expiration countdown will be adjusted once resumed).

It is legal to halt a paused channel. Playing a new chunk on a paused
channel will replace the current chunk and unpause the channel.

Specifying a channel of -1 will pause _all_ channels. Any music is
unaffected.

You may not specify MAX_CHANNEL_POST for a channel.

## Version

This function is available since SDL_mixer 3.0.0.

----
[CategoryAPI](CategoryAPI.md)
