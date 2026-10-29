# SweetAndSavoury

You're hosting an event at a food festival and want to showcase the best possible pairing of two dishes from the festival that complement each other's flavor profile.

Each dish has a flavor profile represented by an integer. A negative integer means a dish is sweet, while a positive integer means a dish is savory. The absolute value of that integer represents the intensity of that flavor. For example, a flavor profile of -3 is slightly sweet, one of -10 is extremely sweet, one of 2 is mildly savory, and one of 8 is significantly savory.

You have two arrays, one for sweet dishes and one for savory dishes, and you want to find a pair of one sweet dish and one savory dish that, when combined, have a total flavor profile that's as close to zero as possible. This means the sum of their flavor profiles should be as close to zero as possible.

If there are multiple pairs with the same total flavor profile, pick the pair with the least sweet dish (the one with the highest flavor profile value, since negative numbers are sweeter).

If there are multiple such pairs, pick the pair with the least savory dish (the one with the lowest flavor profile value).
