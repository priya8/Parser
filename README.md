Parser-
=======
Problem statement

Input:

Given n valid URLs and n skew words. Output: 1) Display, corresponding n titles (Headlines) 2) Based on the occurrence of skew words, create a cluster of web pages



Output:

1) URL1 Title1 CLASS A 2) URL2 Title2 CLASS A 3) URL3 Title3 CLASS B

Specific Input related to testing:

urls.txt contains all the URL's where in the each URL's content will be parsed and hashed to obtain the following skew Words (NOT CASE sensitive): BUY, ACQUIRE, MERGE, RAISED, FUNDED, SECURED, SHUT, CLOSED

If highest occurring terms are: BUY / ACQUIRE / MERGE , then the CLASS is assigned as M&A If highest occurring terms are: RAISED / FUNDED / SECURED , then the CLASS is assigned as GROWTH If highest occurring terms are: SHUT / CLOSED , then the CLASS is assigned as CLOSURE
