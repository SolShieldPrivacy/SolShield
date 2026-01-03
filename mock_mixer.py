"""
Mock-симуляция privacy-миксера SolShield
ВАЖНО: Это НЕ работает на блокчейне! Только демонстрация концепции.
"""

import random
from datetime import datetime

class MockMixer:
    def __init__(self):
        self.pool = []  # список "внесённых" транзакций
        self.treasury = 0
        self.shield_balance = {"user1": 1500, "user2": 300}

    def mix(self, amount_sol: float, user: str, shield_used: int = 0):
        if shield_used > self.shield_balance.get(user, 0):
            return "Недостаточно $SHIELD"
        
        fee = 0.5 + (random.random() * 1.5)  # 0.5–2 SOL
        if shield_used >= 1000:
            fee *= 0.6  # скидка 40%
        elif shield_used >= 500:
            fee *= 0.8  # скидка 20%

        print(f"[{datetime.now()}] Mock mix:")
        print(f"  Внесено: {amount_sol} SOL от {user}")
        print(f"  Комиссия: {fee:.2f} SOL (оплачено в $SHIELD эквивалент)")
        print(f"  Использовано $SHIELD: {shield_used}")
        
        self.treasury += fee
        self.pool.append({"from": user, "amount": amount_sol})
        
        # Симуляция выхода
        output_address = f"new_{random.randint(1000,9999)}"
        print(f"  Вывод: {amount_sol - fee:.2f} SOL → {output_address}")
        print("-" * 50)
        return output_address

# Пример использования
if __name__ == "__main__":
    mixer = MockMixer()
    mixer.mix(10.0, "user1", shield_used=1200)
    mixer.mix(5.0, "user2", shield_used=300)
    print(f"В treasury накоплено: {mixer.treasury:.2f} SOL")