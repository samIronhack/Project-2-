# Project-2-

2nd attempt after Power Outage

For this project we had to perform an analysis between an existing database and scrape a website to create a dataframe of our own. 

For this project I wanted to compare the IMDB database to the database of popular streaming platforms:

- Amazon Prime
- Disney Plus 
- Netflix

My hypothesis for this analysis is that streaming platforms do not care about popular rated movies and that they care more about the quantity of content. 

For my hypothesis a platform has to have more than 20% (50) of either Tv Shows / Movies in the top 250 movies/Tv Shows


To start I scraped IMDB's website to create the following DataFrame 

IMDB top 250 Movies DataFrame
![Screenshot 2022-07-26 at 00 00 16](https://user-images.githubusercontent.com/104360125/180881129-8429d6b9-2d1f-4028-b419-4adf862c957c.png)


IMDB top 250 Tv Shows DataFrame
![Screenshot 2022-07-25 at 23 59 44](https://user-images.githubusercontent.com/104360125/180881071-fd7c924d-2c6b-45a8-a932-0c7642866e71.png)

Thanks to my Sponsor Express VPN I was able to get this without it being imported in Spanish. 
![Screenshot 2022-07-26 at 00 01 15](https://user-images.githubusercontent.com/104360125/180881226-f03d7953-7704-4d21-b67b-4d5e67e81709.png)

Since later on in I would have to merge these dataframes I set the column ['Title'] as the index of each of the two dataframes


Then I got to work on the Dataframes I collected from Kaggle. Each of the dataframes was created by the same user and the all had an identical layout. 
This allowed me to use each cleaning method to all the dataFrames. 

I renamed certain Colums and added uppercasing to make the dataframe look better. 
This is what they looked like after the first clean.

Netflix DataFrame

![Screenshot 2022-07-26 at 00 06 19](https://user-images.githubusercontent.com/104360125/180881844-65f1d751-7ed6-4446-95b5-c340cf7c6fc7.png)

The sizes of the dataFrames 

Amazon Prime -->  9668 rows × 12 columns
Netflix      -->  8807 rows × 12 columns
Disney Plus  -->  1450 rows × 12 columns

I then decided to drop certain columns as they were not relevant for the analysis. These Columns were:

'rating', 'description', 'Content type', 'cast', 'country', 'show_id', 'date_added', 'director'


Just as for the IMDB dataFrames I set the index column to 'Title' for mergin later on.

Final dataFrame before merging with IMDB dataFrame 
![Screenshot 2022-07-26 at 00 11 49](https://user-images.githubusercontent.com/104360125/180882685-9289e6ff-005c-49f6-9e2d-949c406e6d41.png)

On the last File I added a few more columns to the dataframes so that it would be clear what belonged to what dataFrame.
Those columns are vilible in the next Dataframe on the most right two columns. I assigned the platform to each of the previous databases and connected the type also. 

The Final DataFrame(Sample(50))
![Screenshot 2022-07-26 at 00 25 58](https://user-images.githubusercontent.com/104360125/180884201-35092d96-6335-48da-ba70-3730d0eff439.png)



With the DataFrame the following graphs were made to visualise how many titles each platform has in their global library. 

HYPOTHESIS REMINDER::

Streaming platforms do not care about popular rated movies and that they care more about the quantity of content. 

If they have > 20% of the IMDB library I am wrong



All platforms and their library count NETFLIX is the winner!
![Screenshot 2022-07-25 at 23 48 25](https://user-images.githubusercontent.com/104360125/180885102-9b46adbf-9691-4f41-83dc-d85340867271.png)

My Hypothesis is wrong... 
with 51 series in the IBDB library Netlflix seems to care about the popularity of the series they allow us to stream.

The other platforms however do not meet this requirement.

Lets have a deeper look at the data. 

This graph although I like it less shows the difference between movies and series better.
![Screenshot 2022-07-25 at 23 48 39](https://user-images.githubusercontent.com/104360125/180885780-83a47120-12aa-491f-af4b-9ebf7efebf48.png)

It is clear that platforms prefer to buy popular series > movie.

##THOUGHTS## This is probably becuase we will spend a lot more time on the platform watching series than watching a single movie. 

Lets Check what score is purchased most frequently

Most frequent purchased IMDB rating for all platforms 
![Screenshot 2022-07-26 at 00 51 56](https://user-images.githubusercontent.com/104360125/180887364-37e439bc-4ed0-4671-91f0-61746609f797.png)
The most frequent bought ratings are between 8.4 and 8.7 

Below you can find graphs for each specific platform 

IMDB Rating Purchases by Amazon  
![Screenshot 2022-07-26 at 00 53 43](https://user-images.githubusercontent.com/104360125/180887531-107a9198-14b4-4d10-bfe2-f36f8525db7b.png)

IMDB Rating Purchases by Disney  
![Screenshot 2022-07-26 at 00 53 57](https://user-images.githubusercontent.com/104360125/180887550-8a166531-c2f3-47e2-b5d9-320087c1b9b9.png)

IMDB Rating Purchases by Netflix  
![Screenshot 2022-07-26 at 00 54 11](https://user-images.githubusercontent.com/104360125/180887570-ed1f7bef-2ce6-4f95-a650-4a8c611a45cd.png)

Lets look at the production date of the popular movies/tv shows in the library of the platofrms 

Amazon Prime  
![Screenshot 2022-07-26 at 00 57 13](https://user-images.githubusercontent.com/104360125/180888152-826bd123-9751-4e9a-8187-77ba3f3f60b1.png)

DIsney Plus 
![Screenshot 2022-07-26 at 00 57 05](https://user-images.githubusercontent.com/104360125/180888275-e5962c77-08e3-43cd-a92c-b7dbd29690a8.png)

Netflix 
![Screenshot 2022-07-26 at 00 56 58](https://user-images.githubusercontent.com/104360125/180888286-d205230a-75f0-4615-a396-b0fae14bf492.png)

Netflix and Amazon seem to have a very comparable strategy on this while Disney is the outlyer. This is most likely due to the fact that disney's library does not have as many matches with the IMDB top 250 library. 

So to confirm again. 

My Hypothesis was wrong for Netflix but does count for Amazon Prime and Disney Plus. 






