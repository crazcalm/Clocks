Clocks
======

Some Clock related scripts.

I was inspired by a youtube video to make a timer. The video used 
time.sleep(1) to create the seconds, which works. However, it is not accurate
because, outside of the time.sleep(1), the code still takes time to run.

To fix this, I used the time.clock(), which is a clock that, once initiated,
will continue to run. This makes the timer more accurate and more reusable.
