====== (This is the documentation for SDL3, which is under heavy development and the API is changing! [https://wiki.libsdl.org/SDL2/ SDL2] is the current stable version!) ======
= SDL_GDKGetTaskQueue =

Gets a reference to the global async task queue handle for GDK, initializing if needed.

== Syntax ==

<syntaxhighlight lang='c'>
int SDL_GDKGetTaskQueue(XTaskQueueHandle * outTaskQueue);
</syntaxhighlight>

== Function Parameters ==

{|
|'''outTaskQueue'''
|a pointer to be filled in with task queue handle.
|}

== Return Value ==

Returns 0 if success, -1 if any error occurs.

== Remarks ==

Once you are done with the task queue, you should call
XTaskQueueCloseHandle to reduce the reference count to avoid a resource
leak.

== Version ==

This function is available since SDL 3.0.0.

----
[[CategoryAPI]]


