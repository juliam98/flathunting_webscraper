# flathunting_webscraper

## what is this?

This _very primitive_ webscraper takes a URL of a website's (for now just Foxtons) search page and returns a dataframe of summary infomation about properties which meet your search criteria. 

All you need to do is go to the estate agent's website and search for properties, adjust your location, rent, and  other filters, hit search and copy the URL to the code. You only need to do it once, and then every time you run the code the list will be generated from up to date search results. No need to go back to the website to create new searches. 

You might get an error if nothing meets your search criteria, and if you're looking in London like I am, then prepare for this to happen a lot. 

## how does it work?

The output you will get looks something like this:

|   |             name            |    rent    |                             link                             |
|---|:---------------------------:|:----------:|:------------------------------------------------------------:|
| 0 | Otter Close, Stratford, E15 | £1,900 pcm | https://www.foxtons.co.uk/properties-to-rent/e15/chpk3264388 |
| 1 | Chiltern Road, Mile End, E3 | £1,900 pcm | https://www.foxtons.co.uk/properties-to-rent/e3/chpk3200496  |

Like I said, don't get your hopes up. Those are all the 2-bed properties under £2,000 in E1. 

## why?

Because flathunting is daunting as it is, so why not make it fun by convincing yourself that you are optimising this task by doing things like writing the code for this webscraper. 

## future 
_I might do this, might not, my hyperfixations end just as abruptly as they begin._ 

But the ideas might inspire you, so here they are:
- Generate a message which informs you no properties have met your search criteria (if you're also looking in London, you will likely see this a lot)
- Ability to provide multiple URLs to search from (e.g. so yo can check out properties from E1 and E2 in one go)
- Filter out properties with 'let agreed' labels
- Compare the output with properties saved in the spreadsheet from previous searches, append only new results
- Make the code work for other websites

## godspeed in your flat search

<div align="center">
  <img src="https://i.chzbgr.com/full/9756515072/h077AA256/bowtie-landlords-counting-their-money-air-honest-but-s-much" height=300px>
</div>
