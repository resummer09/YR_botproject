class Data:
    def __init__(self):
        # 유파: 딕셔너리
        self.clan = {'하스바닌군':0, '쿠라마신류':1, '하구레모노':2, '히라사카기관':3, '사립오토기학원':4,'오니의혈통':5}
        # 분야: 리스트
        self.expertise = ['기술','체술','인술','모술','전술','요술']
        # 특기: 리스트 딕셔너리
        self.skills = [{},
                      {},
                      {},
                      {},
                      {},
                      {}]

# 플레이어 클래스
class player:
    def __init__(self, name: str):
        self.name = name
        self.clan = None
        self.field = None
        self.hp = 0

        # 변조는 딕셔너리로 관리
        # 배경은 안 씀
        # 효과적용 셀프로 (생명력 감소 등)

    def setClan(self, clan:str):
        self.clan = clan
    def setSkill(self, skils:list):
        self.skills = []

# 턴 고지
# 플롯인법 사용 여부 확인
# 플롯 선택 (누른사람 선택완료 채팅, 누른사람/눌린플롯 저장)
# 공개
# 동플롯 : 선공스킬 확인 - 있을시 사용 여부 확인 - 없을시 랜덤 행동 처리
# 선공 행동 확인 - 회피 - 처리
# 후공 행동 확인 - 회피 - 처리
# 스킬 {'이름':이름, '거리':거리, '코스트':코스트, '유형': 유형, '효과':효과, '태그':태그}
# 효과는 효과 문장, 태그는 특수한 인법 태그 (생명소비 / 선공 / 플롯 / 타이밍)
