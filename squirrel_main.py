import pandas
data = pandas.read_csv("./squirrel_count.csv")

fur_color = data["Primary Fur Color"].unique()
# print(fur_color)

grey_sq = data[data["Primary Fur Color"] == "Gray"]
grey_cnt = len(grey_sq)
# print(grey_cnt)

cinnamon_sq = data[data["Primary Fur Color"] == "Cinnamon"]
cinnamon_sq_cnt = len(cinnamon_sq)
# print(cinnamon_sq_cnt)

black_sq = data[data["Primary Fur Color"] == "Black"]
black_sq_cnt = len(black_sq)
# print(black_sq_cnt)

data_dictionary = {
    "Fur Color" : ["Gray", "Cinnamon", "Black"],
    "Count " : [grey_cnt, cinnamon_sq_cnt, black_sq_cnt]
}

data_frame = pandas.DataFrame(data_dictionary)
print(data_frame)

data_frame.to_csv("sq_csv")