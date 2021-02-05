def ndc(url,msp,desired_column,total_rows):

    import pandas as pd
   
    from matplotlib import pyplot as plt

    #The data set is read into a data frame 'df'
    df = pd.read_csv(url)
   
    """Here a dataframe of most significant digits of the digits stored
    in the desired column of the provided data frame"""
    
    df[msp] = df[desired_column].astype(str).str[0]
    
    #Here a set of msp and their occurence percentages are obtained
    collection = ((df[msp].value_counts()*100)/total_rows)

    #test_dictionary maps the msp values with their occurence percentages
    mapping_dictionary = dict(collection)

    """Here the key is obtained for the value which has the max occurence
    percentage in the desired column of the provided dataset """
    max_obtained_percentage_key = max(mapping_dictionary, key=mapping_dictionary.get)

    """Here result is obtained according to Benford's law i.e if
    max_obtained_percentage_key is 1 then the desired column is valid else
    the desired column is invalid which will be illustated in the bar plot"""
    if max_obtained_percentage_key  == '1':
        plt.title('Valid Desired Column Data')
    else:
        plt.title('Invalid Desired Column Data')
        
    #Here the msp and their occurence percentages are seperated for plotting
    msp,occurence_percentages = mapping_dictionary.keys(),mapping_dictionary.values()

    """Then the msp and their occurence percentages will be plotted along
    with the result"""
    plt.bar(msp,occurence_percentages)

    plt.show()
    
