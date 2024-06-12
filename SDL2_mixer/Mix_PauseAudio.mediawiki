====== (This function is part of SDL_mixer, a separate library from SDL.) ======
= Mix_PauseAudio =

Suspend or resume the whole audio output.

== Header File ==

Defined in [<SDL_mixer.h>](https://github.com/libsdl-org/SDL_mixer/blob/SDL2/include/SDL_mixer.h)

== Syntax ==

<syntaxhighlight lang='c'>
void Mix_PauseAudio(int pause_on);
</syntaxhighlight>

== Function Parameters ==

{|
|int
|'''pause_on'''
|1 to pause audio output, or 0 to resume.
|}

== Version ==

This function is available since SDL_mixer 2.8.0.

----
[[CategoryAPI]], [[CategoryAPIFunction]]


