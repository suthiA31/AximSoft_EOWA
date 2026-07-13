from utils.data_loader import load_data

df = load_data()
print(df.shape)

print(df[[
    "order_id",
    "customer_unique_id",
    "seller_id"
]].head())
print(df.columns.tolist())