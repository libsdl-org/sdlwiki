###### (This function is part of SDL_mixer, a separate library from SDL.)
# Mix_ReserveChannels

Reserve the first channels for the application.

## Syntax

```c
int Mix_ReserveChannels(int num);

```

## Function Parameters

|             |                                                        |
| ----------- | ------------------------------------------------------ |
| **num**     | number of channels to reserve, starting at index zero. |

## Return Value

Returns the number of reserved channels.

## Remarks

While SDL_mixer will use up to the number of channels allocated by
[Mix_AllocateChannels](Mix_AllocateChannels)(), this sets channels aside
that will not be available when calling [Mix_PlayChannel](Mix_PlayChannel)
with a channel of -1 (play on the first unused channel). In this case,
SDL_mixer will treat reserved channels as "used" whether anything is
playing on them at the moment or not.

This is useful if you've budgeted some channels for dedicated audio and the
rest are just used as they are available.

Calling this function will set channels 0 to `n - 1` to be reserved. This
will not change channel allocations. The number of reserved channels will
be clamped to the current number allocated.

By default, no channels are reserved.

## Version

This function is available since SDL_mixer 2.0.0.

----
[CategoryAPI](CategoryAPI)

