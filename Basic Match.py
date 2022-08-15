# Basic matching engine

def matchingWords(sentence1, sentence2):
    words1 = sentence1.split(" ")
    words2 = sentence2.split(" ")
    score = 0
    for word1 in words1:
        for word2 in words2:
            if word1.lower() == word2.lower():
                score += 1
    return score


if __name__ == "__main__":
    sentences = ["python is a good", "this is snake is python", "he is good boy", "play with him"]

    query = input("Enter query string: ")
    scores = [matchingWords(query, sentence) for sentence in sentences]
    print(scores)
    sortedSS=[sentScore for sentScore in sorted(zip(scores, sentences)) if sentScore[0]!=0]
    print((sortedSS))
    sortedSSreverse = [sentScore for sentScore in sorted(zip(scores, sentences), reverse=True) if sentScore[0]!=0]
    print(sortedSSreverse)
    print(f"{len(sortedSS)} results found!")
    for score, item in sortedSS:
        print(f"\"{item}\": with a score of {score}")
