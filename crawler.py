# WebDriver
from selenium import webdriver

# Selenium Operator
import selenium_operator as op

# Utils
import time
import pandas as pd
import sys

class Crawler:
    
    def __init__(self):
        
        # Setting base url
        self.base_url = 'https://www.cartolafcbrasil.com.br/scouts/cartola-fc-2021'
        
        # Creating driver
        self.driver = webdriver.Chrome(executable_path = 'driver\chromedriver.exe')
        
        # Initializing in main cartola data page
        self.driver.get(self.base_url)

        # Creating operator
        self.op = op.SeleniumOperator(self.driver)
        
        # Data to be extracted
        self.data = []
        self.aux_data = []
        
        # DataFrame 
        self.df = []
        
    def get_total_rounds(self):    
        pass
    
    def round_select(self, round_id):
        
        url = f'https://www.cartolafcbrasil.com.br/scouts/cartola-fc-2021/rodada-{round_id}'
        self.driver.get(url)
        
        time.sleep(3)
        
        #round_tab = '//*[@id="ctl00_cphMainContent_drpRodadas"]'
        #self.op.find_and_click(round_tab, 1)
        
        """
        
        - //*[@id="ctl00_cphMainContent_drpRodadas"]/option[2]
        - //*[@id="ctl00_cphMainContent_drpRodadas"]/option[3]
        - //*[@id="ctl00_cphMainContent_drpRodadas"]/option[4]
        - ...
        
        """
        
        #round_option = f'//*[@id="ctl00_cphMainContent_drpRodadas"]/option[{round_id}]'
        #self.op.find_and_click(round_option, 1)
        
        #search_button = '//*[@id="ctl00_cphMainContent_btnPesquisar"]'
        #self.op.find_and_click(search_button, 1)
        
    def club_selector(self, club_id):
        
        # Selecting club
        club_list = '//*[@id="ctl00_cphMainContent_drpClubes"]'
        self.op.find_and_click(club_list, 0.25)
        
        club_option = f'//*[@id="ctl00_cphMainContent_drpClubes"]/option[{club_id}]'
        self.op.find_and_click(club_option, 0.25)
        
        """
        CLUB OPTIONS
        
        - //*[@id="ctl00_cphMainContent_drpClubes"]/option[2]
        - //*[@id="ctl00_cphMainContent_drpClubes"]/option[3]
        - ...
        - //*[@id="ctl00_cphMainContent_drpClubes"]/option[21]
        """

        #breakpoint()
    
    def position_selector(self, pos_id):
        
        pos_list = '//*[@id="ctl00_cphMainContent_drpPosicoes"]'
        self.op.find_and_click(pos_list, 0.25)
        
        pos_option = f'//*[@id="ctl00_cphMainContent_drpPosicoes"]/option[{pos_id}]'
        self.op.find_and_click(pos_option, 0.25)
        
        """
        POSITION OPTIONS
        
        - //*[@id="ctl00_cphMainContent_drpPosicoes"]/option[1]
        - ...
        - //*[@id="ctl00_cphMainContent_drpPosicoes"]/option[7]
        
        """
        
        #breakpoint()
    
    def status_selector(self, status_id):
        
        status_list = '//*[@id="ctl00_cphMainContent_drpStatus"]'
        self.op.find_and_click(status_list, 0.25)
        
        status_option = f'//*[@id="ctl00_cphMainContent_drpStatus"]/option[{status_id}]'
        self.op.find_and_click(status_option, 0.25)
        
        """
        STATUS OPTIONS
        
        - //*[@id="ctl00_cphMainContent_drpStatus"]/option[1]
        - ...
        - //*[@id="ctl00_cphMainContent_drpStatus"]/option[6]
        """
                
        #breakpoint()
    
    def press_filter_button(self):
        
        filter_button = '//*[@id="ctl00_cphMainContent_btnFiltrar"]'
        self.op.find_and_click(filter_button, 0.25)
        
        #breakpoint()
    
    def extract_data(self, pl_id, team_name, position_name):
        
        aux_data = []
        aux_data.append(team_name)
        aux_data.append(position_name)
        
        lock = 0.5
        
        if pl_id < 10:
            player_xp = f'//*[@id="ctl00_cphMainContent_gvList_ctl0{pl_id}_aLink"]'
            
        else:
            player_xp = f'//*[@id="ctl00_cphMainContent_gvList_ctl{pl_id}_aLink"]'
        
        player_name      = self.op.get_text(player_xp, lock).partition("(")[0]
        aux_data.append(player_name)
        print(f"\nPlayer Name: {player_name}\n")
        #breakpoint()
        
        actual_price_xp  = f'//*[@id="ctl00_cphMainContent_gvList"]/tbody/tr[{pl_id}]/td[3]'
        actual_price     = self.fixing_float(self.op.get_text(actual_price_xp, lock))
        aux_data.append(actual_price)
        print(f"\nActual Price: {actual_price}\n")
        
        games_played_xp  = f'//*[@id="ctl00_cphMainContent_gvList"]/tbody/tr[{pl_id}]/td[4]'
        games_played     = self.fixing_float(self.op.get_text(games_played_xp, lock))
        aux_data.append(games_played)
        print(f"\nGames Played: {games_played}\n")
        
        average_score_xp = f'//*[@id="ctl00_cphMainContent_gvList"]/tbody/tr[{pl_id}]/td[5]'
        average_score    = self.fixing_float(self.op.get_text(average_score_xp, lock))
        aux_data.append(average_score)
        print(f"\nAverage Score: {average_score}\n")
        
        last_score_xp    = f'//*[@id="ctl00_cphMainContent_gvList"]/tbody/tr[{pl_id}]/td[6]'
        last_score       = self.fixing_float(self.op.get_text(last_score_xp, lock))
        aux_data.append(last_score)
        print(f"\nLast Score: {last_score}\n")
        
        variation_xp     = f'//*[@id="ctl00_cphMainContent_gvList"]/tbody/tr[{pl_id}]/td[7]'
        variation        = self.fixing_float(self.op.get_text(variation_xp, lock))
        aux_data.append(variation)
        print(f"\nVariation: {variation}\n")
        
        ds_xp            = f'//*[@id="ctl00_cphMainContent_gvList"]/tbody/tr[{pl_id}]/td[8]'
        ds               = self.fixing_float(self.op.get_text(ds_xp, lock))
        aux_data.append(ds)
        print(f"\nDS: {ds}\n")
        
        goals_xp         = f'//*[@id="ctl00_cphMainContent_gvList"]/tbody/tr[{pl_id}]/td[9]'
        goals            = self.fixing_float(self.op.get_text(goals_xp, lock))
        aux_data.append(goals)
        print(f"\nGoals: {goals}\n")
        
        assists_xp       = f'//*[@id="ctl00_cphMainContent_gvList"]/tbody/tr[{pl_id}]/td[10]'  
        assists          = self.fixing_float(self.op.get_text(assists_xp, lock)) 
        aux_data.append(assists)
        print(f"\nAssists: {assists}\n")
        
        sg_xp            = f'//*[@id="ctl00_cphMainContent_gvList"]/tbody/tr[{pl_id}]/td[11]'
        sg               = self.fixing_float(self.op.get_text(sg_xp, lock))
        aux_data.append(sg)
        print(f"\nSG: {sg}\n")
        
        fs_xp            = f'//*[@id="ctl00_cphMainContent_gvList"]/tbody/tr[{pl_id}]/td[12]'
        fs               = self.fixing_float(self.op.get_text(fs_xp, lock))
        aux_data.append(fs)
        print(f"\nFS: {fs}\n")
        
        ff_xp            = f'//*[@id="ctl00_cphMainContent_gvList"]/tbody/tr[{pl_id}]/td[13]'
        ff               = self.fixing_float(self.op.get_text(ff_xp, lock))
        aux_data.append(ff)
        print(f"\nFF: {ff}\n")
        
        fd_xp            = f'//*[@id="ctl00_cphMainContent_gvList"]/tbody/tr[{pl_id}]/td[14]'
        fd               = self.fixing_float(self.op.get_text(fd_xp, lock))
        aux_data.append(fd)
        print(f"\nFD: {fd}\n")
        
        ft_xp            = f'//*[@id="ctl00_cphMainContent_gvList"]/tbody/tr[{pl_id}]/td[15]'
        ft               = self.fixing_float(self.op.get_text(ft_xp, lock))
        aux_data.append(ft)
        print(f"\nFT: {ft}\n")
        
        dd_xp            = f'//*[@id="ctl00_cphMainContent_gvList"]/tbody/tr[{pl_id}]/td[16]'
        dd               = self.fixing_float(self.op.get_text(dd_xp, lock))
        aux_data.append(dd)
        print(f"\nDD: {dd}\n")
        
        dp_xp            = f'//*[@id="ctl00_cphMainContent_gvList"]/tbody/tr[{pl_id}]/td[17]'
        dp               = self.fixing_float(self.op.get_text(dp_xp, lock))
        aux_data.append(dp)
        print(f"\nDP: {dp}\n")
        
        gc_xp            = f'//*[@id="ctl00_cphMainContent_gvList"]/tbody/tr[{pl_id}]/td[18]'
        gc               = self.fixing_float(self.op.get_text(gc_xp, lock))
        aux_data.append(gc)
        print(f"\nGC: {gc}\n")
        
        cv_xp            = f'//*[@id="ctl00_cphMainContent_gvList"]/tbody/tr[{pl_id}]/td[19]'
        cv               = self.fixing_float(self.op.get_text(cv_xp, lock))
        aux_data.append(cv)
        print(f"\nCV: {cv}\n")
        
        ca_xp            = f'//*[@id="ctl00_cphMainContent_gvList"]/tbody/tr[{pl_id}]/td[20]'
        ca               = self.fixing_float(self.op.get_text(ca_xp, lock))  
        aux_data.append(ca)
        print(f"\nCA: {ca}\n")
        
        pp_xp            = f'//*[@id="ctl00_cphMainContent_gvList"]/tbody/tr[{pl_id}]/td[21]'
        pp               = self.fixing_float(self.op.get_text(pp_xp, lock))
        aux_data.append(pp)
        print(f"\nPP: {pp}\n")
        
        gs_xp            = f'//*[@id="ctl00_cphMainContent_gvList"]/tbody/tr[{pl_id}]/td[22]'
        gs               = self.fixing_float(self.op.get_text(gs_xp, lock))     
        aux_data.append(gs)
        print(f"\nGS: {gs}\n")
        
        fc_xp            = f'//*[@id="ctl00_cphMainContent_gvList"]/tbody/tr[{pl_id}]/td[23]'
        fc               = self.fixing_float(self.op.get_text(fc_xp, lock))
        aux_data.append(fc)
        print(f"\nFC: {fc}\n")
        
        offside_xp       = f'//*[@id="ctl00_cphMainContent_gvList"]/tbody/tr[{pl_id}]/td[24]'
        offside          = self.fixing_float(self.op.get_text(offside_xp, lock))
        aux_data.append(offside)
        print(f"\nOFFSIDE: {offside}\n")
        
        pi_xp            = f'//*[@id="ctl00_cphMainContent_gvList"]/tbody/tr[{pl_id}]/td[25]'
        pi               = self.fixing_float(self.op.get_text(pi_xp, lock))
        aux_data.append(pi)
        print(f"\nPI: {pi}\n")
        
        self.aux_data.append(aux_data)
        
        #breakpoint()
        
    def create_dataframe(self, club_id, club_name, round_id):
        
        column_list = [
            'Team_Name',
            'Player_Name',
            'Position_Name',
            'Price',
            'Games',
            'Average_Score',
            'Last_Score',
            'Variation',
            'Desarme',
            'Goal',
            'Assist',
            'Clean_Sheet',
            'Falta_Sofrida',
            'Finalização_Fora',
            'Finalização_Defd',
            'Finalização_Trave',
            'Defesa_Dificil',
            'Defesa_Penalti',
            'Gol_Contra',
            'Cartao_Vermelho',
            'Cartao_Amarelo',
            'Gol_Sofrido',
            'Penalti_Perdido',
            'Falta_Cometida',
            'Impedimento',
            'Passe_Incompleto'    
        ]
        
        #print(self.data[0])
        #print("\n\n")
        #print(self.data)
        
        df = pd.DataFrame(self.data[club_id - 2], columns = column_list)
        
        #print("\n\n")
        #print(df)
        #print("\n\n")
        
        df.to_csv(f"data_extracted/{club_name}_{round_id}.csv")
        
        self.df.append(df)
        
    def fixing_float(self, number):
        
        """
        Try de dentro   : caso o número possúa vírgula
        Except de dentro: caso o número não possúa vírgula
        Except de fora  : caso não seja um número (dado em branco)
        """
        
        try:
            try:
                return float(number.replace(',', '.'))        

            except:
                return float(number)
        except:
            return 0
    
    def insert_data(self):
        self.data.append(self.aux_data)
        self.aux_data = []
        
