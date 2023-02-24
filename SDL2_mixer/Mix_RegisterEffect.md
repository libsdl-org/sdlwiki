###### (This function is part of SDL_mixer, a separate library from SDL.)
# Mix_RegisterEffect

Register a special effect function.

## Syntax

```c
int Mix_RegisterEffect(int chan, Mix_EffectFunc_t f, Mix_EffectDone_t d, void *arg);

```

## Function Parameters

|              |                                                                                |
| ------------ | ------------------------------------------------------------------------------ |
| **chan**     | the channel to register an effect to, or [MIX_CHANNEL_POST](MIX_CHANNEL_POST). |
| **f**        | effect the callback to run when more of this channel is to be mixed.           |
| **d**        | effect done callback                                                           |
| **arg**      | argument                                                                       |

## Return Value

Returns zero if error (no such channel), nonzero if added. Error messages
can be retrieved from [Mix_GetError](Mix_GetError)().

## Remarks

At mixing time, the channel data is copied into a buffer and passed through
each registered effect function. After it passes through all the functions,
it is mixed into the final output stream. The copy to buffer is performed
once, then each effect function performs on the output of the previous
effect. Understand that this extra copy to a buffer is not performed if
there are no effects registered for a given chunk, which saves CPU cycles,
and any given effect will be extra cycles, too, so it is crucial that your
code run fast. Also note that the data that your function is given is in
the format of the sound device, and not the format you gave to
[Mix_OpenAudio](Mix_OpenAudio)(), although they may in reality be the same.
This is an unfortunate but necessary speed concern. Use
[Mix_QuerySpec](Mix_QuerySpec)() to determine if you can handle the data
before you register your effect, and take appropriate actions.

You may also specify a callback ([Mix_EffectDone_t](Mix_EffectDone_t)) that
is called when the channel finishes playing. This gives you a more
fine-grained control than [Mix_ChannelFinished](Mix_ChannelFinished)(), in
case you need to free effect-specific resources, etc. If you don't need
this, you can specify NULL.

You may set the callbacks before or after calling
[Mix_PlayChannel](Mix_PlayChannel)().

Things like [Mix_SetPanning](Mix_SetPanning)() are just internal special
effect functions, so if you are using that, you've already incurred the
overhead of a copy to a separate buffer, and that these effects will be in
the queue with any functions you've registered. The list of registered
effects for a channel is reset when a chunk finishes playing, so you need
to explicitly set them with each call to
[Mix_PlayChannel](Mix_PlayChannel)*().

You may also register a special effect function that is to be run after
final mixing occurs. The rules for these callbacks are identical to those
in [Mix_RegisterEffect](Mix_RegisterEffect), but they are run after all the
channels and the music have been mixed into a single stream, whereas
channel-specific effects run on a given channel before any other mixing
occurs. These global effect callbacks are call "posteffects". Posteffects
only have their [Mix_EffectDone_t](Mix_EffectDone_t) function called when
they are unregistered (since the main output stream is never "done" in the
same sense as a channel). You must unregister them manually when you've had
enough. Your callback will be told that the channel being mixed is
`[MIX_CHANNEL_POST](MIX_CHANNEL_POST)` if the processing is considered a
posteffect.

After all these effects have finished processing, the callback registered
through [Mix_SetPostMix](Mix_SetPostMix)() runs, and then the stream goes
to the audio device.

DO NOT EVER call SDL_LockAudio() from your callback function! You are
already running in the audio thread and the lock is already held!

Note that unlike most SDL and SDL_mixer functions, this function returns
zero if there's an error, not on success. We apologize for the API design
inconsistency here.

## Version

This function is available since SDL_mixer 2.0.0.

----
[CategoryAPI](CategoryAPI)

