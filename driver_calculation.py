#!/usr/bin/env python
# coding: utf-8

# In[6]:


#!/usr/bin/env python3

import ipywidgets as widgets
from IPython.display import display

# conda install --channel conda-forge appmode (https://github.com/oschuett/appmode)
# https://towardsdatascience.com/bring-your-jupyter-notebook-to-life-with-interactive-widgets-bc12e03f0916

# setup prompts

routeDropdown = widgets.Dropdown(
    options=['Please choose rate','2.75 - 100','2.70 - 100','2.70 - 95','2.70 - 90','2.50 - 99','2.50 - 85','2.30 - 85','2.70 - weekend','3.50 - weekend'],
    description='Route:',
    disabled=False
)

dropsSlider = widgets.BoundedIntText(
    min=0,
    max=150,
    step=1,
    description='# of Drops:',
    value=0
)
display(routeDropdown)
display(dropsSlider) 

button = widgets.Button(description="Run Calculation")
output = widgets.Output()

# define the different tariff rate calculations

# route1 = [DS01]
# route2 = [DS02,DS06,DS14,DS20,DS21,DS34]
# route3 = [DS05,DS07]
# route4 = [DS08]
# route5 = [DS09]
# route6 = [DS13,DS15]
# route7 = [DS25]

# check was the driver working on the weekend
def weekendDrops():
    
    weekendDrops=dropsSlider.value
    amountOwedForWeekend = weekendDrops * round(float(routeDropdown.value.replace(' - weekend', '')),2)
    print("€" + str(amountOwedForWeekend) + '\n')
    
def route1():
    
# 1-100	€2.75
# 101-110	€2.24
# 111-120	€1.89
# 121+	€1.50

    x=0.0
    drops=dropsSlider.value
    counter = 1

    for drop in range(drops):  
        if counter <= 100:
            x = round(2.75 + x , 2)
            counter += 1
        elif counter > 100 and counter <= 110:
            x = round(2.24 + x , 2)      
            counter += 1
        elif counter > 110 and counter <= 120:
            x = round(1.89 + x , 2)      
            counter += 1
        elif counter > 120:
            x = round(1.5 + x , 2)      
            counter += 1
            
    print("€" + str(x) + '\n') 

    
def route2():

# 1-85		€2.30
# 86-95		€2.00
# 96-105	€1.70
# 106+		€1.40
    
    x=0.0
    drops=dropsSlider.value
    counter = 1

    for drop in range(drops):  
        if counter <= 85:
            x = round(2.3 + x , 2)
            counter += 1
        elif counter > 85 and counter <= 95:
            x = round(2.0 + x , 2)      
            counter += 1
        elif counter > 95 and counter <= 105:
            x = round(1.7 + x , 2)      
            counter += 1
        elif counter > 105:
            x = round(1.4 + x , 2)      
            counter += 1
            
    print("€" + str(x) + '\n') 
    
    

def route3():
    
# 1-95	€2.70
# 96-105	€2.16
# 106-115	€1.84
# 116+	€1.50

    x=0.0
    drops=dropsSlider.value
    counter = 1

    for drop in range(drops):  
        if counter <= 95:
            x = round(2.70 + x , 2)
            counter += 1
        elif counter > 95 and counter <= 105:
            x = round(2.16 + x , 2)      
            counter += 1
        elif counter > 105 and counter <= 115:
            x = round(1.84 + x , 2)      
            counter += 1
        elif counter > 115:
            x = round(1.50 + x , 2)      
            counter += 1
            
    print("€" + str(x) + '\n') 
    
    

def route4():
    
# 1-99	€2.50
# 100-109	€2.00
# 110-119	€1.70
# 120+	€1.40

    x=0.0
    drops=dropsSlider.value
    counter = 1

    for drop in range(drops):  
        if counter <= 99:
            x = round(2.50 + x , 2)
            counter += 1
        elif counter > 99 and counter <= 109:
            x = round(2.00 + x , 2)      
            counter += 1
        elif counter > 109 and counter <= 119:
            x = round(1.70 + x , 2)      
            counter += 1
        elif counter > 119:
            x = round(1.40 + x , 2)      
            counter += 1
            
    print("€" + str(x) + '\n') 
    

def route5():

# 1-90	€2.70
# 91-100	€2.16
# 101-110	€1.84
# 111+	€1.50

    x=0.0
    drops=dropsSlider.value
    counter = 1

    for drop in range(drops):  
        if counter <= 90:
            x = round(2.70 + x , 2)
            counter += 1
        elif counter > 90 and counter <= 100:
            x = round(2.16 + x , 2)      
            counter += 1
        elif counter > 100 and counter <= 110:
            x = round(1.84 + x , 2)      
            counter += 1
        elif counter > 110:
            x = round(1.50 + x , 2)      
            counter += 1
            
    print("€" + str(x) + '\n')     
    

def route6():
# 1-85	€2.50
# 86-95	€2.00
# 96-105	€1.70
# 106+	€1.40

    x=0.0
    drops=dropsSlider.value
    counter = 1

    for drop in range(drops):  
        if counter <= 85:
            x = round(2.50 + x , 2)
            counter += 1
        elif counter > 85 and counter <= 95:
            x = round(2.00 + x , 2)      
            counter += 1
        elif counter > 95 and counter <= 105:
            x = round(1.70 + x , 2)      
            counter += 1
        elif counter > 105:
            x = round(1.40 + x , 2)      
            counter += 1
            
    print("€" + str(x) + '\n')     

    
def route7():
    
# 1-100	€2.70
# 101-110	€2.16
# 111-120	€1.84
# 121+	€1.50

    x=0.0
    drops=dropsSlider.value
    counter = 1

    for drop in range(drops):  
        if counter <= 100:
            x = round(2.70 + x , 2)
            counter += 1
        elif counter > 100 and counter <= 110:
            x = round(2.16 + x , 2)      
            counter += 1
        elif counter > 110 and counter <= 120:
            x = round(1.84 + x , 2)      
            counter += 1
        elif counter > 120:
            x = round(1.50 + x , 2)      
            counter += 1
            
    print("€" + str(x) + '\n')     
    

def runCalculation():
 
    if routeDropdown.value in ['2.75 - 100']:
        route1()
    elif routeDropdown.value in ['2.30 - 85']:
        route2()
    elif routeDropdown.value in ['2.70 - 95']:
        route3()
    elif routeDropdown.value in ['2.50 - 99']:
        route4()
    elif routeDropdown.value in ['2.70 - 90']:
        route5()
    elif routeDropdown.value in ['2.50 - 85']:
        route6()
    elif routeDropdown.value in ['2.70 - 100']:
        route7()
    elif routeDropdown.value in ['2.70 - weekend','3.50 - weekend']:
        weekendDrops()
        
def on_button_clicked(b):
    runCalculation()
    
display(button, output)
button.on_click(on_button_clicked)

