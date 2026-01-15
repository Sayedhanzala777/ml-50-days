# Day 01 - Introduction to Machine Learning
# Simple example to simulate prediction logic

# Sample data (hours studied vs marks)
hours_studied = [1, 2, 3, 4, 5]
marks = [35, 40, 50, 65, 75]

# Simple average-based prediction
def predict_marks(hours):
    avg_marks_per_hour = sum(marks) / sum(hours_studied)
    return hours * avg_marks_per_hour

# Test prediction
test_hours = 6
predicted_marks = predict_marks(test_hours)

print("Predicted marks for", test_hours, "hours of study:", predicted_marks)
