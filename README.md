# PROJECT-II RARE EARTH OXIDES PROJECTS AROUND THE WORLD
![hello](https://www.google.com/imgres?imgurl=https%3A%2F%2Fwww.thoughtco.com%2Fthmb%2Fl61nJt1iaT0dxpcYcnTNno_12wE%3D%2F1500x0%2Ffilters%3Ano_upscale()%3Amax_bytes(150000)%3Astrip_icc()%2Frare-earth-metals-conceptual-image-184893255-588524525f9b58bdb355bc2e.jpg&tbnid=xKo3M5LVxEekCM&vet=12ahUKEwj_4dmxyJ2CAxWrrycCHTdtB4YQMygJegQIARBV..i&imgrefurl=https%3A%2F%2Fwww.thoughtco.com%2Frare-earth-elements-list-606660&docid=SD_00MTlj0X2TM&w=1500&h=1061&q=rare%20earth%20metals&ved=2ahUKEwj_4dmxyJ2CAxWrrycCHTdtB4YQMygJegQIARBV)

## 1. Libraries and Data used:
1.1 Libraries: <br>
    - seaborn <br>
    - matplotlib <br>
    - pandas <br>
    - numpy <br>
    - os <br>
    - b4S <br>
    
2.1 Data source:
    - https://www.metal.com/Rare-Earth-Oxides
    -https://www.kaggle.com/datasets/konradb/global-rare-earth-elements-projects
    

## 2. Data extracting / Data scrapping: 
2.1. create a df from the information scrapped from www.metal.com to get updated info regardin REO prices <br>
2.2. Consistent naming between both df: <br>
2.3 Export csv for data extraction and visualization

## 3. Data cleaning: 
3.1. Drop empty rows / dupplicate values in needed <br>
2.3. Consistent naming between both df: <br>
2.4. Change value type when needed in order to be able to carry on calculations <br>

## 4. Data Exploration & Visualization
3.1. Create subset filtering the desired data to answer each question <br>
3.2. Count yearly occurencies of attacks <br>
3.3. Found median and average values to stablish baseline. <br>
3.4. define a criteria by which analyse data <br>
3.5. Filter data from 1950 onwards for better visualization <br>
> ANGRYNESS FACTOR: to be relevant angryness factor should be at least 20% above average. <br>


## 5. Analysis

## <span style="color:darkslategrey">Q1.: How angry did _Brazilian_ sharks get after the infamous 7 X 1? </span>

<img width="808" alt="Shark-attacks_BR_WC-2014" src="https://user-images.githubusercontent.com/32434139/215420339-c0c79984-1960-4420-aad0-dc3b319e6811.png">


### <span style="color:darkslategrey"> Q1.1: How was this reaction compared to other World Cups? </span>

<img width="803" alt="Shark-attacks_BR_WC-history" src="https://user-images.githubusercontent.com/32434139/215419969-23c9c1f9-b973-40b1-9297-eef49dac37f4.png">


### <span style="color:lightslategrey; line-height:1.5em"> **Analysis:** </span>

Data shows that _Brazilian_ sharks do not react negatively when Brazil loses in the World Cup at all, with numbers in those periods being in all time lows. 

In fact, the rise of the 'angryness factor' on the years leading to some World Cups (see 2002, 2006, 2010 and 2018) could indicate that _Brazilian_ _sharks_ are are generally against what some believe to be the Bread and Circus politics surrounding the event. Qualitative data (e.g. interview with the sharks), is needed for further analysis on that subject. 


## <span style="color:darkslateblue"> Q2: How angry were the _Brazilian_ sharks that did attack? </span>

<img width="755" alt="Shark-attacks_BR_angryness" src="https://user-images.githubusercontent.com/32434139/215419878-77e69851-ae71-48dd-ab53-ee1463d80820.png">


### <span style="color:lightslategrey; line-height:1.5em"> **Analysis:** </span>

Data shows that most fatal attacks happened when Brazil won the worldcup which is leading this researcher to believe that perhaps this is actually how sharks celebrate the world cup. Further research is required to understand sharks customs regarding sports. 


### <span style="color:lightslategrey; line-height:1.5em"> **Conclusion:** </span> 
There's no direct correlation between World Cup outcomes and the Angryness Factor of the sharks. However, more qualitative analysis is needed in order to better understand sharks views and costumns around the topic. 

![wow](https://user-images.githubusercontent.com/32434139/215419740-5eff78f2-09fd-4ec8-82a7-64a3bbd8f0f6.gif)

## <span style="color:darkslateblue"> BONUS Question: What was the "Angryness Factor" sharks from countries that made it to the finals in the same period? </span>

![Shark-attacks_global_WC-history](https://user-images.githubusercontent.com/32434139/215450500-2ca025fa-52a8-481b-89d0-7592fb810845.png)

### <span style="color:lightslategrey; line-height:1.5em"> **Analysis:** </span>

None of the countries that made it to the World Cup finals had a significant increase in the number of attacks, regardless of the outcome of the match. 
Note: Netherlands data was not available in the dataset.  

### Thank you!

![](https://giphy.com/gifs/dazn-usa-dance-shark-sharks-d2eOvdra51vj49P59V)