def mean_cal(value):
    if isinstance(value,dict):
        the_mean=sum(value.values())/len(value)
    else:
        the_mean=sum(value)/len(value)
    
    return(the_mean)

    my_page=[8.8,9.1,9.9]
    my_dict={"Marie":10.9,"John":8.8,"Sam":9.1}
    print(mean_cal(my_dict))