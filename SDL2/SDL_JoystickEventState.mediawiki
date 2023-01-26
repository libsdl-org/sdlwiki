====== (This is the legacy documentation for stable SDL2, the current stable version; [https://wiki.libsdl.org/SDL3/ SDL3] is the current development version.) ======
= SDL_JoystickEventState =

Enable/disable joystick event polling.

== Syntax ==

<syntaxhighlight lang='c'>
int SDL_JoystickEventState(int state);
</syntaxhighlight>

== Function Parameters ==

{|
|'''state'''
|can be one of <code>[[SDL_QUERY]]</code>, <code>[[SDL_IGNORE]]</code>, or <code>[[SDL_ENABLE]]</code>
|}

== Return Value ==

Returns 1 if enabled, 0 if disabled, or a negative error code on failure;
call [[SDL_GetError]]() for more information.

If <code>state</code> is <code>[[SDL_QUERY]]</code> then the current state
is returned, otherwise the new processing state is returned.

== Remarks ==

If joystick events are disabled, you must call [[SDL_JoystickUpdate]]()
yourself and manually check the state of the joystick when you want
joystick information.

It is recommended that you leave joystick event handling enabled.

'''WARNING''': Calling this function may delete all events currently in
SDL's event queue.

== Version ==

This function is available since SDL 2.0.0.

== Related Functions ==

:[[SDL_GameControllerEventState]]

----
[[CategoryAPI]]


