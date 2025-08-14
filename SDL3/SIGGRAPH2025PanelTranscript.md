# SIGGRAPH 2025 Panel Transcript

## Audio

The audio from this panel can be downloaded as [an MP3 file from libsdl.org](https://libsdl.org/siggraph2025/SIGGRAPH_2025_SDL_GPU_Panel.mp3).

## Transcript

SIGGRAPH 2025
Using the SDL GPU Graphics API in Education

Participants

- Sanjay Madhav, USC
- Matt Whiting, USC
- Mike Shah, Yale
- Evan Hemsley, SDL GPU Project Lead

***Sanjay:***
So, yeah, so first we're going to have, Mike's going to talk a little bit about just his experiences teaching computer graphics, especially interactive graphics, kind of the way he teaches his class right now, and kind of what are the benefits, challenges, etc.

***Mike:***
Yeah, so I've been teaching graphics for the past seven or eight years, kind of the same way. We start off with using an API, something like SDL to get a window up. As we just stick around, there's a built in 2D API that lets students start building games. These types of things, getting a great way to just get familiar with the API. And then I've been using OpenGL from that to create a context or you could again choose DirectX, and of course, there’s Metal, Vulkan, we'll get to that stuff later. But we've kind of been stuck in OpenGL 4.1 land because that's where we support Mac, Windows, Linux. That's what every student has and we can kind of support them. But as you've know, being here at this conference, there's Vulkan, Metal, DirectX 12, other new and exciting stuff. And industry wants folks, you know, you guys, us to be using that new tech, right, so we can get the latest performance and advantages there.

So the challenge is, how do you take somebody who doesn't know anything about graphics straight to a 1000 line Vulkan program to create a window?

***Evan:*** A thousand lines is... conservative.

***Mike:***
Yeah. That's like no comments, spacing. So the challenge is, how do we bridge that gap? I think we're going to talk a lot more about that, but we need some sort of stepping stone. And, I mean, feel free to dive in on this, but I still think OpenGL is great API to just learn graphics. In fact, if you're just learning graphics, learning what a depth buffer is, this idea of what a shader is, these types of things, great, just go to OpenGL, something where there's lots of resources, the modern API, and sort of teach that. So I try to teach those two big ideas. Shaders and buffers in my courses. You pack some data, load it up in a buffer, send it over to the GPU. Create a shader program, that executes what's on that data. Those are the two big ideas. But now we have three big ideas, at least with the modern APIs of command buffers and render buffers, which adds a little bit more complexity, or rather going from a 100 lines to what do we say, more than a thousand lines of code. That's tough on students. So that's kind of the challenge, how do we ramp somebody up? And SDL3 is going to help with that, but I'll kind of stop there.

***Sanjay:***
All right, yeah, and so kind of to build on that a little bit, I think. So to really harp on the platform agnostic-ness of the OpenGL 4.1, because really, like, in my classes, you know, at least half the class is Macs, right? So if we teach DX11 or DX12, we have to deal with the fact that what are the Mac students going to do? And you can't do BootCamp anymore. So there's all that. I think the other advantage also is like, you, if you stick to, like OpenGL 4 or 4.1, and like the subset that specifically works with ES2, you can also build for WebGL pretty easily. So being able to have a web based one works. WebGL works reasonably well on most browsers. So it's a cool way, like in our kind of video game programming class. To find a way to just be able to ship a build to the students because they can just play it on the website. And it's good for their portfolios because they can make their build, put it on their website. That's great for that.

So I'm talking a little bit about, so what is SDL? So a few of you said you use it at work, and Mike referenced it a little bit, but SDL is basically a platform library for games. So let's say you didn't use something like SDL, and let's say you wanted to make that basic hello triangle OpenGL program. Well, the first problem is, okay, I need to make a window, right? And then it's like, well, if I make a window on Windows, I have to use Win32 API, or something like that. If I want to make a window on Mac, I may have to write some Objective-C and be very sad about that.

Everyone: *laughter*

***Sanjay:***
Yeah. And if I'm on Linux, it's going to be like X11 or or Wayland, and then you think about, what about other platforms? I want to do a PS5 game or a Switch game or iOS and all these platforms. And it's like, I don't want to write like eight different, "I create a window" code, but that's what you have to do if you don't use a library. There are other options like GLUT or something like that, but that's not really supported anymore. So the great thing about SDL is it’s platform layer, specifically designed to be high performance, specifically designed for games. So as Mike referenced for a long time, they've had a 2D rendering API that you can use if you will make sprite based games. It's really simple to just render some textures and do your sprite based games. But it's not only graphics, right? It's like platform stuff, it's like file IO, it's audio, it's controller, joystick, threading, input, you know, So all the stuff that like, it makes it so that you, especially as an independent developer, you don't have to write all this code yourself, right? And actually, like, I don't know if this is still the case, but at least in earlier versions of Unreal 5, the Linux port of Unreal 5 actually used SDL.

***Evan:*** Yeah, it did, yeah.

***Sanjay:*** I don't know if they still do that.

***Evan:*** I don't know either, but it wouldn't surprise me.

***Sanjay:***
Yeah. So, it's kind of there, and it's, you know, for the open source version, right, it's supported on, you know, PC Mac Linux, it's supported on iOS, Android, the Xbox code is actually open source now because Microsoft is like you can open source that, they don't care. There is actually a PlayStation 5 and PlayStation 4, Switch ports, but those are, you need like the NDA or whatever. Yeah, but reasonably any platform that you want to develop for, emscripten, web works, right? So you can develop for it. And so the idea is that it kind of takes that pain away from, okay, well, I want to make this game. I don't want to write, like 10 different windowing code. But for a long time, there still was the problem of, okay, I want to do 3D graphics now. SDL did not support 3D graphics for a long time. So it meant that then you were back in the scope of like, okay, well, maybe we can use OpenGL, but like, if I want to support, I dunno, like compute shaders, I can't do OpenGL 4.1, right? And then it's like, well, then I need Metal for Mac and then you like, get the same problem space where as a small team, you don't want to deal with all that. And as an educator, I don't want to have two different sets of instructions for everyone in the class, "Oh, you're a Mac student. You do these instructions. You're a PC student, etc.” And basically, you're teaching like two different classes simultaneously with the headache that comes from that.

So for the SDL3 release, one of the big features that they were adding is an SDL GPU API, which Evan was the co-author of. So he's going to talk a little bit now about kind of what were his goals from the outset, how we kind of realized it also works well with education, and then also just like, what's the design philosophy and kind of how does it work.

***Evan:***
Yes, so yeah, again, I’m Evan and I was the project lead for SDL GPU and I'll have to shout out my co-designer, Caleb Cornett, who couldn't make it, but he was also instrumental in helping me design it. So thanks to him.

So my graphics background started with XNA and have any of you used XNA, maybe? Okay, yeah, we got … Wow, awesome. Cool. So yeah, for those that don't know, it was a game framework developed by Microsoft to facilitate game development on Windows and Xbox 360, particularly for indie developers. So it became quite popular among indie developers in the late 2000s, early 2010s, because you could use it to independently publish a game on their online store, Xbox Live Indie Games. And it was discontinued in 2013. So around, I want to say 2014 or 2015, a guy called Ethan Lee, he forked MonoGame and began maintaining a project that he called FNA. And FNA is just a free, open source reimplementation of XNA. So all of the library calls are exactly the same. We just did a clean room implementation, and it's been used to ship hundreds of SKUs now, including indie hits like Celeste, Terraria, FEZ, on platforms that were not initially supported by XNA, like Linux and Nintendo. So our work on FNA ensures that those games are going to be preserved on modern platforms, even though Microsoft abandoned XNA.

So FNA was developed with SDL as the platform layer. So our needs became very entwined with SDL, and we started contributing a lot of patches. Like Ethan designed a bunch of subsystems, and I think all three of us FNA maintainers, we all have maintainer access to SDL now because we just work on it all the time. So I wrote FNA's initial Vulkan backend, which has now been replaced by SDL GPU. But that was in 2020. And, you know, if you've never used XNA, the graphics subsystem is very much like a DX9 era API, like similar to like OpenGL2. And with all the, you know, restrictions that entails. So in the process of implementing XNA graphics on top of Vulkan, I became very deeply acquainted with all of the inefficient things that it does. And so I had to make all these restrictive assumptions about like data transfer and threading, the rules about that stuff were pretty opaque to the client. There were things that like you couldn't do or it would crash. So what I realized was that in the guise of simplifying the mental model for the client about how the GPU works, it sort of makes it harder to actually understand how the GPU works, especially as you become more skilled, you have more techniques in your toolbox. You start to get to a place where there's things that you can't do efficiently with the API that it exposes. So I just found myself thinking over and over, like, oh, if I could just change this function and add, like, two more variables, this could be so fast, but I can't do that because it's a preservation project. So that experience led me to start creating a new graphics library.

We heard that Ryan and the team were wanting to do a GPU abstraction. But they were getting bogged down and they were like, okay, we're not going to ship it in initial SDL 3. And all of us on the FNA team, were like, no, we need that! So, uh, so because I had worked on something independently for a while, I looked at Ryan's proposal and his API structure was very similar to the one that I had already started designing and implementing. So we just opened a pull request, and, you know, many, many months of revisions later, here we are. It's upstream, it's in SDL3.

So… in the early days of Vulkan being announced, we were hoping that, like we had heard rumors of like a "glNext" that Khronos was working on. And we were like, oh, great, because, you know, OpenGL has these problems, especially with like, you know, like the fact that the driver has to bundle a shader compiler, like all this crazy stuff. So we were like, okay, like, maybe glNext will take us into the future. But the reality was that the design of Vulkan really swung the complexity pendulum in the complete opposite direction of OpenGL. So the design of it was driven by industry leading, bleeding edge, AAA graphics engineers who wanted to expose everything that a GPU could possibly do. Like they don't care about like nice little abstractions. Like they just want raw performance and power and control. So that makes sense if you're working as a AAA graphics engineer, for the rest of us, it's a little hard to use.

So, like consider, for example, like, if you want to create a texture in Vulkan, you have to call vkCreateImage, and then you have to call vkAllocateMemory, and you have to use the correct memory heap index based on querying the optimal memory properties from the GPU, then you have to call vkBindImageMemory, and then you can finally use a texture. If you do that, it's still actually not optimal, because what you're supposed to do is allocate a lot of memory, and then start suballocating it. You're supposed to write your own suballocator and then when you delete resources, there's fragmentation, so now you have to write a defragmenter. So imagine teaching that, you know, four weeks into a college class.

***Mike:***
Yikes, yeah.

***Evan:***
So, and there's external libraries that help you with that stuff, but, you know, they’re C++ only. They require configuration and integration into your application. So the fact that there's even a separate library for something like binding image memory, I think just speaks to how complex Vulkan is and how you don't really want to do that. So even beyond the fact that it's hard to write a correct Vulkan program, it's also like even harder if you want to actually apply best practices.

So I work primarily with small teams that ship cross-platform games. Like we want to ship on any platform that you could want. And so for many of these developers, like they're not using a game engine or they don't want to. It's not appealing because of licensing costs or the complexity of the engine or they don't like the engine or they don't like that it doesn't have source code or their workflow doesn't mesh well with the team or whatever. But then the overhead of maintaining a Direct X12 renderer, a Vulkan renderer, a Metal renderer, whatever PS5 is doing, long term, with APIs that complex, it's just, like, not reasonable for teams like that. Like most of them don't have a full time graphics engineer or something.

So, for me, FNA was a good model for how to thread that needle, because it has an API surface that it gives you a lot of explicit control, you're manually, you know, you're creating resources, you're issuing draw calls, you're binding resources. But then, the way we implement it on FNA was that, you know, we had the you have the surface level APIs that you're calling, and then we would implement the backend abstractions. So like, okay, we're translating the calls into Vulkan, we're translating the calls into Metal. So my goal for SDL was to target roughly that level of API complexity, but then expose stuff that we couldn't expose in FNA like command buffers, explicit data transfer, compute shaders. Like that's all stuff we can do now. So, yeah, I designed this for the needs of like, small teams and hobbyist developers, but the qualities that make it good for that also, I think, make it good for education. So that's why we're here today.

So really quick. I just want to break down, like, the design philosophy that we used to design SDL GPU. So our three main goals were maximum portability. We want you to write your application code one time, and then it will… You can reasonably expect that it will run the exact same way on any platform you develop on. So Windows, MacOS, iOS, Linux, Android with some limitations, because Android sucks. Nintendo, PS5, Xbox. So any platform you'd want to ship a commercial game on, like we want you to write code once and then deploy it and you have a reasonable expectation it will work the same way. So if a feature is missing on one backend or it doesn't have wide support with the hardware, like we just would cut it, we don't support that. So we would only expose features that would work the same way on all the backends. So that was goal one.

We wanted to design the API so there was only one way to do something correctly. So we tried to design it so that the best practice way of doing something would just be like automatically the way that we did it in the back end. So, like I mentioned Vulkan memory allocation. Like we do all that for you. Like we chunk out the allocations, we defragment it for you, like we do all of that and you don't have to think about it. We also wanted to avoid exposing features that would require you to have multiple code paths to deal with different kinds of hardware. So, for example, if you're on like a Nintendo Switch, they have unified memory architecture, so they don't make a distinction between system memory and GPU memory. So you could do stuff like instantly copy memory or like you could instantly have memory live in a buffer, like without having to do any kind of data transfer. We don't support that just because not all hardware is designed that way. So you would have to write two different code paths to support the two different kinds of hardware. And we don't want you to have to worry about that.

My other goal was to expose how the GPU works to the client through the API, so I wanted the fact that a GPU is a separate processor to be very clear in the API. So you're filling a command buffer with commands, when you fill up the command buffer, you submit it. You optionally get a fence in return. So that's all that's communicating to you these draw calls are happening on a separate execution timeline from the CPU. It's not like you call draw and then the draw call immediately happens, which I think is the assumption that a lot of people make, like when you're using OpenGL or something like that. I wanted it to be very clear that this is like a separate processor that's executing these commands. I also wanted to make it really clear how data is transferred between CPU memory and GPU memory. So we always make that data transfer execute on the GPU timeline. It makes it a lot easier to reason about.

So lastly, I'll just say that we published SDL3 in January and through FNA, we have tested the GPU API very thoroughly. We've actually shipped a project on every single platform that we claim to support. So it's not just a hobby project, it's not a toy. This is production quality software. You can ship games with it. For students, you know, it's not like you could maybe put SDL GPU on your resume, like, you know, maybe they're not going to hire you at DICE for that or something. But I think that learning it, you'll have an understanding of the execution model of the GPU, how data transfer works, you'll know what a buffer is, you'll know what memory alignment is, you'll understand the overall structures of rendering and you're not going to have to learn, like, what a descriptor heap is. So, yeah, that's what I've got.

***Sanjay:***
Great. There’s a question.

***Audience member:***
Do you have a semantic for pipeline barriers or anything like that?

***Evan:***
Yeah, good question. So we decided to handle all of that automatically. So, like, basically you're inserting commands in linear order, and we just assume that, you know, if you bind a resource to a compute shader and then you read that resource in a graphics pipeline later, we just insert a barrier for you. Yeah.

***Sanjay:***
So now Matt's gonna talk a little bit, so Matt's been hard at work this summer, actually, prototyping our game engine programming class, so he's going to talk a little bit about the way that he used to teach it, what are some of the challenges and how’s it going, converting over to using SDL GPU.

***Matt:***
All right, so yeah, so one of the classes that I teach is game engine programming, which is sort of similar to graphics programming. A lot of game engines is graphics. So what my main goal for the class, in terms of graphics, is sort of what Evan was just saying, is, I want the students... I've been teaching in a DirectX 11, actually, for I don't know, for years. And I always tell them, I'm not trying to teach you DirectX 11. I'm trying to teach you how a real graphics pipeline works. So what I want you to know, I want you to know that there's a CPU and there's a GPU, and those are separate. And if we want the GPU to do something, first, we have to send the data over, and then we have to describe it, we have to give it the commands in this order and make it draw the thing. So my goals are every student understands writing shaders, they understand binding resources, they understand the order things have to go and how we're setting up command buffers that ultimately will be sent across the pipe and then executed on a separate timeline.

So what I've been doing is DirectX 11 for that, and there's two problems with that. One is DirectX 11, is getting a little old. But the real problem is it's a blocker for the Mac users. Half the class comes in with a Mac, and originally I would tell just set up BootCamp, boot it as Windows and let's roll. And then, Apple Silicon came out, and we weren't able to do that anymore. And so we've been having the students check out loaner laptops from the department. And it's not ideal. So I want to maintain something that teaches those fundamentals of how an actual graphics pipeline works, and somehow still support the students with Macs, and how am I going to do that? So, yeah, we kicked around all kinds of things. Let me go OpenGL. I said, "Well, should I convert it to open GL?" And I would always ask, you know, my industry contacts, should I switch this class to open GL? Presumably, we can still teach these same concepts, in OpenGL. And they all freak out. They all say, no! No, don't teach them that. And so, I never have converted. Been keeping it in DirectX 11, and I would always say, well, do you need DirectX 11? And so far, the feedback has been DirectX 11 is fine. We can go from there. So that's great, but I still have this problem that half the class come in with Macs.

So enter SDL. Could SDL make that bridge for me instead of OpenGL? Could SDL GPU be this layer that allows me to target both the Windows and the Mac users in an almost completely unified way that I don't have to run two separate classes learning two separate APIs for everything. And so yeah, I've started trying it out and yeah, it seems like it's working pretty well. We'll be teaching in the spring, and this spring, I will teach that class, and we're going to try doing it in SDL. The immediate pushback that I'm feeling is, okay, well, I thought you wanted to teach the students the real industry standard, like something that they could immediately apply to a graphics job. And my answer there is the same as it always was, which is, you're probably I mean, you might go to a place where we're using DirectX 11, but aren't you going to be using PlayStation? Like, aren't you going to be targeting PlayStation or Switch or something else? I don't think it's really my goal to teach you the API, that you'll ultimately use in your career. When I've been trying to do is teach you the fundamentals. Yep.

***Audience member:***
Never mind.

***Matt:***
You want to hold it? Okay, okay, yeah, I want to teach the fundamentals that, like, for example, I don't need you to memorize the API command to bind a vertex buffer. Right? But I need you to understand that there's something called a vertex buffer and that you'll need to bind it. And so that you can then hit your tech specs for the language that you are using, for the API you are using, and just search it. Search vertex buffer through the technical specifications on the PlayStation, right? When you get on the PlayStation team and you know enough that that's the keywords you're looking for. And when you find it, you'll see you see the command and what the format of it is and be able to read that and understand how to apply that. And indeed, that is the command that you'll find in SDL. So SDL doesn't make you do all the window. So to open a window, it's like three lines of code. SDL_Init, and then you do create window. SDL_CreateWindow, and then you do SDL_ClaimWindowForDevice or something like that, right? So bang, bang, bang. We made a window, and we don't have to worry about that, because that's not what we're interested in. But like to make a vertex buffer, we'll make vertices, make an array of vertices, and then you'll say, create that as a vertex buffer, declare it with the kind of kind of parameters that you expect to specify. And then you can send it with the draw command, right? Issue a draw command. Well, create a command buffer, right? You will create a command buffer, and then onto the command buffer, you'll submit a draw command, and then you'll submit the command buffer, and then it'll go.

So yeah, it's been pretty smooth, very similar in level to where DirectX 11 is in terms of how many commands you have to issue in order to get something to come out. But using either a Vulkan or a Metal backend there seamlessly, which is pretty cool.

***Audience member:***
For the API, what about the shader language? Like, do students have to learn a new shader language?

***Matt:***
Yes, absolutely. We're gonna have to learn a shader language. In my class, we've been doing HLSL, and I'm just going to stick with that. That's fine.

***Evan:***
Yeah, so basically, yeah, that's a good question. Because obviously every backend takes a different kind of shader bytecode. So our approach to that was basically to, we don't want to force a high level language on you. So already with HLSL, you get a compiler that can compile to SPIR-V. We have SPIRV-Cross, which can give you MSL from that. You can compile HLSL to DXIL, which is the DirectX 12 bytecode. So just from there, you can have one high-level language and you'll get every bytecode. We don't care if you generate SPIR-V from GLSL. We don't care if you generate it from Slang. Like, what you do basically is when you're initializing the GPU device in SDL, we ask you to list out the bytecode formats that you can provide in your application, and then it'll just pick the best backend based on that. You're like, okay, I have SPIR-V shaders and SDL will say, okay, I will start a Vulkan backend. So that's how it works.

***Matt:***
Yeah. So in my case, I'm saying initialize it with Vulkan or Metal. You say, I'll accept Vulkan or Metal, and then we'll load, actually, I do it in class. We compile the shaders live in the code. So you'll load the text of the HLSL, compile it to SPIR-V, and then run the shadercross, and then SDL will know whether it has created a Vulkan or it has created a Metal version and create the the correct bytecode. So then now you have the bytecode that you continue with.

***Evan:***
That's the other thing I didn't mention yet, is that… So we have a satellite library called SDL_shadercross, and we basically, we bundle DXC and SPIRV-Cross, and it gives you reflection capabilities. You can do online runtime compilation of shaders. So the reason we couldn't provide that directly in the SDL API is that SDL has a very strict no dependencies policy. So we can't just pull in like the whole DirectX shader compiler. So we made a satellite library for that and it's optional. Like you can you can also use shadercross with a command line interface and just do, like, you can just pre-compile your shaders into bytecode and then load those at runtime. You don't have to do the online workflow. So we tried to keep things very flexible with shaders because we know that people have a lot of different preferences for how they like to use shaders. So I didn't want to say, okay, you have to use GLSL or something like that.

***Audience member:***
Let’s say I want to teach my students with shaders, is there right now an example that for instance has some script that combines both libraries that will allow me to just have the whole pipeline, have the shader code, and it goes into the SDL pipeline? Is there something like that?

***Evan:***
Yeah, we have an examples repository on GitHub. It's called, I think it's just called SDL_gpu_examples, and it has a shadercross workflow, integrated into it. So like that would probably be a good starting point.

***Matt:***
Yeah. I guess, what else should I say? Super important, I am teaching RenderDoc this time. I've been… since it was always Windows focused, and Visual Studio focused up until now, I was using Visual Studio Graphics Analyzer and teaching that to students, which is huge, by the way. You got to teach it.

***Sanjay:***
It doesn't work in DirectX 12.

***Evan:***
It doesn't, yeah.

***Matt:***
But yeah, that's not going to work for Vulkan. It's not going to work for the… Well, I'm still screwed on Mac… But one piece of feedback I did get from industry folks is that's cool that they're learning that concept, but go ahead and teach them, RenderDoc, because that's what we want to use. We'll mostly start with RenderDoc. So, yeah, we'll teach RenderDoc this time on the Windows, but there's still no Mac for that. So we're stuck with Xcode.

***Sanjay:***
That's your summer... rest of the summer project. Who wants to port RenderDoc to Mac?

*Audience laughter*

***Matt:***
Oh, yeah, anybody wants to port RenderDoc over to Metal?

***Sanjay:***
Yeah. Allegedly at some point in the last like three years, it did compile on Mac. Allegedly, according to the pull request, it compiled at some point, it's just you couldn't actually, you could open the program, but then it couldn't do anything.

***Matt:***
Yeah, right. So, yeah, we will have to teach the... that part of the class. I'm going to have to teach twice. I'm going to have to teach the Windows users to use RenderDoc, and then the Mac users will have to sit through that, and then I'll have to teach them, okay, here's the equivalent in Xcode. You can do all the things just totally different UI.

***Sanjay:***
And I think also one things the question about, well on your resume, if you put down SDL GPU, most people are going to be like, "Well, what's SDL GPU?” But Matt has a really good solution to that, which is like, you don't put down there, oh, I wrote an engine with the renderer in SDL GPU. You're like, oh, I wrote an engine with a Metal and Vulkan backend via SDL GPU or something, right? So it's like, because if you just drop the name, it's like, look, it is actually using Metal and Vulkan. It's just you're not directly interfacing it, but to the point is like, you are learning all the concepts, like command buffers and creating resources and resource transfers and so like all the concepts are there, even if you're not getting to the point of like… I don’t know if anyone has gone through the pain of trying to write DirectX 12 code yourself…

***Evan:***
I have!

***Sanjay:***
It’s like, what type of heap do I need? No, that's the wrong type of heap. You have like, five different heaps and I have to manage them all myself. Yep. You were going to say something.

***Mike:***
Oh, yeah. Well, yeah, just on that too, yeah, you want to hit the keywords on your resume search, super important, if you're job hunting. I was going to ask, when do you introduce… Well, first question, how many folks have used Renderdoc? Yeah, awesome. Yeah. I mean, this is a great audience. When do you introduce Renderdoc to your students? First triangle?

***Matt:***
No, no, no. Although some of them get stuck before before I teach it. Yeah. And so they get a preview. *Laughter* They get a preview of it when they're just like, how come my triangle is not on screen? It's like, well, we don't normally cover this, but do this. So first we do a triangle, then I draw a cube with a texture on it, and then we do lighting, and then I have them do some stuff, and then we do at the lighting phase, I'll pause and we'll say, okay, this is this is where the RenderDoc fits in.

***Mike:***
Yeah, there's enough interesting stuff there, yeah.

***Matt:***
Yeah, I think that's where I usually stop around.

***Sanjay:***
So that’s around like week six, seven something.

***Matt:***
Well, so week one is just a math library. And then week two is draw triangle. Week three is the textured cube. Week four is the lighting. So week four.

***Mike:***
So great hack as you're learning, especially in a new API to pop in a debugger, see the steps. I was wondering, is that also useful for SDL GPU if you pop open RenderDoc?

***Evan:***
I use it all the time. I could not do anything I do without it. Yeah.

***Matt:***
Because it's like a Vulcan or a DirectX 12 backend. RenderDoc doesn't know that it's SDL. It doesn't care.

***Evan:***
Yeah. It's just looking at the Vulkan calls. So I guess, you know, one thing you could say is like, oh, well, like, you know, you're just looking at the, you're just seeing the Vulkan calls in RenderDoc, even if you're using SDL GPU. And that's true. But I think there's enough kind of like reverse mapping there where you can say like, okay, here's my draw call. Oh, the thing isn't showing up. And then you can start inspecting the event.

***Sanjay:***
Do you think there's an option for adding an optional flag when you create the GPU renderer where you could insert events?

***Evan:***
We already have that. Yeah, we do. You can insert debug events and labels already. So, yeah.

***Sanjay:***
So that will help also narrow down which Vulkan calls map to it.

***Evan:***
Right. Yeah. You can do that.

***Matt:***
Yeah, but to be honest in my class, I mean, in class, I told you, it's a triangle and a cube.

***Evan:***
So if it's not showing up...

*Laughter*

***Matt:***
Although I am always a little bit surprised. It's like Groundhog Day every year. I'm always surprised that when I say, find the draw call that is your cube, it's not obvious to them that the one with 36 vertices is the cube. The one with three vertices is the triangle.

***Sanjay:***
I think the other thing that also helps like sell them on how important it is… I like to do this one, I haven't taught the class in a while, but one thing I like to do when I introduce RenderDoc or something like that is like, okay I took a frame capture of, I don't know, Grand Theft Auto 5 or something…

***Matt:***
I still use those slides.

***Sanjay:***
Yeah, you still have the slides… So it's like, show them how it looks. You can actually step through. Like, you take any commercial game, you can run through RenderDoc. We can see how like, what are the tricks are and we can see like, oh, like they're doing the transparency here and they're doing. This is how the deferred lighting works. And so I think like that really, like, I think that's, that kind of gives them the aha moment where they're like, oh, it's not just something we're learning just for fun or just because the professor's mean or whatever. It's because like they're actually like, this actually makes sense that this is how you can actually, I mean, in a way, you can reverse engineer the tricks that all these other games are doing.

***Evan:***
Don't tell Baldur Karlsson you're doing that, though, or he'll get upset.

***Sanjay:***
Yeah, yeah. Technically, he's like, you're not really supposed to use the link into spawn processes mode.

***Evan:***
Yeah. Right.

***Sanjay:***
He’s the creator of Renderdoc. Also,  just in case, I think we mentioned Ryan. So Ryan is Ryan Gordon, one of the two primary maintainers of SDL, the other being Sam Lantinga. Sam works at Valve and Ryan… They both work at Valve? Sam is definitely at Valve… I think Ryan’s independent now… yeah, but SDL’s been around for a long time. Like probably 20 plus…

***Mike:***
27 years?

***Evan:***
I think it's 27 years, yeah.

***Sanjay:***
So it's been, I mean version one is very different from version 3. But it's been around a long time, and it's been used in, like probably like thousands of indie games, if not more.

***Evan:***
Yeah, and commercial games... And Valve uses it in the source engine yeah.

***Sanjay:***
Yeah, they use it in Source engine. They use SDL controller in Steam.

***Evan:***
I think they do all the rendering is SDL in Steam now. I think...

***Sanjay:***
If you're wondering, how does my PlayStation controller work on this like 20-year old Steam game is because they're actually intercepting XInput DLL injecting their own that maps to SDL.

***Mike:***
Yeah, and that's a big sell to, well, for students who we're teaching this, but also for you guys, if you're indie creators to say, like, yeah, this is a real, like, tested tool, lots of people are using it all over the game industry. So just keep that in mind. And especially with SDL3, I found, which we're talking about with the GPU API, it's a lot more consistent API overall, so lots of improvements and other stuff in there.

***Evan:***
And completely overhauled documentation, also.

***Sanjay:***
And it's fully CMake native. If you like CMake.

*Laughter*

***Sanjay:***
Yeah that's exciting. Okay, I think there’s questions…

***Audience member:***
Is there like a specific subversion you're targeting internally?

***Evan:***
A subversion of what?

***Audience member:***
Let's just say Vulkan, for example.

***Evan:***
Yeah.

***Audience member:***
Like, it must be 1.1 because of X…

***Evan:***
Yes, we are targeting Vulkan 1.0 with like a short list of required extensions, but just like the universally supported… Like we have a policy where like we only include an extension if it has like a 99% support rate. And so, yeah, I decided to target 1.0 just for maximum hardware compatibility, going as far back as possible. So that's something I didn't mention actually, is that I was looking at a range of hardware support from hardware from like 10 to 15 years ago would still be supported. Like that's basically… we're supporting anything that runs Vulkan at all. It should be supported by SDL GPU. Yeah.

***Sanjay:***
There was also a brief period of time where you explored having a DirectX 11 fallback…

***Evan:***
I wrote a complete Direct X 11 renderer and it was insanely broken. Yeah, just I was hitting driver bugs left and right, so I dropped that. Yeah.

***Audience member:***
I got a question for each of you actually, so the first one, using SDL GPU, like say if you have a, okay understanding of some of the more kind of advanced concepts that, you know, like Vulkan or DX12 use, going from like WebGL or SDL GPU to then eventually learning some of those advanced concepts is that, kind of a good, natural, gradual transition, or is there still quite a lot of extra things you'd have to do? And then the second one, for your projects that you're going to be teaching next spring, hopefully, has there been any specific types of problems that you've ran into kind of porting over to or using SDL GPU specifically rather than DX11, that maybe you didn't anticipate from the get go?

***Sanjay:***
For the first one, I guess that kind of also related, can you mix and match your own Vulkan calls with SDL GPU?

***Evan:***
Absolutely not. I will never allow that because my inbox is already very full. And the last thing I need is being like, why doesn't your renderer work? And then I look at it and they were like, you know, linking an extension from like a custom VkDevice or something. So I'm not allowing that at all. We don't expose any of the internals.

***Mike:***
I’ll piggyback on the... is it a good stair step? Like, if you already know, OpenGL or DirectX, should, you know, the next progression be SDL GPU? And that's what I'm going to be doing in my courses also in this spring coming up, because I kind of get my students for two semesters. And even for myself, the jump or just the cognitive load was very nice. Because when I look at the SDL GPU, it's like, hey, if I look at some of these real engines, like if you've seen like Diligent or other engines where they come up with their own abstraction to support multiple APIs, it kind of looks like SDL GPU. So it has the major concepts. Again, exactly what you talked about.

***Sanjay:***
Like if you look at like Unreal’s RHI layer, right? It's similar sort of idea.

***Mike:***
So it's not going to be like lost time to learn that as you’re progressing.

***Sanjay:***
And I think the second question is, where I'm going to guess. The challenge has been, the challenge of Mac development, because Matt's most comfortable in the world of Visual Studio and Windows…

***Matt:***
Game development is done in Visual Studio. It just is.

***Sanjay:***
And doing the dylibs and just universal binaries and like now, you know, like, how do I get the build system to work.

***Matt:***
Yeah, actually, that's been my biggest headache has been trying to convert everything to CMake and make it work cross platform. That's been the biggest challenge.

***Sanjay:***
The story of every CMake project.

***Matt:***
Thankfully, I got these guys to help me out with that quite a bit. They're knowledgeable about that. Some of the little surprises have been just in the ways that Vulkan has a few different conventions, they're just a little different from DirectX 11. Like, where's the semantics? Where do I put my semantics? Oh, you don't, because Vulkan just has you specify in order. And like, so that is going to be one thing that bugs me a little bit about how I'm going to present this to class because the HLSL has a semantic in it that we will never refer to... And so I'm just going to have to have a little aside where it's like, okay, this is because DirectX 12 has semantics, but we've chosen the Vulkan backend, so we're just not using those. But you still have to have them, but don't use them. So that'll be a little bit of a derailing the conversation, and the adding of pipelines and command buffers, those are, I think, things that DirectX 11 just.

***Sanjay:***
Hides from you.

***Matt:***
Abstracted, completely. But SDL GPU exposes exposes them very trivially, render passes are a thing now. A pipeline is a thing now, and a command buffer is a thing now. It exposes them very trivially, so it's not hard, but it will slow down the rollout a little bit compared to your first, you know, draw a triangle. We used to go straight to here's a shader. There's a vertex buffer. Go. Right. That was all it took to make your first triangle. Now it'll be, this is a shader, this is a vertex buffer, this is a command buffer, this is a render pass, this is a pipeline. So, yeah, it is injecting a little bit more friction than what we had before. But when you actually implement them, they're one line each. Well, two, I guess, because you, you begin and end, each of them. So yeah, that's what I've found so far.

Audience:
Sorry, just to add on to that first question. So it sounds like that's definitely not something you guys want to support, like supporting raw calls to Vulkan or DX12. Let's say, for example, if there are specific types of extensions, like, for example, in that OpenGL that the bindless texture extension is a very, very, very popular one. Like, if there's something that is released in DX12 or in Vulkan, that would be a really awesome feature to have, and maybe users would want to use. Is there any kind of strategy that you guys have kind of put in place for possibly supporting just this extension without having people to actually call, you know, manual, you know, API specific calls, essentially, right? And just use that supported extension more or less.

***Evan:***
Yeah, so there's a world where we do that, especially with like… one thing people have been asking a lot about recently is mesh shaders because they're the new hotness. And our policy for this is basically like… once the hardware support is there, we will come, right? Like when 99% of existing hardware supports it, we will support it. But right now, you know, something like mesh shaders, it's like 30% of existing hardware supports it. So, like now we're violating my philosophy of you write code once and it runs on anything, right? So I want you to have a reasonable expectation that things will actually work. The other thing, so bindless specifically, like, this is a question a lot of people have asked, which is, why don't you have a bindless path? And, like, why are you just doing like old style, like resource binding? And there's a few reasons. And the main one is just that I wanted one way to do things. So that was like another one of our design principles. It was like, there should only be one way to do something. So if we add bindless, now there's two ways to do something, right? Like when you're, when you're referencing graphics resources, either you're doing bindless or you're doing bindful. And so that's really challenging to support. Bindless is a lot more complicated. It requires a lot more infrastructure from the renderer. It has a lot of ways to crash your PC because you are indexing into unprotected memory to do that. So there's a lot of ways to screw it up. So I think that there's a world where we get to bindless support maybe someday, especially now, like the hardware support is kind of getting there now. Like, it's maybe not like 99%, but it's maybe like 80, 85% at this point. So we're getting there. But what I'd really like to see is like a really clear design abstraction for how to support that without causing a lot of problems. And it's very difficult to debug. So there's that. And there's also the fact that sort of the design space we're inhabiting is basically like small teams, indie developers, students, hobbyists. So for those kinds of people, like, are you making an open world game where, like, you would actually need, where bindless rendering would get you actual tangible benefits? Like, no, it's just a cool buzzword that you can say that you have in your renderer. Like, you don't need it. So that's kind of where I'm looking at it. Like if the hardware gets there and there's a nice abstraction to handle it, we'll put it in. But until then, probably not a great use of our time.

***Sanjay:***
*Picking an order for audience questions*

***Audience member:***
I was teaching a course based on RHIs to my students. I actually considered SDL GPU, in all these days of RHIs that exist now, so many solutions, what are the reasons to pick one over any other. Like why would they specifically go for SDL GPU?

***Evan:***
That’s a good question. What do you guys think?

***Sanjay:***
Yeah, I think the main thing is just, like, if you want to support, like, modern renderer semantics, but not have to worry about writing multiple renderers, right? Like ultimately it’s like, like if all your students are on PC, like, yeah, you could teach, I would really wouldn't teach them DirectX 12.

***Matt:***
I would say DirectX 11 if all of your students are on PC, I would still prefer DirectX 11 to be honest.

***Sanjay:***
like, well, I need to support Mac so what. There's not, like, like, yes, you could do Vulkan, but then you run into the problem, like Vulkan’s like, you know, 2000 lines of code to write to render a triangle or something like that.

***Evan:***
I think he's talking about like, maybe to clarify, it's like the actual like, there's multiple abstractions that exist right now, right? So, like, why would you use SDL over, you know, Diligent Engine or, or something like that?

***Mike:***
I mean, I can answer a part of that. I mean, with the, you know, how it's well tested, it's also a C library, which is very nice. So I've taught in like the D language before, so it was trivial to just bind in SDL. And that can be one way to remove friction too if you have a language, or if you want to teach it in Python or something too, that might be an option, or if you're doing stuff in game engines where you're building in a scripting language or these types of things and want to make, you know SDL calls in there, it just gives a lot of flexibility. So that's why, for me, I've ruled out some of the like object oriented, like SFML and stuff that tie me to C++. I mean, there are bindings, but SDL works there.

***Evan:***
Yeah, and I think I would say, like one of the reasons I really wanted to get this GPU upstream into SDL was because it's a very popular library. So a lot of people looking at it and I've received a lot of really helpful contributions since we upstreamed it. There's a lot of people looking at this code who are very good at programming. So that's been really nice. So I feel like the fact that it's tied to a bigger and trusted and popular open source project adds a lot of value.

***Sanjay:***
And I think also, like one thing that's like so like there, you know, compared to some other major open source projects, like everyone, like all the people that are maintainers and stuff are very responsive on pull requests and like, so like, like a couple of years ago, I just showed up and I was like, I want to write Xbox support and they were like, okay, sure, you know, because a lot of other open source projects are very, like, you'll like see like the pull requests which just sit there for years and stuff.. So they're very active. Like, I think it's pretty much, at least a couple of people at Valve, whose like full day job is just to work on SDL. So it's battle tested a lot of support. There are some really cool, you know, third party sort of, you know, like renderer things. Like I know Hades 2 uses one of, I forgot the library, [Evan’s note: It’s called The Forge] but it's just I think there's such a huge user base and it's always being maintained. And so I think that's like a big advantage.

***Mike:***
Oh, the other thing I'll toss in quick, especially from my teaching perspective, SDL is like locked in the ABI. It's very like stable. I don't have to worry about like function calls, randomly changing or somebody having a wild idea, so that's been really important.

***Evan:***
Yeah, just to clarify, we have a have an ABI lock policy on major versions, so we will never change a function that has been published. Yeah.

***Sanjay:***
All right, I think you're next.

***Audience member:***
Yeah, you I've got two questions. You half answered the first one already, but I'm mostly curious, um, how you create and allocate and bind resource descriptors versus an API like Vulkan. And the second question is, um, for platforms that have multiple back ends like Vulkan and DX12 on Windows, is there any way that you can, like hint SDL GPU to like pick one over the other?

***Evan:***
Yes, yeah, for your second question, yes, you can say, please give me a D3D12 backend and it will do that.

[Evan's note: in hindsight I think I might have slightly misunderstood the first question, in SDL GPU we don’t expose descriptors, it’s just automatically managed by the backend when you make bind calls.]

The first question about binding, yeah, so you know, we had to design like an implementation for that. So basically what I do is when you create a pipeline object, we also just create descriptors for it and then they are kept in a pool structure. So we basically just, we preallocate like thousands of descriptors based on the layout. And then they all go into a pool and then when something needs them, they just get pulled out of the pool. And then I think. I'm trying to remember. It's been a while since I looked at this, but I think that we are basically just grabbing, like.. I think we're just grabbing, like, a free descriptor out of a list when you need one, and then writing into it with the binding call.

***Audience member:***
Does that mean there’s like an upper limit?

***Evan:***
No, because if we run out, then we just make more. Yeah.

***Audience member:***
I saw that you have a limit of 4 uniform buffers. Is that like, a Vulkan thing?

***Evan:***
So yeah, we have a we have a max of four per stage, so you can have four in the vertex shader and four in the fragment shader. So the reason for that is, I mean, I guess just getting into like the design of the API, I guess, so the way that you interact with uniform or constant buffers is we have a call for that called like Push GPU Vertex Uniforms, Push GPU Fragment Uniforms, etc. So kind of treat it like a push style API. I wanted to use actual Vulkan push commands, but they have some really weird restrictions. Like, you can't have more than like four kilobytes of data in the buffer. It'll crash.

***sAudience member:***
Do you support push constants?

***Evan:***
No. Yeah. So, yeah, so it's like a push style API that I just implemented with uniform buffers. So like those are allocated differently. So the reason we manage them on the back end is because, the way that you would interact with them was basically all the same. So, like in an earlier version of the API, you would create a uniform buffer specifically and then like add stuff to it and then bind it specifically. But the reason I didn't like that was because…

*Loud music starts playing*

***Sanjay:***
I think we’re being played out. Yeah. The rave is starting. But we can answer more questions. Yeah. They want us out of the room at 5… Yeah, it's 5.

*Audience applause*

***Sanjay:***
If you have questions just come talk to us. We'll just be out there. Thank you.
