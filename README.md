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

- Amazon Prime -->  9668 rows × 12 columns
- Netflix      -->  8807 rows × 12 columns
- Disney Plus  -->  1450 rows × 12 columns

I then decided to drop certain columns as they were not relevant for the analysis. These Columns were:

'rating', 'description', 'Content type', 'cast', 'country', 'show_id', 'date_added', 'director'


Just as for the IMDB dataFrames I set the index column to 'Title' for mergin later on.

Final dataFrame before merging with IMDB dataFrame 

![Screenshot 2022-07-26 at 00 11 49](https://user-images.githubusercontent.com/104360125/180882685-9289e6ff-005c-49f6-9e2d-949c406e6d41.png)

On the last File I added a few more columns to the dataframes so that it would be clear what belonged to what dataFrame

This is visible on the following image:

![Screenshot 2022-07-26 at 08 39 05](https://user-images.githubusercontent.com/104360125/180940113-e05af50c-4ae5-496d-979e-2d430db51e0c.png)



With all this data I made the following visualisation to show you wether my hypothsis is correct or not.


##HYPOTHESIS REMINDER##

My hypothesis for this analysis is that streaming platforms do not care about popular rated movies and that they care more about the quantity of content. 
For my hypothesis a platform has to have more than 20% (50) of either Tv Shows / Movies in the top 250 movies/Tv Shows


First lets take a look at the total number of IMDB titles the platforms have in their library. 

All the platforms and their IMDB top 250 count 

![Screenshot 2022-07-26 at 08 40 53](https://user-images.githubusercontent.com/104360125/180940391-c3b671c8-ddce-4c95-a213-d1d2884c1d17.png)

In this image we can see that that Netflix is the only one that meets the requirement to prove my hypothesis wrong with 51 Tv Shows in their library.

Now lets take a closer look at the different content types side by side. 

![Screenshot 2022-07-26 at 08 44 04](https://user-images.githubusercontent.com/104360125/180940950-33b89617-1fc6-4020-8e48-7c8783756354.png)

In this Image I find it easier to see the difference between movies and Tv Shows
It is clear that pltforms prefer to purchase Tv Shows, this is most likely due to the fact that people will spend more time on the platform watching an entire series than they would watching a single movie. 

What ratings level is purchased most commonly? 
This image shows all different streaming platforms and what rating their most commonly buy. 

![Screenshot 2022-07-26 at 08 45 55](https://user-images.githubusercontent.com/104360125/180941246-d98fb7e0-b669-4d11-8e57-d77b896e567b.png)

It is cleat that thisis between 8.4 and 8.7. higher than this would be hard since there is only a small number of titles with a rating that high. 

Now lets look at each platform individual 


Amazon Prime 

![Screenshot 2022-07-26 at 08 49 22](https://user-images.githubusercontent.com/104360125/180941802-be726b27-ef40-4d7d-a241-aa63c0ff7d4b.png)


Disney Plus 

![Screenshot 2022-07-26 at 08 49 35](https://user-images.githubusercontent.com/104360125/180941867-2b63f754-fa8c-48c2-b6fc-65c96c4f4e5d.png)

Netflix 

![Screenshot 2022-07-26 at 08 49 56](https://user-images.githubusercontent.com/104360125/180941924-0b859911-7c39-4116-9dd5-b774b2bc2af9.png)


Then at last I would like to show the production date of movies that platforms own 


Amazon Production date of movies and series owned 

![Screenshot 2022-07-26 at 08 51 45](https://user-images.githubusercontent.com/104360125/180942253-5d183e73-e905-4850-8235-ac8b6f9bb908.png)


Disney Plus Production date of movies and series owned 

![Screenshot 2022-07-26 at 08 52 02](https://user-images.githubusercontent.com/104360125/180942302-31169fca-e186-464f-b62c-19563a3f8af2.png)


Netflix Production date of movies and series owned 

![Screenshot 2022-07-26 at 08 52 14](https://user-images.githubusercontent.com/104360125/180942337-d7045b2e-f770-4215-a97c-0c99f858a51a.png)

On all platforms we can see that most movies and Tv Shows owned by platforms are from the year 2000.

Disney Plus with a high percentage on older movies is probably due to their self produced animation moveis in the 80's and 90's. 



All in all from this analysis we can conclude that overall platforms do not care that much for popularity ratings of movies and series but focus on quantity. 

If you as a consumer do care about this then Netlix is your best option! 


Thank you for taking the time to read my report. 

Samuel Ledeboer 
