import pickle

# Load the trained model
with open("house_price_model.pkl", "rb") as file:
    model = pickle.load(file)

# Print the number of features
print("Model expects:", model.n_features_in_, "features")

# Print the feature names (if available)
if hasattr(model, "feature_names_in_"):
    print("Feature Names:", model.feature_names_in_)
else:
    print("Feature names are not available in the model.")
