###
#/***************************************************
#File Name: piechart.py
#Version/Date: 0.2 (2020-05-06)
#Programmer/ID: Raja Muhammad Darwisy bin Raja Ahmad(11911000792)
#Project Name: Smart Finance Manager 
#Teammates: Raven Lim Zhe Xuan , Nagaindran A/L Kanaseelanayagam, Fong Zheng Wei
#Course/Term: PSP0201 Mini IT Project (2019/20 T3)
#***************************************************/
###


""" 
███████ ██       █████   ██████   ██████  ███████ ██████                                                       
██      ██      ██   ██ ██       ██       ██      ██   ██                                                      
█████   ██      ███████ ██   ███ ██   ███ █████   ██   ██                                                      
██      ██      ██   ██ ██    ██ ██    ██ ██      ██   ██                                                      
██      ███████ ██   ██  ██████   ██████  ███████ ██████                                                       
                                                                                                               
                                                                                                               
███    ██  ██████  ████████     ██ ███    ██  ██████ ██      ██    ██ ██████  ███████ ██████      ██ ███    ██ 
████   ██ ██    ██    ██        ██ ████   ██ ██      ██      ██    ██ ██   ██ ██      ██   ██     ██ ████   ██ 
██ ██  ██ ██    ██    ██        ██ ██ ██  ██ ██      ██      ██    ██ ██   ██ █████   ██   ██     ██ ██ ██  ██ 
██  ██ ██ ██    ██    ██        ██ ██  ██ ██ ██      ██      ██    ██ ██   ██ ██      ██   ██     ██ ██  ██ ██ 
██   ████  ██████     ██        ██ ██   ████  ██████ ███████  ██████  ██████  ███████ ██████      ██ ██   ████ 
                                                                                                               
                                                                                                               
███    ███  █████  ██ ███    ██     ██████  ██████   ██████   ██████  ██████   █████  ███    ███               
████  ████ ██   ██ ██ ████   ██     ██   ██ ██   ██ ██    ██ ██       ██   ██ ██   ██ ████  ████               
██ ████ ██ ███████ ██ ██ ██  ██     ██████  ██████  ██    ██ ██   ███ ██████  ███████ ██ ████ ██               
██  ██  ██ ██   ██ ██ ██  ██ ██     ██      ██   ██ ██    ██ ██    ██ ██   ██ ██   ██ ██  ██  ██               
██      ██ ██   ██ ██ ██   ████     ██      ██   ██  ██████   ██████  ██   ██ ██   ██ ██      ██               
                                                                                                               
                                                                                                            
 """


import matplotlib.pyplot as plt

# Data to plot
labels = 'Clothing', 'Entertainment', 'Foods and drinks', 'Transportation'
sizes = [215, 130, 245, 210] #sample data
colors = ['gold', 'yellowgreen', 'lightcoral', 'lightskyblue']
explode = (0.1, 0, 0, 0)  # explode 1st slice

# Plot
plt.pie(sizes, explode=explode, labels=labels, colors=colors,
autopct='%1.1f%%', shadow=True, startangle=140)

plt.axis('equal')
plt.show()



if __name__ == "__main__":
    print("Please run main.py instead")
    pass