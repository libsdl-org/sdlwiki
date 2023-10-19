###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_LockProperties

Lock a set of properties 

## Syntax

```c
int SDL_LockProperties(SDL_PropertiesID props);

```

## Function Parameters

|               |                        |
| ------------- | ---------------------- |
| **props**     | the properties to lock |

## Return Value

Returns 0 on success or a negative error code on failure; call
[SDL_GetError](SDL_GetError)() for more information.

## Remarks

Obtain a multi-threaded lock for these properties. Other threads will wait
while trying to lock these properties until they are unlocked. Properties
must be unlocked before they are destroyed.

The lock is automatically taken when setting individual properties, this
function is only needed when you want to set several properties atomically
or want to guarantee that properties being queried aren't freed in another
thread.

## Thread Safety

It is safe to call this function from any thread.

## Version

This function is available since SDL 3.0.0.

## Related Functions

* [SDL_UnlockProperties](SDL_UnlockProperties)

----
[CategoryAPI](CategoryAPI)

