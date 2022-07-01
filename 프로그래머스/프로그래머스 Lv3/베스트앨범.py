from collections import defaultdict

def solution(genres, plays):
    answer = []
    genre_dict = defaultdict(list)
    sum_dict = defaultdict(int)
    
    for idx, (genre, play) in enumerate(zip(genres, plays)):
        genre_dict[genre].append((idx, play))
        sum_dict[genre] += play
    
    # TODO: sum_dict을 sort하기
    sorted_sum_dict = sorted(sum_dict.items(), key = lambda x: x[1], reverse = True)
    
    for genre, sumNum in sorted_sum_dict:
        # sort해서 2개까지 뽑아 answer에 넣기
        finalArr = sorted(genre_dict[genre], key = lambda x: x[1], reverse = True)[:2]
        for f in finalArr:
            answer.append(f[0])
        
    return answer

print(solution(	["classic", "pop", "classic", "classic", "pop"], [500, 600, 150, 800, 2500]))