import pandas as pd

def dict_():
    
    name_g  = 'Guilherme'
    goals_g = 45
    age_g   = 21
    g_data  = [name_g, goals_g, age_g]
    
    name_l  = 'Leonardo'
    goals_l = 23
    age_l   = 21
    l_data  = [name_l, goals_l, age_l]
    
    data_dict = {}
    
    #guilherme = {0 : [name_g, goals_g, age_g]}
    #leonardo  = {1 : [name_l, goals_l, age_l]}
    
    #data_dict.update(guilherme)
    
    #print(data_dict)
    
    #data_dict.update(leonardo)
    
    #print(data_dict)
    
    #df = pd.DataFrame.from_dict(data_dict, orient='index')
    #print(df)
    
    #df.columns = ["Name", "Goals", "Age"]
    #print(df)

    data = []
    data.append(g_data)
    print(data)
    
    data.append(l_data)
    print(str(data) + "\n\n")
    
    print(pd.DataFrame(data, columns=['Name', 'Goals', 'Age']))

def teams_id(id_):
    
    teams_dict = {
        2  : "Athletico-PR",
        3  : "Atletico-GO", 
        4  : "Atletico-MG",
        5  : "Bahia",
        6  : "Botafogo",
        7  : "Bragantino",
        8  : "Ceara",
        9  : "Corinthians",
        10 : "Coritiba",
        11 : "Flamengo",
        12 : "Fluminense",
        13 : "Fortaleza",    
        14 : "Goias",
        15 : "Gremio",
        16 : "Internacional",
        17 : "Palmeiras",
        18 : "Santos",
        19 : "Sao_Paulo",
        20 : "Sport",
        21 : "Vasco",
    }

    name = teams_dict[id_]
    print(name)

if __name__ == "__main__":
    
    teams_id(15)
    #dict_()    