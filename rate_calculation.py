{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 6,
   "metadata": {
    "scrolled": false
   },
   "outputs": [
    {
     "data": {
      "application/vnd.jupyter.widget-view+json": {
       "model_id": "19144791034c4c3fb8ce0d15fca9094b",
       "version_major": 2,
       "version_minor": 0
      },
      "text/plain": [
       "Dropdown(description='Route:', options=('Please choose rate', '2.75 - 100', '2.70 - 100', '2.70 - 95', '2.70 -…"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "data": {
      "application/vnd.jupyter.widget-view+json": {
       "model_id": "53d7c4ef38e34fca93935611b03e8f1f",
       "version_major": 2,
       "version_minor": 0
      },
      "text/plain": [
       "BoundedIntText(value=0, description='# of Drops:', max=150)"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "data": {
      "application/vnd.jupyter.widget-view+json": {
       "model_id": "3fa4c44385084586b09edf23b0cd2fde",
       "version_major": 2,
       "version_minor": 0
      },
      "text/plain": [
       "Button(description='Run Calculation', style=ButtonStyle())"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "data": {
      "application/vnd.jupyter.widget-view+json": {
       "model_id": "d1c9a8c82fd24045af991509796e28d2",
       "version_major": 2,
       "version_minor": 0
      },
      "text/plain": [
       "Output()"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "#!/usr/bin/env python3\n",
    "\n",
    "import ipywidgets as widgets\n",
    "from IPython.display import display\n",
    "\n",
    "# conda install --channel conda-forge appmode (https://github.com/oschuett/appmode)\n",
    "# https://towardsdatascience.com/bring-your-jupyter-notebook-to-life-with-interactive-widgets-bc12e03f0916\n",
    "\n",
    "# setup prompts\n",
    "\n",
    "routeDropdown = widgets.Dropdown(\n",
    "    options=['Please choose rate','2.75 - 100','2.70 - 100','2.70 - 95','2.70 - 90','2.50 - 99','2.50 - 85','2.30 - 85','2.70 - weekend','3.50 - weekend'],\n",
    "    description='Route:',\n",
    "    disabled=False\n",
    ")\n",
    "\n",
    "dropsSlider = widgets.BoundedIntText(\n",
    "    min=0,\n",
    "    max=150,\n",
    "    step=1,\n",
    "    description='# of Drops:',\n",
    "    value=0\n",
    ")\n",
    "display(routeDropdown)\n",
    "display(dropsSlider) \n",
    "\n",
    "button = widgets.Button(description=\"Run Calculation\")\n",
    "output = widgets.Output()\n",
    "\n",
    "# define the different tariff rate calculations\n",
    "\n",
    "# route1 = [DS01]\n",
    "# route2 = [DS02,DS06,DS14,DS20,DS21,DS34]\n",
    "# route3 = [DS05,DS07]\n",
    "# route4 = [DS08]\n",
    "# route5 = [DS09]\n",
    "# route6 = [DS13,DS15]\n",
    "# route7 = [DS25]\n",
    "\n",
    "# check was the driver working on the weekend\n",
    "def weekendDrops():\n",
    "    \n",
    "    weekendDrops=dropsSlider.value\n",
    "    amountOwedForWeekend = weekendDrops * round(float(routeDropdown.value.replace(' - weekend', '')),2)\n",
    "    print(\"€\" + str(amountOwedForWeekend) + '\\n')\n",
    "    \n",
    "def route1():\n",
    "    \n",
    "# 1-100\t€2.75\n",
    "# 101-110\t€2.24\n",
    "# 111-120\t€1.89\n",
    "# 121+\t€1.50\n",
    "\n",
    "    x=0.0\n",
    "    drops=dropsSlider.value\n",
    "    counter = 1\n",
    "\n",
    "    for drop in range(drops):  \n",
    "        if counter <= 100:\n",
    "            x = round(2.75 + x , 2)\n",
    "            counter += 1\n",
    "        elif counter > 100 and counter <= 110:\n",
    "            x = round(2.24 + x , 2)      \n",
    "            counter += 1\n",
    "        elif counter > 110 and counter <= 120:\n",
    "            x = round(1.89 + x , 2)      \n",
    "            counter += 1\n",
    "        elif counter > 120:\n",
    "            x = round(1.5 + x , 2)      \n",
    "            counter += 1\n",
    "            \n",
    "    print(\"€\" + str(x) + '\\n') \n",
    "\n",
    "    \n",
    "def route2():\n",
    "\n",
    "# 1-85\t\t€2.30\n",
    "# 86-95\t\t€2.00\n",
    "# 96-105\t€1.70\n",
    "# 106+\t\t€1.40\n",
    "    \n",
    "    x=0.0\n",
    "    drops=dropsSlider.value\n",
    "    counter = 1\n",
    "\n",
    "    for drop in range(drops):  \n",
    "        if counter <= 85:\n",
    "            x = round(2.3 + x , 2)\n",
    "            counter += 1\n",
    "        elif counter > 85 and counter <= 95:\n",
    "            x = round(2.0 + x , 2)      \n",
    "            counter += 1\n",
    "        elif counter > 95 and counter <= 105:\n",
    "            x = round(1.7 + x , 2)      \n",
    "            counter += 1\n",
    "        elif counter > 105:\n",
    "            x = round(1.4 + x , 2)      \n",
    "            counter += 1\n",
    "            \n",
    "    print(\"€\" + str(x) + '\\n') \n",
    "    \n",
    "    \n",
    "\n",
    "def route3():\n",
    "    \n",
    "# 1-95\t€2.70\n",
    "# 96-105\t€2.16\n",
    "# 106-115\t€1.84\n",
    "# 116+\t€1.50\n",
    "\n",
    "    x=0.0\n",
    "    drops=dropsSlider.value\n",
    "    counter = 1\n",
    "\n",
    "    for drop in range(drops):  \n",
    "        if counter <= 95:\n",
    "            x = round(2.70 + x , 2)\n",
    "            counter += 1\n",
    "        elif counter > 95 and counter <= 105:\n",
    "            x = round(2.16 + x , 2)      \n",
    "            counter += 1\n",
    "        elif counter > 105 and counter <= 115:\n",
    "            x = round(1.84 + x , 2)      \n",
    "            counter += 1\n",
    "        elif counter > 115:\n",
    "            x = round(1.50 + x , 2)      \n",
    "            counter += 1\n",
    "            \n",
    "    print(\"€\" + str(x) + '\\n') \n",
    "    \n",
    "    \n",
    "\n",
    "def route4():\n",
    "    \n",
    "# 1-99\t€2.50\n",
    "# 100-109\t€2.00\n",
    "# 110-119\t€1.70\n",
    "# 120+\t€1.40\n",
    "\n",
    "    x=0.0\n",
    "    drops=dropsSlider.value\n",
    "    counter = 1\n",
    "\n",
    "    for drop in range(drops):  \n",
    "        if counter <= 99:\n",
    "            x = round(2.50 + x , 2)\n",
    "            counter += 1\n",
    "        elif counter > 99 and counter <= 109:\n",
    "            x = round(2.00 + x , 2)      \n",
    "            counter += 1\n",
    "        elif counter > 109 and counter <= 119:\n",
    "            x = round(1.70 + x , 2)      \n",
    "            counter += 1\n",
    "        elif counter > 119:\n",
    "            x = round(1.40 + x , 2)      \n",
    "            counter += 1\n",
    "            \n",
    "    print(\"€\" + str(x) + '\\n') \n",
    "    \n",
    "\n",
    "def route5():\n",
    "\n",
    "# 1-90\t€2.70\n",
    "# 91-100\t€2.16\n",
    "# 101-110\t€1.84\n",
    "# 111+\t€1.50\n",
    "\n",
    "    x=0.0\n",
    "    drops=dropsSlider.value\n",
    "    counter = 1\n",
    "\n",
    "    for drop in range(drops):  \n",
    "        if counter <= 90:\n",
    "            x = round(2.70 + x , 2)\n",
    "            counter += 1\n",
    "        elif counter > 90 and counter <= 100:\n",
    "            x = round(2.16 + x , 2)      \n",
    "            counter += 1\n",
    "        elif counter > 100 and counter <= 110:\n",
    "            x = round(1.84 + x , 2)      \n",
    "            counter += 1\n",
    "        elif counter > 110:\n",
    "            x = round(1.50 + x , 2)      \n",
    "            counter += 1\n",
    "            \n",
    "    print(\"€\" + str(x) + '\\n')     \n",
    "    \n",
    "\n",
    "def route6():\n",
    "# 1-85\t€2.50\n",
    "# 86-95\t€2.00\n",
    "# 96-105\t€1.70\n",
    "# 106+\t€1.40\n",
    "\n",
    "    x=0.0\n",
    "    drops=dropsSlider.value\n",
    "    counter = 1\n",
    "\n",
    "    for drop in range(drops):  \n",
    "        if counter <= 85:\n",
    "            x = round(2.50 + x , 2)\n",
    "            counter += 1\n",
    "        elif counter > 85 and counter <= 95:\n",
    "            x = round(2.00 + x , 2)      \n",
    "            counter += 1\n",
    "        elif counter > 95 and counter <= 105:\n",
    "            x = round(1.70 + x , 2)      \n",
    "            counter += 1\n",
    "        elif counter > 105:\n",
    "            x = round(1.40 + x , 2)      \n",
    "            counter += 1\n",
    "            \n",
    "    print(\"€\" + str(x) + '\\n')     \n",
    "\n",
    "    \n",
    "def route7():\n",
    "    \n",
    "# 1-100\t€2.70\n",
    "# 101-110\t€2.16\n",
    "# 111-120\t€1.84\n",
    "# 121+\t€1.50\n",
    "\n",
    "    x=0.0\n",
    "    drops=dropsSlider.value\n",
    "    counter = 1\n",
    "\n",
    "    for drop in range(drops):  \n",
    "        if counter <= 100:\n",
    "            x = round(2.70 + x , 2)\n",
    "            counter += 1\n",
    "        elif counter > 100 and counter <= 110:\n",
    "            x = round(2.16 + x , 2)      \n",
    "            counter += 1\n",
    "        elif counter > 110 and counter <= 120:\n",
    "            x = round(1.84 + x , 2)      \n",
    "            counter += 1\n",
    "        elif counter > 120:\n",
    "            x = round(1.50 + x , 2)      \n",
    "            counter += 1\n",
    "            \n",
    "    print(\"€\" + str(x) + '\\n')     \n",
    "    \n",
    "\n",
    "def runCalculation():\n",
    " \n",
    "    if routeDropdown.value in ['2.75 - 100']:\n",
    "        route1()\n",
    "    elif routeDropdown.value in ['2.30 - 85']:\n",
    "        route2()\n",
    "    elif routeDropdown.value in ['2.70 - 95']:\n",
    "        route3()\n",
    "    elif routeDropdown.value in ['2.50 - 99']:\n",
    "        route4()\n",
    "    elif routeDropdown.value in ['2.70 - 90']:\n",
    "        route5()\n",
    "    elif routeDropdown.value in ['2.50 - 85']:\n",
    "        route6()\n",
    "    elif routeDropdown.value in ['2.70 - 100']:\n",
    "        route7()\n",
    "    elif routeDropdown.value in ['2.70 - weekend','3.50 - weekend']:\n",
    "        weekendDrops()\n",
    "        \n",
    "def on_button_clicked(b):\n",
    "    runCalculation()\n",
    "    \n",
    "display(button, output)\n",
    "button.on_click(on_button_clicked)"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.7.6"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}