
# pick one of the options to find something about i
def options():
    print("Please enter the corresponding number to find more answers about your questions;")
    info_option = input("1. How much of a threat is global warming to our planet and the environment?\n"
                   "2. How will this affect me?\n"
                   "3. What is climate change?\n "
                   "4. What is the difference between global warming and climate change?\n"
                   "5. Is there proof of Climate change and global warming?\n"
                   "6. Why be concerned about a degree or two change in the average global temperature?\n"
                   "7. What is Climate?\n"
                   "8. What are the benefits of acting on Climate change now?\n"
                   "9. What happens if we do nothing to stop climate change?\n"
                   "10.What is Carbon Footprint? And why should I calculate it?\n"
                   "11.TAKE ME BACK TO MENU!\n")

    if info_option == '1':
        print("How much of a threat is global warming to our planet and the environment?")
        print('''
            Climate change poses a fundamental threat to the places, species and people’s livelihoods 
            To adequately address this crisis we must urgently reduce carbon pollution and prepare for the
            consequences of global warming which we are already experiencing. We need to do the following; better
            policies to fight climate change, engage with businesses to reduce carbon emissions 
            and help people and nature adapt to a changing climate, and much much more.
            ''')

    if info_option == '2':
        print("How will this affect me?")
        print('''
            Climate change may affect our health and wellbeing through the impacts of extreme events,
            worsening air quality, changes in the spread of infectious diseases, threats to food and
            water quality and quantity and effects on our mental health.
                ''')

    if info_option == '3':
        print("What is climate change?")
        print('''
            Climate change refers to long-term shifts in temperatures and weather patterns. These shifts may be natural
            but since the 1800s, human activities have been the main driver of climate change, primarily due to the  
            burning of fossil fuels (like coal, oil and gas), which produces heat-trapping gases.
            ''')

    if info_option == '4':
        print("What is the difference between global warming and climate change?")
        print('''
            "Global warming” refers to the rise in global temperatures due mainly to the increasing concentrations of 
            greenhouse gases in the atmosphere. “Climate change” refers to the increasing changes in the measures of climate 
            over a long period of time – including precipitation, temperature, and wind patterns.
            ''')

    if info_option == '5':
        print("Is there proof of Climate change and global warming?")
        print('''
            Ice cores drawn from Greenland, Antarctica, and tropical mountain glaciers show that Earth's climate 
            responds to changes in greenhouse gas levels. Ancient evidence can also be found in tree rings, ocean 
            sediments, coral reefs, and layers of sedimentary rocks. There is much much more evidence, THEREFORE IT IS 
            PROVEN.
            ''')

    if info_option == '6':
        print("Why be concerned about a degree or two change in the average global temperature?")
        print('''
            If warming reaches 2 degrees Celsius, more than 70 percent of Earth's coastlines will see sea-level rise 
            greater than 0.2 meters, resulting in increased coastal flooding, beach erosion, salinization of water 
            supplies and other impacts on humans and ecological systems.
            ''')

    if info_option == '7':
        print("What is Climate?")
        print('''
        Climate is the long-term pattern of weather in a particular area. Weather can change from hour-to-hour, 
        day-to-day, month-to-month or even year-to-year. A region's weather patterns, usually tracked for at least
        30 years, are considered its climate.
        ''')

    if info_option == '8':
        print("What are the benefits of acting on Climate change now?")
        print('''
            There are a number of benefits that can result from taking action to reduce greenhouse gas emissions and 
            adapt to climate change, including: Improvements to individual and public health due to more active 
            lifestyles, cleaner air, and improved water and soil quality, and much much more.
            ''')

    if info_option == '9':
        print("What happens if we do nothing to stop climate change?")
        print('''
            The wildlife we love and their habitat will be destroyed, leading to mass species extinction. Superstorms, 
            drought, and heat waves would become increasingly common and more extreme, leading to major health crises 
            and illness. Agricultural production would plummet, likely leading to global food shortages and famine. Etc.
            ''')

    if info_option == '10':
        print("What is Carbon Footprint? And why should I calculate it?")
        print('''
            your carbon footprint is the amount of greenhouse gas you produce in units of carbon dioxide. This footprint
            is determined by your daily lifestyle and activities, such as travel (car, plane, train, etc), electrical 
            use, consumption of products and services, foods you eat, etc. You should calculate your footprint to find
            out how much YOU'RE affecting the planet in negative ways.
            ''')

    if info_option == '11':
        return options


options()
