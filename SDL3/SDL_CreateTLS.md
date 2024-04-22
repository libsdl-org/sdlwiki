###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_CreateTLS

Create a piece of thread-local storage.

## Header File

Defined in [SDL_thread.h](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_thread.h)

## Syntax

```c
SDL_TLSID SDL_CreateTLS(void);

```

## Return Value

Returns the newly created thread local storage identifier or 0 on error.

## Remarks

This creates an identifier that is globally visible to all threads but
refers to data that is thread-specific.

## Version

This function is available since SDL 3.0.0.

## Code Examples

```c
// BEWARE: This code example was migrated from the SDL2 Wiki, by only updating the names.

static SDL_SpinLock tls_lock;
static SDL_TLSID thread_local_storage;
void SetMyThreadData(void *value)
{
    if (!thread_local_storage) {
        SDL_LockSpinlock(&tls_lock);
        if (!thread_local_storage) {
            thread_local_storage = SDL_CreateTLS();
        }
        SDL_UnlockSpinlock(&tls_lock);
    }
    SDL_SetTLS(thread_local_storage, value, 0);
}
void *GetMyThreadData(void)
{
    return SDL_GetTLS(thread_local_storage);
}

```

## See Also

* [SDL_GetTLS](SDL_GetTLS)
* [SDL_SetTLS](SDL_SetTLS)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction)

