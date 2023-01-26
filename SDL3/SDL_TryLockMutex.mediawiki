====== (This is the documentation for SDL3, which is under heavy development and the API is changing! [https://wiki.libsdl.org/SDL2/ SDL2] is the current stable version!) ======

== Draft ==

'''THIS PAGE IS A WORK IN PROGRESS''' ... Please make edits to this page to improve it!
= SDL_TryLockMutex =

Try to lock a mutex without blocking.

== Syntax ==

<syntaxhighlight lang='c'>
int SDL_TryLockMutex(SDL_mutex * mutex) SDL_TRY_ACQUIRE(0, mutex);
</syntaxhighlight>

== Function Parameters ==

{|
|'''mutex'''
|the mutex to try to lock
|}

== Return Value ==

Returns 0, <code>[[SDL_MUTEX_TIMEDOUT]]</code>, or -1 on error; call
[[SDL_GetError]]() for more information.

== Remarks ==

This works just like [[SDL_LockMutex]](), but if the mutex is not
available, this function returns <code>[[SDL_MUTEX_TIMEOUT]]</code>
immediately.

This technique is useful if you need exclusive access to a resource but
don't want to wait for it, and will return to it to try again later.

== Version ==

This function is available since SDL 3.0.0.

== Code Examples ==

<syntaxhighlight lang='c'>
int status;
SDL_mutex *mutex;

mutex = SDL_CreateMutex();
if (!mutex) {
  SDL_LogError(SDL_LOG_CATEGORY_APPLICATION, "Couldn't create mutex\n");
  return;
}

status = SDL_TryLockMutex(mutex);

if (status == 0) {
  SDL_Log("Locked mutex\n");
  SDL_UnlockMutex(mutex);
} else if (status == SDL_MUTEX_TIMEDOUT) {
  /* Mutex not available for locking right now */
} else {
  SDL_LogError(SDL_LOG_CATEGORY_APPLICATION, "Couldn't lock mutex\n");
}

SDL_DestroyMutex(mutex);
</syntaxhighlight>

== Related Functions ==

:[[SDL_CreateMutex]]
:[[SDL_DestroyMutex]]
:[[SDL_LockMutex]]
:[[SDL_UnlockMutex]]

----
[[CategoryAPI]], [[CategoryMutex]], [[CategoryDraft]]


