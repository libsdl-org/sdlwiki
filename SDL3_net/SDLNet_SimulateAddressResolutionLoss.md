###### (This function is part of SDL_net, a separate library from SDL.)
# SDLNet_SimulateAddressResolutionLoss

Enable simulated address resolution failures.

## Header File

Defined in SDL_net.h

## Syntax

```c
void SDLNet_SimulateAddressResolutionLoss(int percent_loss);

```

## Function Parameters

|                      |                                                                          |
| -------------------- | ------------------------------------------------------------------------ |
| **percent_loss**     | A number between 0 and 100. Higher means more failures. Zero to disable. |

## Remarks

Often times, testing a networked app on your development machine--which
might have a wired connection to a fast, reliable network service--won't
expose bugs that happen when networks intermittently fail in the real
world, when the wifi is flakey and firewalls get in the way.

This function allows you to tell the library to pretend that some
percentage of address resolutions will fail.

The higher the percentage, the more resolutions will fail and/or take
longer for resolution to complete.

Setting this to zero (the default) will disable the simulation. Setting to
100 means _everything_ fails unconditionally. At what percent the system
merely borders on unusable is left as an exercise to the app developer.

This is intended for debugging purposes, to simulate real-world conditions
that are various degrees of terrible. You probably should _not_ call this
in production code, where you'll likely see real failures anyhow.

## Thread Safety

It is safe to call this function from any thread.

## Version

This function is available since SDL_Net 3.0.0.

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction)

