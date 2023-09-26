import utils
import reader

def run():
    data = reader.get_data("./data.csv")
    local_score , away_score = utils.get_match_result(data)
    result = utils.get_winner(local_score, away_score)
    utils.generate_pie_chart(result.keys(), result.values())



if __name__ =="__main__":
    run()