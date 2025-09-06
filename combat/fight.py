"""
Module defining the combat system.
"""
# ULEPSZONY IMPORT: Importujemy tylko to, co potrzebne, i pod czytelną nazwą
from saving_data.save_and_load_player import save_player_to_json

class Fight:
    """
    Manages a combat encounter between a player and a monster.
    """
    def __init__(self, player, monster):
        """
        Initialize a new fight.

        Args:
            player (Player): The player character.
            monster (Monster): The monster character.
        """
        self.player = player
        self.monster = monster
        print("\n--- A fight begins! ---")
        print(f"{player.name} (HP: {player._hit_points}/{player._hit_points_max}) vs. {monster.name} (HP: {monster.hit_points})")
        print("-" * 25)


    def start(self):
        """
        Starts and manages the turn-based combat loop.
        """
        try:
            while self.player.alive and self.monster.alive:
                # Tura gracza
                input("Press Enter to attack...") # Dodajemy pauzę, aby gracz mógł śledzić akcję
                self.player.attack(self.monster)
                
                # Sprawdzenie, czy potwór przeżył
                if not self.monster.alive:
                    break

                # Tura potwora
                print(f"{self.monster.name} attacks!")
                self.monster.attack(self.player)

            # Logika po zakończeniu walki
            if self.player.alive:
                print(f"\n--- {self.player.name} won the fight! ---")
                
                # Zdobywanie nagród
                gold_reward = self.monster.gold_reward()
                exp_reward = self.monster.exp_reward()
                
                self.player.gold += gold_reward
                
                # --- KLUCZOWA POPRAWKA ---
                # Używamy metody gain_experience, aby obsłużyć również awans na wyższy poziom!
                self.player.gain_experience(exp_reward)
                
                print(f"{self.player.name} received {gold_reward} gold.")
                
                # Zapisujemy stan gry
                save_player_to_json(self.player)
                
            else:
                print(f"\n--- {self.monster.name} won the fight! You have been defeated. ---")

        except Exception as e:
            print(f"An error occurred during the fight: {e}")