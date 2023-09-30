###### (This function is part of SDL_net, a separate library from SDL.)
# SDLNet_RefAddress

Add a reference to an [SDLNet_Address](SDLNet_Address).

## Syntax

```c
SDLNet_Address* SDLNet_RefAddress(SDLNet_Address *address);

```

## Function Parameters

|                 |                                                             |
| --------------- | ----------------------------------------------------------- |
| **address**     | The [SDLNet_Address](SDLNet_Address) to add a reference to. |

## Return Value

Returns the same address that was passed as a parameter.

## Remarks

Since several pieces of the library might share a single
[SDLNet_Address](SDLNet_Address), including a background thread that's
working on resolving, these objects are referenced counted. This allows
everything that's using it to declare they still want it, and drop their
reference to the address when they are done with it. The object's resources
are freed when the last reference is dropped.

This function adds a reference to an [SDLNet_Address](SDLNet_Address),
increasing its reference count by one.

The documentation will tell you when the app has to explicitly unref an
address. For example, [SDLNet_ResolveHostname](SDLNet_ResolveHostname)()
creates addresses that are already referenced, so the caller needs to unref
it when done.

Generally you only have to explicit ref an address when you have different
parts of your own app that will be sharing an address. In normal usage, you
only have to unref things you've created once (like you might free()
something), but you are free to add extra refs if it makes sense.

This returns the same address passed as a parameter, which makes it easy to
ref and assign in one step:

```c
myAddr = SDLNet_RefAddress(yourAddr);
```

## Thread Safety

It is safe to call this function from any thread.

## Version

This function is available since SDL_Net 3.0.0.

----
[CategoryAPI](CategoryAPI)

