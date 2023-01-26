====== (This is the legacy documentation for stable SDL2, the current stable version; [https://wiki.libsdl.org/SDL3/ SDL3] is the current development version.) ======
= SDL_AtomicLock =

Lock a spin lock by setting it to a non-zero value.

== Syntax ==

<syntaxhighlight lang='c'>
void SDL_AtomicLock(SDL_SpinLock *lock);
</syntaxhighlight>

== Function Parameters ==

{|
|'''lock'''
|a pointer to a lock variable
|}

== Remarks ==

'''''Please note that spinlocks are dangerous if you don't know what you're
doing. Please be careful using any sort of spinlock!'''''

== Version ==

This function is available since SDL 2.0.0.

== Related Functions ==

:[[SDL_AtomicTryLock]]
:[[SDL_AtomicUnlock]]

----
[[CategoryAPI]]


