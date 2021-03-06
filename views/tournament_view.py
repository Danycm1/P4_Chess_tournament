from models.tournament import Tournament


class TournamentView():

    def ask_information(self, dataRequested):
        print('Please type the ' + dataRequested)

    def display(self, message):
        ''' Helper function to display a message '''
        print(message)

    def display_tournaments_name(self, tournaments_to_display: list[Tournament]):
        ''' Display tournament name with index '''
        self.display('Choose a tournament')

        for index, tournament in enumerate(tournaments_to_display):
            print(f'{index + 1}: {tournament.name}')

    def display_players_name(self, players_to_display: list[Tournament]):
        ''' Display player name with index '''
        self.display('Choose 8 players to add')

        for index, player in enumerate(players_to_display):
            print(f'{index + 1}: {player}')
