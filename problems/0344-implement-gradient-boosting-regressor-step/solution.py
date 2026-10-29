import numpy as np

def gradient_boosting_step(X, y, predictions, learning_rate=0.1):
    X = np.asarray(X, dtype=float)
    y = np.asarray(y, dtype=float)
    predictions = np.asarray(predictions, dtype=float)

    # For squared loss, the negative gradient is the residual
    residuals = y - predictions

    best = None  # (sse, feature, threshold, left_value, right_value)
    n_samples, n_features = X.shape

    for f in range(n_features):
        for t in np.unique(X[:, f]):
            left = X[:, f] <= t
            right = ~left
            if not left.any() or not right.any():
                continue
            # The stump predicts the mean residual in each region
            left_val = residuals[left].mean()
            right_val = residuals[right].mean()
            pred_stump = np.where(left, left_val, right_val)
            sse = np.sum((residuals - pred_stump) ** 2)
            if best is None or sse < best[0]:
                best = (sse, f, t, left_val, right_val)

    if best is None:
        # No valid split (e.g. all feature values are identical)
        update = np.full(n_samples, residuals.mean())
    else:
        _, f, t, left_val, right_val = best
        update = np.where(X[:, f] <= t, left_val, right_val)

    return predictions + learning_rate * update