def teams_id(id_):
    
    # first: //*[@id="ctl00_cphMainContent_drpClubes"]/option[2]
    # last : //*[@id="ctl00_cphMainContent_drpClubes"]/option[21]

    teams_dict = {
        2   : "America-MG",
        3   : "Athletico-PR",
        4   : "Atletico-GO", 
        5   : "Atletico-MG",
        6   : "Bahia",
        7   : "Bragantino",
        8   : "Ceara",
        9   : "Chapecoense",
        10  : "Corinthians",
        11  : "Cuiaba",
        12  : "Flamengo",
        13  : "Fluminense",
        14  : "Fortaleza",    
        15  : "Gremio",
        16  : "Internacional",
        17  : "Juventude",
        18  : "Palmeiras",
        19  : "Santos",
        20  : "Sao_Paulo",
        21  : "Sport",
    }

    name = teams_dict[id_]    
    return name

def position_id(id_):
    
    pos_dict = {
        2: 'Goleiro',
        4: 'Zagueiro',
        3: 'Lateral',
        5: 'Meio-Campo',
        6: 'Atacante',
        7: 'Tecnico'
    }
    
    name = pos_dict[id_]
    return name

def main(round_atual):
    
    # Creating object
    c = Crawler()
    
    # Selecting round
    for round_id in range(round_atual,round_atual+1):
        
        c.round_select(round_id)
        
        # Filtering club and setting all player status
        for club_id in range(2,22):
            
            
            print("Selecionando Clube...")
            c.club_selector(club_id)
            c.press_filter_button()
            print("Clube selecionado!")

            # time.sleep(100)

            pl_id = 2
            
            # Filtering position

            for pos_id in range(2,8):
                c.position_selector(pos_id)
                c.press_filter_button()
                
                if pos_id == 2:
                    c.status_selector(1)
                    c.press_filter_button()
                    time.sleep(2)
                
                while True:
                    try:
                        c.extract_data(pl_id, teams_id(club_id), position_id(pos_id))
                        pl_id += 1
                    
                    except Exception as e:
                        print(f"\nNão conseguiu pegar os dados na posição: {pl_id}\nExceção: {e}")
                        pl_id = 2
                        break
            
            c.insert_data()
            c.create_dataframe(club_id, teams_id(club_id), round_id)    
        
    
if __name__ == "__main__":
    
    if len(sys.argv) < 1:
        print("Usage: python app.py <rodada>")
        sys.exit(-1)

    round_atual = int(sys.argv[1])
    print(f"Rodada Atual: {round_atual}\n\n")
    
    main(round_atual)    