#python
#Skeleton Code

import string
import random

class Player:
    def __init__(self, name, hp, damage, correct_alp):
        self.name = name      # 이름
        self.hp = hp          # 생명력
        self.damage = damage  # 데미지
        self.correct_alp = 0  # 알파벳 맞춘 횟수

class Game:
    def __init__(self):
        self.player = []  # 캐릭터의 목록. start_game()에서 생성
        self.user_character = ""  # 사용자가 선택한 캐릭터
        self.remain_alp = list(string.ascii_uppercase)  # 남은 알파벳
        self.cur_string = ["_"] * 10  # 현재까지의 글자상태를 저장
        self.answer_string = ""  # 랜덤 10글자 단어

    def start_game(self):
        """
        - [ 게임 시작 전 ] 부분을 담당하는 함수 입니다.
        - 캐릭터들을 초기화 하고, 사용자가 플레이할 캐릭터를 선택합니다.
        - 랜덤 알파벳 10글자로 이루어진 answer_string 을 생성합니다.
        - 동일 클래스의 game()에서 호출됩니다.
        """
        self.player.append(Player("김건웅", 50, 20, 0))
        self.player.append(Player("김현주", 70, 25, 0))
        self.player.append(Player("박진혁", 80, 30, 0))
        self.player.append(Player("유송경", 90, 35, 0))
        

        n = int(input("당신의 캐릭터 번호를 선택해주세요 (1,2,3,4): "))
        character = self.player[n-1].name
        self.user_character += character
        print("당신의 캐릭터는 %s입니다.\n" % self.user_character)

        for i in range(10):
            self.answer_string += random.choice(string.ascii_uppercase)
        print("컴퓨터가 랜덤으로 만든 답입니다. 플레이어에게는 보이지 않습니다. RWECLKUEHS\n")

    def sort_data(self, i):        
        """ 
        - [ 게임 진행 ] 부분에서 게임진행 순서를 담당하는 함수 입니다.
        - 동일 클래스의 game()에서 호출됩니다.
        """
        
        if i==1:
            self.player.sort(key=lambda p : p.name)
        elif i==2 or i==3:
            self.player.sort(key=lambda p : p.hp, reverse=True)

    def play_game(self):
        """ 
        - [ 게임 진행 ] 부분을 담당하는 함수 입니다.
        - 동일 클래스의 game()에서 호출됩니다.
        """

        print(
            f"게임은 {self.player[0].name},{self.player[1].name},{self.player[2].name},{self.player[3].name} 순으로 진행됩니다.\n")

        for i in range(4):

            if self.player[i].name == self.user_character:
                print("***** 내 캐릭터 *****")
            else:
                print(f"***** {i+1} 캐릭터 *****")

            print(f"이름: {self.player[i].name} (HP: {self.player[i].hp})")
            

            while(True):
                alph = input("선택알파벳: ")
                if self.remain_alp.count(alph) == 0:
                    print("알파벳을 다시 선택하세요.")
                else:
                    self.remain_alp.remove(alph)
                    break


            if self.answer_string.count(alph) >= 1:
                print("***** 맞았습니다 ᵔεᵔ  *****")
                self.player[i].correct_alp += 1
                for i in range(10):
                    if self.answer_string[i] == alph:
                        self.cur_string[i] = alph
                for i in self.cur_string:
                    print(i, end=" ")
            else:
                print("***** 틀렸습니다 (ﾟ⊿ﾟ)  ******")
                self.player[i].hp -= self.player[i].damage
                print("%s님은 틀렸기 때문에 HP가 %d 남았습니다." % (self.player[i].name, self.player[i].hp), end="")
            print("\n")

    def game_result(self):
        """
        - [ 게임 종료 후 ] 부분을 담당하는 함수 입니다.
        - 게임의 결과를 생명력순, 알파벳 맞춘 횟수 순 두가지의 경우로 출력해야 합니다.
        - 동일 클래스의 game()에서 호출됩니다.
        """

        print("\n\n******************* 게임이 끝났습니다 *******************")

        print("=============================")
        print("     게임 순위 - 생명력")
        print("=============================")
        self.player.sort(key = lambda p : p.hp, reverse=True)
        for i in range(4):
            if self.player[i].hp < 0 :
                print("%d등: %s (사망)" % (i+1, self.player[i].name)) 
            else :
                print("%d등: %s (HP:%d)" % (i+1, self.player[i].name, self.player[i].hp)) 
        print()
            
        print("=============================")
        print(" 게임 순위 - 알파벳 맞춘 횟수")
        print("=============================")
        self.player.sort(key = lambda p : p.correct_alp, reverse=True)
        for i in range(4):
            print("%d등: %s %d회" % (i+1, self.player[i].name, self.player[i].correct_alp)) 

    def game(self):
        """
        - 게임 운영을 위한 함수입니다. 
        - 별도의 코드 작성이 필요 없습니다. 
        """

        self.start_game()

        print("******************* 게임 시작 *******************\n")

        for i in range(1, 4):
            print("===========================")
            print(f"     ROUND {i} - START")
            print("===========================")

            self.sort_data(i)
            self.play_game()

            print("===========================")
            print(f"     ROUND {i} - END")
            print("===========================")

        self.game_result()

if __name__ == '__main__':

    """
    - 코드를 실행하는 부분입니다. 
    - 역시 별도의 코드 작성이 필요 없습니다. 
    """
    game = Game()
    game.game()
