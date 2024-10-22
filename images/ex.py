def load_reviews(file_name):
    """Загружает отзывы из файла"""
    with open(file_name, 'r', encoding='utf-8') as f:
        reviews = f.readlines()
    return reviews

def analyze_reviews(reviews, positive_keywords, negative_keywords):
    """Анализирует отзывы и возвращает статистику"""
    total_reviews = len(reviews)
    total_words = 0
    positive_count = 0
    negative_count = 0

    for review in reviews:
        words = review.split()
        total_words += len(words)

        # Определяем, является ли отзыв положительным или отрицательным
        if any(word.lower() in review.lower() for word in positive_keywords):
            positive_count += 1
        elif any(word.lower() in review.lower() for word in negative_keywords):
            negative_count += 1

    avg_words = total_words / total_reviews if total_reviews > 0 else 0
    positive_percentage = (positive_count / total_reviews) * 100 if total_reviews > 0 else 0
    negative_percentage = (negative_count / total_reviews) * 100 if total_reviews > 0 else 0

    return total_reviews, avg_words, positive_count, negative_count, positive_percentage, negative_percentage

def display_statistics(total_reviews, avg_words, positive_count, negative_count, positive_percentage, negative_percentage):
    """Выводит статистику по отзывам"""
    print(f"Общее количество отзывов: {total_reviews}")
    print(f"Средняя длина отзыва: {avg_words:.2f} слов")
    print(f"Положительных отзывов: {positive_count} ({positive_percentage:.2f}%)")
    print(f"Отрицательных отзывов: {negative_count} ({negative_percentage:.2f}%)")

# Ключевые слова для анализа
positive_keywords = ["отличный", "прекрасный", "рекомендую", "доволен"]
negative_keywords = ["ужасное", "разочарован", "не понравилось", "совсем не то"]

# Загрузка и анализ отзывов
reviews = load_reviews("images/input.txt")
total_reviews, avg_words, positive_count, negative_count, positive_percentage, negative_percentage = analyze_reviews(reviews, positive_keywords, negative_keywords)

# Вывод статистики
display_statistics(total_reviews, avg_words, positive_count, negative_count, positive_percentage, negative_percentage)