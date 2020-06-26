- Date : 2020-06-05
- Tags : #Android

## Flavor dimensions

When building the app, Gradle combines a product flavor configuration from each flavor dimension we define, along with a build type configuration, to create the final build variant. Gradle does not combine product flavors that belong to the same flavor dimension.

You can also create a src folder for a flavour variant,  eg if you have a `client` dimension and a `services` dimension you can create a folder named `client1Service1` and `client1Service2` if you need specific code only for `client1`.

[Flavors & Dimensions- Building Multiple Android Apps with a single codebase](https://medium.com/@manikandan2203/flavors-dimensions-building-multiple-android-apps-with-a-single-codebase-4876f4f2193d)

[Advanced Android Flavors Part 2 — Enter Flavor Dimensions](https://proandroiddev.com/advanced-android-flavors-part-2-enter-flavor-dimensions-4ad7f486f6)
