import joblib

model = joblib.load(
    "/home/aximsoft/Documents/AximSoft_EOWA/WEEK_12/models/improved_decision_tree.pkl"
)

print(type(model))
print(model)