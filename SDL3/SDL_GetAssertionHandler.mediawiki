====== (This is the documentation for SDL3, which is under heavy development and the API is changing! [https://wiki.libsdl.org/SDL2/ SDL2] is the current stable version!) ======
= SDL_GetAssertionHandler =

Get the current assertion handler.

== Syntax ==

<syntaxhighlight lang='c'>
SDL_AssertionHandler SDL_GetAssertionHandler(void **puserdata);
</syntaxhighlight>

== Function Parameters ==

{|
|'''puserdata'''
|pointer which is filled with the "userdata" pointer that was passed to [[SDL_SetAssertionHandler]]()
|}

== Return Value ==

Returns the [[SDL_AssertionHandler]] that is called when an assert
triggers.

== Remarks ==

This returns the function pointer that is called when an assertion is
triggered. This is either the value last passed to
[[SDL_SetAssertionHandler]](), or if no application-specified function is
set, is equivalent to calling [[SDL_GetDefaultAssertionHandler]]().

The parameter <code>puserdata</code> is a pointer to a void*, which will
store the "userdata" pointer that was passed to
[[SDL_SetAssertionHandler]](). This value will always be NULL for the
default handler. If you don't care about this data, it is safe to pass a
NULL pointer to this function to ignore it.

== Version ==

This function is available since SDL 3.0.0.

== Related Functions ==

:[[SDL_SetAssertionHandler]]

----
[[CategoryAPI]], [[CategoryAssertions]]
<!-- #See the Style Guide for instructions on editing the footer. -->


