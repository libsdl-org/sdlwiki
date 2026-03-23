# How to report SDL bugs

## Where to report bugs in SDL

Bug reports for SDL can be posted at [the bug tracker](https://github.com/libsdl-org/SDL).

The bug tracker is our TODO list and our institutional memory; it's totally cool to ask about and discuss bugs on the forums, Discord, or by email, but we will almost certainly forget to deal with the problem if it's not open in the bug tracker.

## Don't use the bug tracker for questions

We have [various places](FAQCommunities) for discussion. Questions about SDL can be asked there, including "how do I use this?" and "am I using this correctly?"

These questions are better posted to those places, so they don't clog up the bug tracker and so others can benefit from them later.

## Tell us what platform you're using

SDL runs on a lot of platforms, and people often forget to mention which one they're using when they hit a bug. It's _extremely_ useful to say "I'm on Windows 10" or "I'm seeing this on macOS 15.4."

If you're dealing with a rendering bug, it's useful to report that you're using a specific 2D render backend (OpenGL, Direct3D 9, etc) or GPU API target (Vulkan, Metal, etc).

## Reporting memory leaks

Memory leaks happen, and we are happy to fix leaks in SDL. However, almost all leaks reported to our bug tracker are either leaks in other libraries that SDL uses, or intentional one-time allocations made by GPU drivers.

If you're using a memory leak tool, like AddressSanitizer or Valgrind, before reporting:

- Are you _sure_ this is an SDL leak? If the last thing in the callstack is not SDL, it's very likely it's a leak in a system library or graphics driver that SDL doesn't control. It's possible SDL is misusing a library, but almost always this either a bug or an intentional one-time allocation by that library. In particular D-Bus, Mesa, and NVIDIA drivers are known to have these. Please report these leaks to that library's maintainer instead of SDL, since we do not have the power to fix their leaks.
- If the leak is in SDL, it's often easy to identify where it's leaking and where it should be cleaned up. Please submit a PR with a fix if possible. Not only will this make it easy for us to confirm and accept your change, often in the process you may discover you're just not calling the code that cleans up the memory.
- If you're not able to tell where the leak should be cleaned up, please include symbols in your leak stack traces so we can see clearly what is happening.
