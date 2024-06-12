###### (This function is part of SDL_mixer, a separate library from SDL.)
# Mix_ResumeGroup

Resume playing of a group of channels by arbitrary tag.

## Header File

Defined in [<SDL3_mixer/SDL_mixer.h>](https://github.com/libsdl-org/SDL_mixer/blob/main/include/SDL3_mixer/SDL_mixer.h)

## Syntax

```c
int Mix_ResumeGroup(int tag);
```

## Function Parameters

|     |         |                                                          |
| --- | ------- | -------------------------------------------------------- |
| int | **tag** | an arbitrary value, assigned to channels, to search for. |

## Return Value

(int) Returns zero, whether any channels were resumed or not.

## Remarks

It is legal to resume an unpaused or invalid channel; it causes no effect
and reports no error.

If the paused channel has an expiration, its expiration countdown resumes
now, as well.

A tag is an arbitrary number that can be assigned to several mixer
channels, to form groups of channels.

The default tag for a channel is -1.

## Version

This function is available since SDL_mixer 3.0.0.

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction)

