###### (This function is part of SDL_mixer, a separate library from SDL.)
# Mix_PauseGroup

Pause playing of a group of channels by arbitrary tag.

## Syntax

```c
int Mix_PauseGroup(int tag);

```

## Function Parameters

|             |                                                          |
| ----------- | -------------------------------------------------------- |
| **tag**     | an arbitrary value, assigned to channels, to search for. |

## Return Value

Returns zero, whether any channels were halted or not.

## Remarks

Pausing a channel will prevent further playback of the assigned chunk but
will maintain the chunk's current mixing position. When resumed, this
channel will continue to mix the chunk where it left off.

A paused channel can be resumed by calling [Mix_Resume](Mix_Resume)() or
[Mix_ResumeGroup](Mix_ResumeGroup)().

A paused channel with an expiration will not expire while paused (the
expiration countdown will be adjusted once resumed).

A tag is an arbitrary number that can be assigned to several mixer
channels, to form groups of channels.

The default tag for a channel is -1.

## Version

This function is available since SDL_mixer 3.0.0.

----
[CategoryAPI](CategoryAPI)

