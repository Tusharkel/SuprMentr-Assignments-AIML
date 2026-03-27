'''
Assignment (07/03/2026)

Assignment Name : KNN in Real Life
Description : Explain Netflix-like recommendations using KNN and create a small similarity example.
'''

import math

movies = {
    "Inception":         [1, 0, 0, 1, 1],
    "The Notebook":      [0, 1, 0, 0, 1],
    "Avengers":          [1, 0, 0, 1, 0],
    "Titanic":           [0, 1, 0, 0, 1],
    "Interstellar":      [0, 0, 0, 1, 1],
    "The Hangover":      [0, 0, 1, 0, 0],
    "Iron Man":          [1, 0, 0, 1, 0],
    "La La Land":        [0, 1, 1, 0, 1],
    "Guardians Galaxy":  [1, 0, 1, 1, 0],
    "A Beautiful Mind":  [0, 0, 0, 0, 1],
}

def euclidean_distance(v1, v2):
    return math.sqrt(sum((a - b) ** 2 for a, b in zip(v1, v2)))

def recommend(watched_movie, k=3):
    target = movies[watched_movie]
    distances = []

    for movie, features in movies.items():
        if movie == watched_movie:
            continue
        dist = euclidean_distance(target, features)
        distances.append((movie, round(dist, 4)))

    distances.sort(key=lambda x: x[1])

    print(f"\nYou watched: '{watched_movie}'")
    print(f"Features → Action={target[0]}, Romance={target[1]}, Comedy={target[2]}, Sci-Fi={target[3]}, Drama={target[4]}")
    print(f"\nDistances to all other movies:")
    for movie, dist in distances:
        print(f"   {movie:<22} → distance: {dist}")

    print(f"\nTop {k} Recommendations (KNN, k={k}):")
    for i, (movie, dist) in enumerate(distances[:k], 1):
        print(f"   {i}. {movie} (distance: {dist})")

recommend("Inception", k=3)
recommend("The Notebook", k=3)