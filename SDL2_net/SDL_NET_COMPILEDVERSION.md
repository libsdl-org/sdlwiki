###### (This function is part of SDL_net, a separate library from SDL.)
# SDL_NET_COMPILEDVERSION

This is the version number macro for the current SDL_net version.

## Header File

Defined in SDL_net.h

## Syntax

```c
#define SDL_NET_COMPILEDVERSION \
    SDL_VERSIONNUM(SDL_NET_MAJOR_VERSION, SDL_NET_MINOR_VERSION, SDL_NET_PATCHLEVEL)
```

## Remarks

In versions higher than 2.9.0, the minor version overflows into the
thousands digit: for example, 2.23.0 is encoded as 4300. This macro will
not be available in SDL 3.x or SDL_net 3.x.

Deprecated, use SDL_NET_VERSION_ATLEAST or SDL_NET_VERSION instead.

----
[CategoryAPI](CategoryAPI), [CategoryAPIMacro](CategoryAPIMacro)

