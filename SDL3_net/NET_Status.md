###### (This function is part of SDL_net, a separate library from SDL.)
# NET_Status

A tri-state for asynchronous operations.

## Header File

Defined in [<SDL3_net/SDL_net.h>](https://github.com/libsdl-org/SDL_net/blob/main/include/SDL3_net/SDL_net.h)

## Syntax

```c
typedef enum NET_Status
{
    NET_FAILURE = -1,  /**< Async operation complete, result was failure. */
    NET_WAITING = 0,   /**< Async operation is still in progress, check again later. */
    NET_SUCCESS = 1    /**< Async operation complete, result was success. */
} NET_Status;
```

## Remarks

Lots of tasks in SDL_net are asynchronous, as they can't complete until
data passes over a network at some murky future point in time.

This includes sending data over a stream socket, resolving a hostname,
connecting to a remote system, and other tasks.

The library never blocks on tasks that take time to complete, with the
exception of functions named "Wait", which are intended to do nothing but
block until a task completes. Functions that are attempting to do something
that might block, or are querying the status of a task in-progress, will
return a [NET_Status](NET_Status), so an app can see if a task completed,
and its final outcome.

## Version

This enum is available since SDL_net 3.0.0.

----
[CategoryAPI](CategoryAPI), [CategoryAPIEnum](CategoryAPIEnum), [CategorySDLNet](CategorySDLNet)

