###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_StorageReady

Checks if the storage container is ready to use.

## Header File

Defined in [<SDL3/SDL_storage.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_storage.h)

## Syntax

```c
bool SDL_StorageReady(SDL_Storage *storage);
```

## Function Parameters

|                              |             |                               |
| ---------------------------- | ----------- | ----------------------------- |
| [SDL_Storage](SDL_Storage) * | **storage** | a storage container to query. |

## Return Value

(bool) Returns true if the container is ready, false otherwise.

## Remarks

This function should be called in regular intervals until it returns true -
however, it is not recommended to spinwait on this call, as the backend may
depend on a synchronous message loop.

## Version

This function is available since SDL 3.0.0.

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryStorage](CategoryStorage)

