###### (This function is part of SDL_mixer, a separate library from SDL.)
# Mix_Resume

Resume a particular channel.

## Syntax

```c
void Mix_Resume(int channel);

```

## Function Parameters

|                 |                                                             |
| --------------- | ----------------------------------------------------------- |
| **channel**     | the channel to resume, or -1 to resume all paused channels. |

## Remarks

It is legal to resume an unpaused or invalid channel; it causes no effect
and reports no error.

If the paused channel has an expiration, its expiration countdown resumes
now, as well.

Specifying a channel of -1 will resume _all_ paused channels. Any music is
unaffected.

## Version

This function is available since SDL_mixer 3.0.0.

----
[CategoryAPI](CategoryAPI)

