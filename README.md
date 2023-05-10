For this project, I analysed the videos in the why are you lying challenge. Through the challenge trend on tiktok, hundreds of young Kenyans talked about mistreatment in their high schools

Although the videos occurred under many different tags, I worked specifically with the videos under the following tags:
1) whyareyoulyingchallenge
2) whyyoulyingchallenge

I used these two trends because through my research, I found that they were likely to contain more of the videos in the trend that related specifically to Kenyan high schools. Importantly, this means that my universe of data contains many of the major videos in the trend, but not every single video related to kenyan high schools that may for instance be in the trend #ohwhyareyoulying instead of #whyareyoulying.




# Getting the videos

I got all the videos in the trend through a wrapper library called Tiktokpy.

* [Library source]
(https://tiktokpy.readthedocs.io/en/latest/users/explanation.html)
* [Specific link](https://tiktokpy.readthedocs.io/en/latest/users/explanation.html#data-collection)

The total of the videos extracted was 171. 

I then set up the scraper so that it input results into a format that could be converted into a dataframe.

Here is the notebook in which I get the videos

# Cleaning the data
However, there were duplicates. That is, videos which were tagged with both tags appeared twice in my dataset. 

I therefore removed the duplicates through Microsoft Excel. From the 171 videos, I remained with 140 videos

For the remaining videos, I removed any videos that were not Kenyan. For instance, videos about Nigerians given the trend's audio was a Nigerian song. 

From the 140 videos, I remained with 70 videos.

Here is the notebook in which I collect the videos
Here is the Excel sheet with the final dataset

# How I categorised the videos

I then went through each video to further categorise them. Here are some of the columns I added manually and what they reference:

* important text: The text that is inside the video rather than in the caption
* issue raised: summary of themes raised in the video	
* gen_in_comment_or_video: whether the video referenced the generation factor in the video itself or in the comment
* generation_reference_in_video: whether the video itself referenced the generation factor
* consequences: whether the video referenced consequences such as loss of school leaving certificate, suspension, loss of recommendors
* school: if the school is identified
* gender: if the school's gender is identifiable
* direct_family_reference: if there is a reference to the students as sons, daughters or the school as home etc	
* bullied_by: who conducted the mistreatment, usually school administration or teachers.

# Tech:
#Python, #R, #Tiktokpy

