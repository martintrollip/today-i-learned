- Date : 2020-06-11
- Tags : #Random

## Bypass youtube ads by adding a dot after the domain


On desktop if you use `https://www.youtube.com/watch?v=` you will see ads.  And if you add a dot after the domain such as `https://www.youtube.com./watch?v=` then you won't see ads.

The website will serve the content but there is no associated hostname, no cookies and the CORS and ads whitelist is broken since only the version without the dot is on the white list. 


[fyi: You can bypass youtube ads by adding a dot after the domain](https://www.reddit.com/r/webdev/comments/gzr3cq/fyi_you_can_bypass_youtube_ads_by_adding_a_dot/)

[Cross-origin resource sharing](https://en.wikipedia.org/wiki/Cross-origin_resource_sharing)
