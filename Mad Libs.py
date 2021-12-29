import random 
when= ['Last night','last month','Few years ago','Yesterday']
who=['A piggy','A baby','A crow','Few dogs']
name=['Reaper','Jimmy','Kelly','Stuart']
residence=['Barbados','Las Vegas','India','Yemen']
went=['the Office','the Whitehouse','the Mall','the Dog park']
happened=['Hunted','fished','ate a hotdog','Wrote a book']
print(random.choice(when)+', '+random.choice(who)+' called '+random.choice(name)+' who lived in '+random.choice(residence)+' went to '+random.choice(went)+' and '+random.choice(happened))