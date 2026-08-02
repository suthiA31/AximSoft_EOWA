from prediction import predict_image

disease, confidence, probabilities = predict_image(
    "test.jpg"
)

print(disease)
print(confidence)
print(probabilities)