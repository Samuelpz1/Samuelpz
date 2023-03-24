def get_match_result(data):
    matches_n = list(map(lambda item: item["Match No."],data))
    #matches_n = list(dict.fromkeys(matches_n))
    #print(matches_n)
    score = list(map(lambda item : item ["Goal"], data))
    #print(len(score))
    local_score = score[0:128:2]
    away_score =  score[1:128:2]
    counter = 0
    while counter <64:
        local_score[counter] = int(local_score[counter])
        away_score[counter] = int(away_score[counter])
        counter += 1
    return local_score , away_score

def get_winner(local_score , away_score):
    local_win = 0
    away_win = 0
    draw_win = 0
    limit = len(local_score)
    counter = 0
    while counter < limit:
        #print("Local : ", local_score[counter], " Away : ", away_score[counter])
        result = local_score[counter] - away_score[counter]
        if (result<0):
            away_win+=1
        elif(result>0):
            local_win+=1
        else:
            draw_win+=1
        counter += 1
    
    keys = ["Local Wins","Away Wins","Draw"]
    values = [local_win,away_win,draw_win]
    result = {keys:values for (keys,values)in zip(keys,values)}
    return result
        

def generate_pie_chart(labels,values):
    import matplotlib.pyplot as plt
    fig, ax = plt.subplots()
    ax.pie(values,labels=labels)
    ax.axis("equal")
    plt.show()


if __name__=="__main__":
    data = get_data("./data.csv")