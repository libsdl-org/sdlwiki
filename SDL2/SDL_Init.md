====== (This is the legacy documentation for stable SDL2, the current stable version; [https://wiki.libsdl.org/SDL3/ SDL3] is the current development version.) ======
= SDL_Init =

Initialize the SDL library.

== Syntax ==

<syntaxhighlight lang='c'>
int SDL_Init(Uint32 flags);
</syntaxhighlight>

== Function Parameters ==

{|
|'''flags'''
|subsystem initialization flags
|}

== Return Value ==

Returns 0 on success or a negative error code on failure; call
[[SDL_GetError]]() for more information.

== Remarks ==

[[SDL_Init]]() simply forwards to calling [[SDL_InitSubSystem]]().
Therefore, the two may be used interchangeably. Though for readability of
your code [[SDL_InitSubSystem]]() might be preferred.

The file I/O (for example: [[SDL_RWFromFile]]) and threading
([[SDL_CreateThread]]) subsystems are initialized by default. Message boxes
([[SDL_ShowSimpleMessageBox]]) also attempt to work without initializing
the video subsystem, in hopes of being useful in showing an error dialog
when [[SDL_Init]] fails. You must specifically initialize other subsystems
if you use them in your application.

Logging (such as [[SDL_Log]]) works without initialization, too.

<code>flags</code> may be any of the following OR'd together:

* <code>[[SDL_INIT_TIMER]]</code>: timer subsystem
* <code>[[SDL_INIT_AUDIO]]</code>: audio subsystem
* <code>[[SDL_INIT_VIDEO]]</code>: video subsystem; automatically initializes the events subsystem
* <code>[[SDL_INIT_JOYSTICK]]</code>: joystick subsystem; automatically initializes the events subsystem
* <code>[[SDL_INIT_HAPTIC]]</code>: haptic (force feedback) subsystem
* <code>[[SDL_INIT_GAMECONTROLLER]]</code>: controller subsystem; automatically initializes the joystick subsystem
* <code>[[SDL_INIT_EVENTS]]</code>: events subsystem
* <code>[[SDL_INIT_EVERYTHING]]</code>: all of the above subsystems
* <code>[[SDL_INIT_NOPARACHUTE]]</code>: compatibility; this flag is ignored

Subsystem initialization is ref-counted, you must call
[[SDL_QuitSubSystem]]() for each [[SDL_InitSubSystem]]() to correctly
shutdown a subsystem manually (or call [[SDL_Quit]]() to force shutdown).
If a subsystem is already loaded then this call will increase the ref-count
and return.

== Version ==

This function is available since SDL 2.0.0.

== Related Functions ==

:[[SDL_InitSubSystem]]
:[[SDL_Quit]]
:[[SDL_SetMainReady]]
:[[SDL_WasInit]]

----
[[CategoryAPI]]


