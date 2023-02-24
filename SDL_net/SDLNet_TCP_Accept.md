====== (This function is part of SDL_net, a separate library from SDL.) ======
= SDLNet_TCP_Accept =

Accept an incoming connection on the given server socket.

== Syntax ==

<syntaxhighlight lang='c'>
TCPsocket SDLNet_TCP_Accept(TCPsocket server);
</syntaxhighlight>

== Function Parameters ==

{|
|'''server'''
|the server socket to accept a connection on.
|}

== Return Value ==

Returns the newly created socket, or NULL if there was an error.

== Remarks ==

<code>server</code> must be a socket returned by [[SDLNet_TCP_Open]] with
an address of INADDR_NONE or INADDR_ANY (a "server socket"). Other sockets
do not accept connections.

== Version ==

This function is available since SDL_net 2.0.0.

----
[[CategoryAPI]]


