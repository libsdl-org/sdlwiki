###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)

## Draft

**THIS PAGE IS A WORK IN PROGRESS** ... Please make edits to this page to improve it!



<!-- #*^*^*^*^*See https://wiki.libsdl.org/SGFunctions for details on editing this page*^*^*^*^* -->
# SDL_TLSCreate

Create a piece of thread-local storage.

## Syntax

```c
SDL_TLSID SDL_TLSCreate(void);

```

## Return Value

Returns the newly created thread local storage identifier or 0 on error.

## Remarks

This creates an identifier that is globally visible to all threads but
refers to data that is thread-specific.

## Version

This function is available since SDL 3.0.0.

## Code Examples

```c++
static SDL_SpinLock tls_lock;
static SDL_TLSID thread_local_storage;

void SetMyThreadData(void *value)
{
    if (!thread_local_storage) {
        SDL_AtomicLock(&tls_lock);
        if (!thread_local_storage) {
            thread_local_storage = SDL_TLSCreate();
        }
        SDL_AtomicUnlock(&tls_lock);
    }
    SDL_TLSSet(thread_local_storage, value, 0);
}

void *GetMyThreadData(void)
{
    return SDL_TLSGet(thread_local_storage);
}
```

## Related Functions

* [SDL_TLSGet](SDL_TLSGet.md)
* [SDL_TLSSet](SDL_TLSSet.md)

----
[CategoryAPI](CategoryAPI.md), [CategoryThread](CategoryThread.md), [CategoryDraft](CategoryDraft.md)
<!-- #See the Style Guide for instructions on editing the footer. -->
