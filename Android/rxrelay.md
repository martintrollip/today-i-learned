- Date : 2020-07-27
- Tags : #Android

## RxRelay

Relays are RxJava types which are both Observable and a Consumer.  Basically a Subject without the ability to call stream terminating operations such as `onComplete` or `onError`.  They allow you to bridge non-Rx APIs into Rx easily, and without the worry of accidentally triggering a terminal state.

See the different Jake Wharton implementations for BehaviourRelay, PublishRelay and ReplayRelay.  


[RxRelay](https://github.com/JakeWharton/RxRelay)
