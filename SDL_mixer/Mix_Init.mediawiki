====== (This function is part of SDL_mixer, a separate library from SDL.) ======
= Mix_Init =

Initialize SDL_mixer.

== Syntax ==

<syntaxhighlight lang='c'>
int Mix_Init(int flags);
</syntaxhighlight>

== Function Parameters ==

{|
|'''flags'''
|initialization flags, OR'd together.
|}

== Return Value ==

Returns all currently initialized flags.

== Remarks ==

This function loads dynamic libraries that SDL_mixer needs, and prepares
them for use.

Note that, unlike other SDL libraries, this call is optional! If you load a
music file, SDL_mixer will handle initialization on the fly. This function
will let you know, up front, whether a specific format will be available
for use.

Flags should be one or more flags from [[MIX_InitFlags]] OR'd together. It
returns the flags successfully initialized, or 0 on failure.

Currently, these flags are:

* <code>[[MIX_INIT_FLAC]]</code>
* <code>[[MIX_INIT_MOD]]</code>
* <code>[[MIX_INIT_MP3]]</code>
* <code>[[MIX_INIT_OGG]]</code>
* <code>[[MIX_INIT_MID]]</code>
* <code>[[MIX_INIT_OPUS]]</code>
* <code>[[MIX_INIT_WAVPACK]]</code>

More flags may be added in a future SDL_mixer release.

This function may need to load external shared libraries to support various
codecs, which means this function can fail to initialize that support on an
otherwise-reasonable system if the library isn't available; this is not
just a question of exceptional circumstances like running out of memory at
startup!

Note that you may call this function more than once to initialize with
additional flags. The return value will reflect both new flags that
successfully initialized, and also include flags that had previously been
initialized as well.

As this will return previously-initialized flags, it's legal to call this
with zero (no flags set). This is a safe no-op that can be used to query
the current initialization state without changing it at all.

Since this returns previously-initialized flags as well as new ones, and
you can call this with zero, you should not check for a zero return value
to determine an error condition. Instead, you should check to make sure all
the flags you require are set in the return value. If you have a game with
data in a specific format, this might be a fatal error. If you're a generic
media player, perhaps you are fine with only having WAV and MP3 support and
can live without Opus playback, even if you request support for everything.

Unlike other SDL satellite libraries, calls to [[Mix_Init]] do not stack; a
single call to [[Mix_Quit]]() will deinitialize everything and does not
have to be paired with a matching [[Mix_Init]] call. For that reason, it's
considered best practices to have a single [[Mix_Init]] and [[Mix_Quit]]
call in your program. While this isn't required, be aware of the risks of
deviating from that behavior.

After initializing SDL_mixer, the next step is to open an audio device to
prepare to play sound (with [[Mix_OpenAudio]]() or
[[Mix_OpenAudioDevice]]()), and load audio data to play with that device.

== Version ==

This function is available since SDL_mixer 2.0.0.

== Related Functions ==

:[[Mix_Quit]]

----
[[CategoryAPI]]


