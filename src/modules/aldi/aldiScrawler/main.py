from facade import facade

resourceList = []
resourceList.append('https://www.aldi.com.au/en/groceries/baby/baby-food/')
resourceList.append('https://www.aldi.com.au/en/groceries/beauty/')
resourceList.append('https://www.aldi.com.au/en/groceries/liquor/beer-cider/')
resourceList.append("https://www.aldi.com.au/en/groceries/liquor/champagne-sparkling/")
resourceList.append('https://www.aldi.com.au/en/groceries/pantry/chocolate/')
resourceList.append('https://www.aldi.com.au/en/groceries/pantry/coffee/')
resourceList.append('https://www.aldi.com.au/en/groceries/fresh-produce/dairy-eggs/')
resourceList.append('https://www.aldi.com.au/en/groceries/freezer/')
resourceList.append('https://www.aldi.com.au/en/groceries/pantry/gluten-free/')
resourceList.append('https://www.aldi.com.au/en/groceries/health/')
resourceList.append('https://www.aldi.com.au/en/groceries/laundry-household/household/')
resourceList.append('https://www.aldi.com.au/en/groceries/laundry-household/laundry/')
resourceList.append('https://www.aldi.com.au/en/groceries/liquor/wine/')
resourceList.append('https://www.aldi.com.au/en/groceries/baby/nappies-and-wipes/')
resourceList.append('https://www.aldi.com.au/en/groceries/pantry/olive-oil/')
resourceList.append('https://www.aldi.com.au/en/groceries/pantry/just-organic/')
resourceList.append('https://www.aldi.com.au/en/groceries/liquor/spirits/')
resourceList.append('https://www.aldi.com.au/en/groceries/super-savers/')



myFacade = facade()
for link in resourceList:
    myFacade.scrawler(link)