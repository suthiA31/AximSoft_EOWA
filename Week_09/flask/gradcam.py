from tensorflow.keras.models import load_model

model = load_model("model/efficientnet_finalch1.keras")

print("="*60)
print("MODEL TYPE:", type(model))
print("="*60)

print("Inputs:")
print(model.inputs)

print("Outputs:")
print(model.outputs)

print("="*60)

for i, layer in enumerate(model.layers):
    print(i, layer.name, layer.__class__.__name__)

print("="*60)

base = model.get_layer("efficientnetb0")

print("Base Model Input:")
print(base.input)

print("Base Model Output:")
print(base.output)

print("="*60)

print(base.summary())