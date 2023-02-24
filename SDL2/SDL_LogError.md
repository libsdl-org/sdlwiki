====== (This is the legacy documentation for stable SDL2, the current stable version; [https://wiki.libsdl.org/SDL3/ SDL3] is the current development version.) ======
= SDL_LogError =

Log a message with [[SDL_LOG_PRIORITY_ERROR]].

== Syntax ==

<syntaxhighlight lang='c'>
void SDL_LogError(int category, SDL_PRINTF_FORMAT_STRING const char *fmt, ...) SDL_PRINTF_VARARG_FUNC(2);
</syntaxhighlight>

== Function Parameters ==

{|
|'''category'''
|the category of the message
|-
|'''fmt'''
|a printf() style message format string
|-
|'''...'''
|additional parameters matching % tokens in the '''fmt''' string, if any
|}

== Version ==

This function is available since SDL 2.0.0.

== Related Functions ==

:[[SDL_Log]]
:[[SDL_LogCritical]]
:[[SDL_LogDebug]]
:[[SDL_LogInfo]]
:[[SDL_LogMessage]]
:[[SDL_LogMessageV]]
:[[SDL_LogVerbose]]
:[[SDL_LogWarn]]

----
[[CategoryAPI]]


