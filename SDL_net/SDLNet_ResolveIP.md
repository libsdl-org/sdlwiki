====== (This function is part of SDL_net, a separate library from SDL.) ======
= SDLNet_ResolveIP =

Resolve an IP address to a host name in canonical form.

== Syntax ==

<syntaxhighlight lang='c'>
const char * SDLNet_ResolveIP(const IPaddress *ip);
</syntaxhighlight>

== Function Parameters ==

{|
|'''ip'''
|the IP address to resolve into a hostname.
|}

== Remarks ==

If the IP couldn't be resolved, this function returns NULL, otherwise a
pointer to a static buffer containing the hostname is returned.

'''Warning''': This function is not thread-safe!

== Version ==

This function is available since SDL_net 2.0.0.

----
[[CategoryAPI]]


