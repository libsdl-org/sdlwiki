====== (This is the legacy documentation for stable SDL2, the current stable version; [https://wiki.libsdl.org/SDL3/ SDL3] is the current development version.) ======
= SDL_AddTimer =

Call a callback function at a future time.

== Syntax ==

<syntaxhighlight lang='c'>
SDL_TimerID SDL_AddTimer(Uint32 interval,
                         SDL_TimerCallback callback,
                         void *param);
</syntaxhighlight>

== Function Parameters ==

{|
|'''interval'''
|the timer delay, in milliseconds, passed to <code>callback</code>
|-
|'''callback'''
|the [[SDL_TimerCallback]] function to call when the specified <code>interval</code> elapses
|-
|'''param'''
|a pointer that is passed to <code>callback</code>
|}

== Return Value ==

Returns a timer ID or 0 if an error occurs; call [[SDL_GetError]]() for
more information.

== Remarks ==

If you use this function, you must pass <code>[[SDL_INIT_TIMER]]</code> to
[[SDL_Init]]().

The callback function is passed the current timer interval and the user
supplied parameter from the [[SDL_AddTimer]]() call and should return the
next timer interval. If the value returned from the callback is 0, the
timer is canceled.

The callback is run on a separate thread.

Timers take into account the amount of time it took to execute the
callback. For example, if the callback took 250 ms to execute and returned
1000 (ms), the timer would only wait another 750 ms before its next
iteration.

Timing may be inexact due to OS scheduling. Be sure to note the current
time with [[SDL_GetTicks]]() or [[SDL_GetPerformanceCounter]]() in case
your callback needs to adjust for variances.

== Version ==

This function is available since SDL 2.0.0.

== Related Functions ==

:[[SDL_RemoveTimer]]

----
[[CategoryAPI]]


