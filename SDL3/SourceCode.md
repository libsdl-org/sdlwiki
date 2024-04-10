# Obtaining SDL's source code


## Building and installation

Building and installing SDL for your platform (including how to obtain prebuilt binaries in some cases) is covered in [Installation](Installation).

## SDL 3.0

The source code to the latest official release of SDL3 is [here](https://github.com/libsdl-org/SDL/releases).

If you want up to the minute bug fixes and improvements, you can track our work in SDL's [Git](https://git-scm.com Git) repository, [here](https://github.com/libsdl-org/SDL). To clone the repo:

```bash
git clone https://github.com/libsdl-org/SDL
```

SDL3 is currently the "main" branch in git.

We intend official releases to be reasonably stable, and don't promise anything about the quality level of the Git repo from moment to moment, but as official releases tend to happen months apart, you might find a bug that's bothering you is fixed in revision control long before it makes it to a release.


## SDL 2.0 (legacy)

At the time of this writing, SDL2 has gone into maintenance mode, and will eventually be retired. Applications should move to SDL3 when possible.

It is still possible, for the time being, for there to be minor bugfix releases of SDL2, but these will stop sooner than later.

However, we offer [sdl2-compat](https://github.com/libsdl-org/sdl2-compat), a small library that provides the SDL2 API, using SDL3 behind the scenes. This is the recommended way forward for SDL2 apps that can't directly migrate to something newer at this point; it can even be used with existing binaries, by replacing the SDL2 shared library with sdl2-compat, or just setting the SDL_DYNAMIC_API environment variable to point to a copy of sdl2-compat.


## SDL 1.2 (obsolete!)

If you want SDL 1.2, the final released version is 1.2.15. We occasionally collect a fix or two in revision control, but our current intention is to never release an official 1.2.16 build, and while we may accept small patches, we do not intend to ever work on 1.2 again. You should expect it to continue to bitrot over time, and become a liability to your project. The best course of action is to move to SDL 3.0 or later as quickly as possible.

We have put together a [migration guide](SDL12MigrationGuide) to help with this.

Failing that, we offer [sdl12-compat](https://github.com/libsdl-org/sdl12-compat), a small library that provides the SDL 1.2 API, using SDL2 behind the scenes. This is the recommended way forward for SDL 1.2 apps that can't directly migrate to something newer at this point; it can even be used with existing binaries, by replacing the SDL 1.2 shared library with sdl12-compat. sdl12-compat can even chain through sdl2-compat, getting your 1.2 app all the way to SDL3's tech.

If you need the real (not sdl12-compat) SDL 1.2, you probably shouldn't use the last official release at this point. Instead, get the latest from revision control, which has accumulated some significant fixes since 1.2.15 was released.

You can find 1.2's source code in [a separate Git repository](https://github.com/libsdl-org/SDL-1.2):

```bash
git clone https://github.com/libsdl-org/SDL-1.2
```

